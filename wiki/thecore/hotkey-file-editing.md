---
type: Reference
title: Hotkey file editing
description: How TheCore community hand-edits the StarCraft II `.SC2Hotkeys` text file — what the in-game editor cannot express, what the game writes back on its own, and the file conventions worked out in Discord between 2019 and 2026.
tags: [thecore, starcraft, discord, hotkeys]
source: "TheCore Discord #general 389438169520799746, 2019-08-24..2026-08-27"
---

# Hotkey file editing

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-389438169520799746.jsonl`; a few 6-digit suffixes collide in the 23k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## Binds the in-game editor refuses but the file accepts

- **The editor gives one key plus one alternate per action; the file takes as many comma-separated keys as you like and the game reads all of them.** This is why TheCore ships as a text file. jaydik, 2020: "each in-game action only allows 2 hotkeys, one key and one alternate ... so things get messy when we're adding like 10 keys for a single action" (949022, 940483), answering "is there something actually wrong with remapping keys in game" (852868, 680553). Restated in 2022 — "by editing the hotkey file, we can set any number of alternate hotkeys" (607121) — and again (483486, 564220, 831264). Worked example: to add Backspace to Zerg select-larva, first move the Lair/Hive upgrade off Backspace in the editor, then append `backspace` to the select-larva line (692856, 931078).
- **Edennil's rule for when you must leave the editor** (032221, 2024-12-12): "the only cases where we have to edit the file instead of in-game are: - when we want more than 2 keys for a hotkey (e.g. select larva, rapid fire) - if there is a bug where a hotkey doesn't show in the in-game editor (i can't remember the list for these, but there are/were co-op and campaign keys in this)". Everything else is doable in game.
- **A comma separates key combinations for one command.** `CameraSave7=Alt+U,Control+Alt+Slash` is one camera on two combinations (245579, 751553, 811530); the 6c camera block has the same shape (078996):

  ```
  CameraSave0=Control+Shift+0,Control+Alt+P
  CameraSave1=Control+Shift+9,Control+Alt+O
  CameraView0=0
  CameraView1=9
  ```

  CoreLite ships `Halt=5 / Land=4 / Lift=5`; Altafen's fix is `Lift=5,6`, "a comma-separated second key, which the in-game editor will not give you" (993133); ScaryMouse instead swaps lift and land, since only lift clashes (783090). Edennil keeps `/` on the thumb and adds an alternate drop key on an index key — not `'`, which is hold position (366731, 576640).
- **The canonical editor-impossible line is `ControlGroupAppendAndSteal3=Control+O,Alt+J`** (377354, 252497). `Alt+J` adds a new town hall to the `O` group under the same modifier as create-camera, so one Alt hold does both: select the town hall, hold Alt, press `J`, then `0`/`9`/`8`/`U` to overwrite the camera (184882, 017415). The alternate is missing from the spreadsheet (646766, 314960), which confused readers of the opening-sequence instructions (071650, 353308). Described from 2020 on as add-to-CG3 on both `Control+O` and `Alt+J` (168134, 282508, 428200, 025738, 033940), as "alt+j is a secondary bind for ctrl+O, pairing camera with control group" (032973, 486368, 103499), as the only control group carrying an alternate and the reason the Alt hold works (439645, 957171, 250236, 052570, 757766, 359923, 209332), and as an instruction: "If Alt + J isn't an alternative for 'Add + Steal to your CC/Nexus/Hatchery control group', then add it as an alternative" (064160, 623804, 429959). Edennil uses Alt+J, with Alt+0 also available (260260, 026728, 052618, 447316); for Zerg it adds hatcheries without breaking out of camera creation (540958, 672394). `alt+J` and `alt+O` are not interchangeable: `alt+0` and `alt+J` set the home camera, `alt+O` sets camera 5 or 6 (836724).
- **Alternates are the layout's main file-level trick, and the point is avoiding finger repetition.** Select-larva carries many alternates, so instead of `K` then `P` you hold `P` to make drones (950292, 890089); "the hotkey for nearly every unit is also bound to select larvae alternate" (954524); `P` is an alternate build-basic for the same reason (930753). Select-larva is alternate-bound onto the key of the unit you are morphing — "have select larva alternate bound to that key / so to build zerglings you wouldn't go K-; / you'd just hold down the semi key", called "actually huge" (635624, 687849, 740426, 374259) — which is also why morph lair (423220) and the hatchery upgrades (845600, 611603, 602365) sit on awkward keys. `;` selects larva *and* builds a zergling in one rapid-fire press, queen on `'` (497350, 511105); SuperSquare wanted `;` for queen and was talked out of it (459284). Terran: alternate-bind marines to `K` so a six-marine batch is `;k ;k ;k` (824799, 044161, 297354). NReilingh added `/` as an alternate build-factory so a mis-pressed build-advanced cancels by tapping the same key again, accepted by JaKaTaK (245029, 729788); build advanced has no alternate and cannot easily get one without costing you stop (466921, 672898, 343501), so it is pressed with the thumb even though the finger chart puts `/` on index — the chart is a guideline (787840, 776616).
- **Concrete alternate pairs given as file edits**: build basic on `K` and `P` (976497, 552960); liberator siege on `K` and `[`, `[` being the rapid-fire one (576207, 964289); siege tank up `K`, down `P` (230348); ravager bile on `P` for rapid fire (952558) and in 5.0 on `P` and `K` so you "hit k 3x per tank to break siege lines" (409749, 729118); Mell00yell00 moved liberator siege to `K` for consistency, lost rapid fire, added `[` to get it back (171594, 800405); `-` works as an alternate to `/`, useful for shift injects (198486). The alternates broke originally because `K` used to be a control group and `I` the command key; Jak moved the command key to `K` and cleared only the errors the editor reported, leaving alternates unbound (449162, 160084, 772964, 042816) — fixed in 6g.
- **The same command on two keys with different rapid-fire settings is the clearest editor-impossible bind.** Yamato on `K` (not rapid-fire) and `P` (rapid-fire) (330304, 197325, 820801). Also `P` as a second lift and reaper grenade key (243444), `K` for the precise reaper grenade with `P` or `[` rapid-fire (774928), the Liberator's two siege keys (103681). Corrosive bile's alternate `;` in v5 *is* rapid-fired, so you get both (379966, 782484); the sheet shows bile on `k` and `p`, "one option without rapid fire and one with" (623136).
- **Rapid fire is a file-only edit: add your spell key as an extra alternate to "Choose Ability or AI Target".** Siaal's walkthrough (457941 through 896641): the left click that places a fungal reticle is a "select AI target" input, so "to make a key RF, just add it to the list of alternatives for select target ... (which needs to be done by editing the actual file, cannot be done through the in-game ui)". It sits on the fourth tab of the hotkeys UI with the generic hotkeys (150366, 858463); doubled up, you hold the key and your refresh rate fires the ability repeatedly (685142). "Putting a lot of spammable spells on RF's made the game so much more enjoyable for me" (840606). Edennil (815756): "you'll [find] a hotkey called 'Choose Ability or AI Target'. By default this is left click. All this ability does is 'left click' for you when you are using an ability or spell (building a barracks is using an ability). TheCore makes *most* keys rapid fire." That is why `K`,`P`,`P` places a barracks (438672). Which keys are rapid fire is a spreadsheet column (646260, 876628). Rapid fire makes a key send what left click sends, hence double-tap-to-place only works on rapid-fire keys (076938, 555457).
- **`K` is deliberately the one comfortable non-rapid-fire key**, for storm, forcefield, EMP and fungal, which do not stack (980630, 967755, 928114); "if you hold down k you will stim your army to death" (664512); `J` is likewise not rapid fire (318539, 735765). As of 2020-05-05 `K` was the only one; a second would have to be `-`, since `'` is hold position and stop cannot be taken, unless you cut into rapid-fire warp-ins (105674, 900948, 596881, 926132); JaKaTaK left the case for a non-rapid-fire feedback open (004042). Rapid fire ships pre-configured (043385), though AvroArrow found `k` rapid-firing when it should not (600627, 509106), symptom `k` firing twice and building a pylon instead of a cyber core (632031), blamed on a 150 ms repeat delay (839026). Preference order is `P` first, then `[`, `-`, `/`; `P` for comfort, the rest "pretty controversial" (314369, 930197, 043029). Rapid fire is scarce: recall and chrono cannot have it, and load/unload constrains where the PF worker goes (875763, 799752); for Terran and Protoss make unload rapid-fire and `/` not, moving unload to `[` (889647, 642149, 320583), not worth it for Zerg (363059). Liberator siege wants rapid fire, tank siege does not (614954). Put overlord speed where rapid fire cannot reach it (831306). Back-mouse-button warp-ins are about twice as fast because of rapid fire (295819). **Cloud gaming (GeForce Now, Boosteroid) cannot load an edited file**, so you lose the extra rapid-fire and select-larva alternates; pick two rapid-fire keys, Edennil suggests `;` and `p` (743782, 966294).
- **Mouse buttons are ordinary key tokens in the file, so you can bind them when the client refuses.** In `MorphMorphalisk/Queen=Slash,Minus` replace `Slash` or `Minus` with `ForwardMouseButton`, `BackMouseButton` or `MiddleMouseButton` (363230); `LeftMouseButton` and `RightMouseButton` are also valid (580180). Heliac's file has `WarpIn=Shift+BackMouseButton` (729290). Warp gates go on `Shift+MouseButton4` because you hold Shift anyway for rapid-fire warp-ins, leaving plain MB4 as tab-through-group (285709); Poletes puts select-all-warp-gates on shift+BMB (453077); rebind warp-in to shift plus a key rather than a bare key — "it's 2x faster if you do it that way" (130944, 153088). Several put select-all-warpgates on a side button (846657); Mell00yell00 pings with the forward one (190926). Next/previous subgroup live on the mouse buttons in every Core version and are missing from the spreadsheet (334421, 919070, 999730, 306556, 157652, 096778, 877844, 281809, 928960, 251850, 470608); "tab" in Core documentation means those thumb buttons, not the Tab key (549483, 014194, 582080). Bind both directions: with back tab bound, "robo is always back tab x1" whatever else you built (834202, 708497, 210746). With no side buttons, move Patrol off `Y` and put next-subgroup there (130569), or pick any unused key; CoreLite keeps Tab and puts nothing on the mouse (507092). JohnKavinski needs next/previous subgroup for turning in-base CCs into orbitals and changed his mouse grip for it (849785). AvroArrow's alternative: gateway/robo/starport on one key, cycle types with the side buttons (384384). **SC2 cannot bind mouse scroll up or down** without external software (200110, 303012); extra buttons get mapped to keyboard keys in Razer Synapse or Logitech G Hub (717810, 260989). No file token for the scroll wheel was ever found (177661), asked again in February and still unresolved, with JuicyJuuce suggesting you "experiment with words to that effect" (079244, 747099, 908566, 294770).
- **Per-context scoping: `Command/Unit=Key` binds a command only on the unit or building that owns it.** ketchupfriend found `Immortal/RoboticsFacility=SemiColon` in the shipped 6.0 US QWERTY file where the spreadsheet says `K` (165481). The inject line is `MorphMorphalisk/Queen=Slash,Minus` (363230, 677467). Heliac's personal edit list for `TheCore6g_right_US_qwerty` is the largest worked example in the channel (729290, 566835, 489064, 347274):

  ```
  Stimpack/BarracksTechLab=SemiColon
  ResearchShieldWall/BarracksTechLab=P
  ResearchPunisherGrenades/BarracksTechLab=K
  Land=BracketClose
  Lift=BracketClose
  LurkerCancelHoldFire/LurkerMP=Minus
  StopGenerateCreep=BracketClose
  WarpIn=Shift+BackMouseButton
  MedivacSpeedBoost/Medivac=P
  BatteryOvercharge/Nexus=SemiColon
  TempestResearchGroundAttackUpgrade/FleetBeacon=P
  Lower/SupplyDepot=K
  Raise/SupplyDepotLowered=P
  MassRecall/Mothership=K
  TemporalField/Mothership=P
  BansheeSpeed/StarportTechLab=SemiColon
  ResearchRavenEnergyUpgrade/StarportTechLab=K
  ResearchVoidRaySpeedUpgrade/FleetBeacon=SemiColon
  AnionPulseCrystals/FleetBeacon=K
  Carrier/Stargate=Minus
  Mothership/Nexus=Minus
  ```

  Scoping also fixes the Hellion/Hellbat collision: `ResearchHighCapacityBarrels/Hellion=Q` "or whatever garbage button you want" — blue-flame research on `I` takes priority over the morph even before the research is done, and an explicit research bind clears it (128444, 548619, 444189, 223435); "i assume the same is true of smart servos" (033339). pinion's 2020-08 block pins commands out of the way with blank right-hand sides (542170):

  ```
  BurrowUp=SemiColon
  Spray=Period
  LoadOutSpray=
  LoadOutSpray@1=
  LoadOutSpray@14=
  ```

  Other scoped lines quoted: `Salvage/SensorTower=` versus `Salvage/Bunker=`, split in 5.0.14, so up-to-date left Core6 leaves Sensor Tower salvage unbound and right Core6 has it on the default `V` instead of `P`, alongside an undefined `CameraTurnRight=` in the left US QWERTY file (193567); and `CameraCenter=Alt`, cameras on Alt+`0`, Alt+`9`, Alt+`8`, Alt+`u` (623342).
- **Campaign- and co-op-only commands appear in the editor only after you load that mode.** Edennil (588127): "Open up a co-op game. Then quit to get. (Just to get the in-game editor to show co-op) … For every command card unique to that hero I literally just add new abilities". Nova Covert Ops: "Nova campaign might exist for v5 (I can't remember), but I know it doesn't exist for v6" (491732); Mell00yell00 hand-built Nova keys without posting lines (395078). Nova per-ability file lines: not discussed in the channel.
- **Two commands on one key is a file-level fact SC2 tolerates in melee and calls a conflict elsewhere.** The check runs against the command set of the last mode played. Siaal (913665, 2020-01-19): "the campaign, coop and, *especially* arcade game modes haev extra hotkeys that will potentially conflict with the core that the game doesn't usually worry aobut if you only play melee game modes"; "the hotkeys interface will change to resemble the last thing you played" … "if you just came out of coop you'll have all the coop commanders" (410625, 146624); "it'll also show things as unbound if it detected a conflict" (038868). When both commands exist in the current mode, one silently wins: "I believe cloak gets the priority and the main keybinds for burrow/unborrow don't work" (444948); "the default blueflame hotkey is `I` so it takes priority over morph" (724166). Edennil: "sc2 is really bad at letting you know what hotkeys are even available, how they conflict, and where they are used" (973519). The internal algorithm of the check, beyond "same key, both available in the current mode, one wins", is not discussed in the channel.
- **In melee the conflict warning is cosmetic unless you act on it.** Siaal (105812, 2020-01-15): "so event hough it shows attack as unbound it'll still be bound to ; unless yout ry to fix the conflict and then if oyu go back into melee everything will be back to normal"; "ther's a good chance that as long as you spam cancel it won't actually rewrite the file" (038868).
- **Same-key pairs the editor rejects**: burrow and cloak — "In the core both are set as the same key but in campaign/coop it will cause a conflict" (814880), "stukov's infested banshee causes conflicts in multiplayer with both cloak and burrow" (917717, 071124), "the only way to to avoid hotkey conflicts is to move either burrow or cloak" (333221); hold position versus Spawn Changeling & Consume (613358); Stasis Ward and hold position on `'` (492461); hellion morph versus blueflame research on `I` (724166, 548619); morph to lurker versus lunge (999624); create-camera on Ctrl+Shift versus held Ctrl for cameras 5, 6 and 8 (577229).
- **A file-written modifier duplicate of a plain key is not honoured.** JimKlide wanted `Alt+J` as a second inject key alongside plain `J`: "But adding it directly in the hot key configuration results in sc2 telling me about some conflict on launch" (296287, 445130, 714708); Edennil: "Correct on all accounts" (462654). The workaround is outside the game — keyboard firmware or AutoHotkey making alt+J emit a plain J (535377, 118770).
- **Modifier fall-through: `Control+<key>` falls back to the unmodified command when the modified version is unbound, `Alt+<key>` does not.** So Alt+<inject key> will not inject, which breaks NoTruePunk's scheme of putting all cameras on Alt for Zerg (340162); v5 has the same shortcoming (392896).
- **Only the fourth (global) tab accepts modifiers at all, and editing the file does not get around it.** The menu has four tabs — Zerg, Terran, Protoss, global — and only the fourth takes a modifier; "even if you edit the file manually alt+l will just be interpreted as l" (298691, 627934, 493640). Flatly: "It's physically impossible to use modifiers to build buildings or units, yes" (084658), with Altafen's caveat "(without qmk or something)" (633503). This killed SwordSmith's modifier-layer proposal (093472, 258826). Anything in the Global section can be layered under a modifier (034513), "u can layer and layer and layer" (711765) — the mechanism behind the camera-on-a-modifier schemes. **Autocast is always `Alt + <key>` and cannot be changed** (179452). Map ping lives under Unit Management, not Global -> UI (587340, 948041), suggested on `f7` or Ctrl+Shift plus something (932786).
- **Three-modifier combinations are "banished" and several do nothing at all.** Bose's triple-modifier add-to-control-group did nothing (347645, 948265); Altafen: "keys with 3 modifiers are 'banished' and meant to not be used" (055761, 242240); "control + alt + shift + key = banished. Don't use" (012018). The intent is that nothing is left unbound: toggle-fps-counter and friends are parked on Ctrl+Shift+Alt+W so the file has no holes (655680, 514772), and banished functions generally sit on Ctrl+Shift+Alt+key (711219, 381629, 523813, 346635), rally point included (442827). Edennil's reading rule: "if you see keys with impossible combinations, you aren't meant to press it" (941594); use Add+Steal instead of Add (629211, 889050, 998570). Plain add-to-control-group is the standard banished command, buried there because a unit in two groups is rare (288833, 680373, 023360, 864926, 040313, 288024, 454047); Mell00yell00 instead parks create/steal on `ctrl+alt+shift+CG` (435113). Even under Core+, Edennil sticks to six combinations — Control, Shift, Alt, Control+Shift, Control+Alt, Shift+Alt — and warns Control+Alt and Shift+Alt now centre on selection, since Alt+key is create-camera-and-center; older Core+ files moved create-camera onto a two-modifier combination for that reason (473657). Select-all-warpgates is parked on Control+Alt+Shift+F9 and now deserves a real bind (972251).
- **Binds that silently fail.** The v5 file's `ControlGroupRecall9=Control+sC` is an invalid string the game drops without complaint; it should be `Control+comma`, leaving select-CG9 unbound while `,` still add/steals into CG9 (942420, 825793, 975647, 945216, 425483, 367336, 588706, 149086, 923295, 277565). Siaal treats it as known and asks new v5 users to check (445043); Sora patched it by hand (343751). A literal `/` in a bind line is ignored — SC2 spells it `Slash` (504263, 144330). On UK QWERTY the US file's `Backslash` binds came out as `Enter` and SC2 silently unbound all of them, chat being on Enter (609214); the fix is the swap under key names below (875881, 441444), and a later apparent relapse was a hidden US layout in the Windows registry, not the file (026823). **The editor can silently unbind a key everywhere:** open it, click rebind, press a key that is already bound, and the existing bind is destroyed (744896, 565440). Assigning an alternate gives "A primary hotkey was unbound" when that key is already used at the same level or globally, and SC2 may not register the Menu key at all (252544, 004564). The "essential hotkeys unbound" popup can survive a full profile reinstall: pinion deleted the profile and local file, re-imported a 2018 backup and edited it in Notepad, and the UI still showed Spray and Unburrow unbound though unburrow worked in game (272175, 886923); Poletes' relog-and-Ignore fix did not stick (121035, 704702). Unresolved. **A file from the wrong keyboard region silently breaks camera keys** — SieStein's v5 cameras would not save or recall, cause being the file not matching his layout (937503, 341696, 819047, 375421).

## What the game writes to the file itself

- **One file per profile, but SC2 keeps a separate command set per game mode, and switching modes silently corrupts the file.** Edennil's diagnosis (876776): "Blizzard has separate hotkey settings for different game modes... it shows the hotkeys for the last game mode you played. When you want to edit campaign or co-op keybinds, you have to load into the campaign or co-op first... Some arcade maps also are like this". Siaal in 2020 said the same: "the hotkeys interface will change to resemble the last thing you played" … "if you just came out of coop you'll have all the coop commanders, if you jsut came out of campaign, you'll have all the story units" (410625, 146624). ScaryMouse: "SC2 in general messes up hotkeys when you switch between different game modes", so keep a separate file per mode (842399, 222972).
- **Multiplayer (melee) is the safe mode; campaign, co-op and arcade are the ones that rewrite.** Campaign: logging into the campaign with a 5.0 profile rebinds a batch of keys and they stay wrong back in versus (Amcore 064000, 2019-09-14), though he corrected himself the same day — "it doesn't look like it messes up my 1v1 or competitive key bindings, it just doesn't work for the campaign" (055829). Lady Interstellar (094464, 2021-01-27): "If I boot up the campaign, it deletes half of my pre-existing configuration. Same for co-op". Arcade is the worst: "I played a game on the arcade and now my 6g file is completely borked" (055690, 2020-01-15); "especially arcade is weird, everyone keeps reporting that no matter what they play attack is always unbound" (294157). Coop, campaign and arcade can all make SC2 rewrite or merge the profile, and several people lost or corrupted binds that way (530665, 750404, 222922). Concrete arcade damage: the LOTV hotkey trainer arcade map injected a stale "Ballistic Range on Tech Lab" line into possum's file, which is why Corvid Reactor and Advanced Ballistics were missing (016168) — "Line 813 is medivac boost, which isn't an upgrade anymore. But the line for it's hotkey assignment is still there and is the same as for Corvid Reactor" (959996, 066011). LordEng1ish hit the same class of bug after loading campaign — Starport, reaper cluster bomb, ghost sniper and cloak, thor immortality protocol and more all unbound — and a fresh us_qwerty v6 verified them bound in multiplayer (159037, 852348).
- **Older-expansion (Wings of Liberty / Heart of the Swarm) multiplayer storing hotkeys separately: not discussed in the channel.** The nearest thing is Siaal keeping separate HotS and LotV files by hand (739221, 2020-04-07).
- **When the write happens: on save in the editor, or when you accept the conflict prompt on launch.** Joli Boli's borked file came from exactly that: "It asked if I wanted to save changes and I honestly don't remember what clicked" (191489). Spamming cancel avoids the rewrite — "ther's a good chance that as long as you spam cancel it won't actually rewrite the file" (038868).
- **Keys absent from the file fall back to SC2 defaults, not to nothing.** Edennil on Core 5 files after a patch (407900, 2022-04-07): "There might even be new abilities that didn't conflict with a hotkey and so have their default"; "Those are the SC2 defaults and because the defaults didn't interfere with the core 5 hotkeys, the sc2 client assigned them the default. In the core 6, the keys did interfere with the default, so it left them unbound" (642728); "The client just automatically assigned them a value, even though those keys aren't really usable with the core 5" (016778). That is why a fresh file can look fine and still have unusable binds you never chose.
- **The fix for first-time setup: do it in a custom melee game, alone, before touching any other mode.** Edennil's recipe, given twice (103372, 624214): "Go into a custom melee game with just yourself (not arcade) to make sure that your client is looking at multiplayer hotkeys. Download a fresh hotkey file and make the changes I recommend in the faq. Then make a copy of that file and save it somewhere safe." The 2020 equivalent was to switch to Default or Grid before launching arcade (056320).
- **On pinning every command with an explicit line: no general rule was ever stated.** The advice in the channel is only the two practical forms — hand-edit when you need more than two keys or when a command does not show in the editor (032221) — and pinion's blank right-hand sides parking commands out of the way, `LoadOutSpray=` through `LoadOutSpray@14=` alongside `BurrowUp=SemiColon` (542170).
- **On diffing after playing a mode: not discussed in the channel.** Diffing is only ever recommended version-to-version — "Then run a diff on the 2 files to see what has changed" (Edennil 604490, 2019-11-08) — because there is no changelog between lettered betas (260776), with Bitstorm using diffchecker for the same job (505294). The comparable workflows people do describe are bind-then-read-back and play-and-bind-as-you-go: PiG "just went through adding them using ingame UI one at a time then checking text file to see what it said" (650058), and JuicyJuuce "i basically played all the campaign missions and bound keys as i went (keys appear and disappear depending on the mission you are on)" (621170).
- **Back up the file outside the StarCraft II folder, where the game cannot reach it.** The strongest form is Siaal's: "backup your hotkey files so starcraft can't suddenly cahnge them for you" (227476, 118484), specifically before you play anything that is not multiplayer. ScaryMouse: "keep a backup of the hotkey file somewhere outside of the Starcraft II folder, where the game can't mess with it" (407690, 517963; nthimoni 729341), repeated in 2021 (605248) and by Mell00yell00 in 2022 (819399). Back up before adding campaign or co-op binds yourself — "Just backup your hotkeys before you do, sometimes conflicts do weird things" (983314) — a job Mell00yell00 puts at 15-20 minutes (010428). Blizzard does not sync the file between machines, which is a second reason to keep your own copy (984105). Copy your file before editing it (019136), and keep separate files for multiplayer, campaign and co-op, maybe one per co-op commander (249931, 875329) — campaign conversion alone takes 10-20 minutes (952745).
- **Read-only is mentioned exactly once, by Siaal: "set your file to read only and deal with the errors"** (608896, 2020-06-15). Nobody follows up on it.
- **Version control is discussed only for distributing TheCore, never for a personal file.** JuicyJuuce (529074): "the dream has been to transition from the google drive to a git repo but we never finished that project", pointing at github.com/TheCoreHotkeys. Nobody recommends git for their own hotkeys.
- Someone asked whether SC2 can be made to reload a text-edited file quickly. Nobody answered (727208).

## Where the file lives, and picking it in game

- **Windows: `C:\Users\<you>\Documents\StarCraft II\Accounts\<accountnumber>\Hotkeys`** (416906, 500924; verbatim again at 092991, repeated 634172; 748648; `c:/users/<user>/Documents/StarCraft II/Accounts/<number>/Hotkeys/` 590046). The 2020 form spells out the second level: `Documents\Starcraft II\Accounts\<account_number>\<second_number>\Hotkeys` (907860). The account number is Blizzard-assigned and opaque (269446). **Never the install directory** — "Do NOT look in the install directory... `C:\Program Files (x86)\StarCraft`" (226607); putting it in Program Files is the single most common install mistake (027028, 346344, 081216, 327337).
- **macOS: `~/Library/Application Support/Blizzard/StarCraft II/Accounts/<id>/Hotkeys`** (648761, 279144; 167971, confirmed 766986).
- **The `Hotkeys` folder does not exist until you save a custom profile in game.** It is a Blizzard "space saver" (891530); create any hotkey set in the in-game editor, save it with something changed, and the folder appears (051925, 616682, 985216, 311121, 499728, 997435, 350448, 757753, 258624, 163941). Added to the FAQ 2022-02-13 (663755, permalink 942491990501777408) after JabaWaba lost time to it (252365, 187772). See [faq](/faq.md).
- **Finding the right account folder: open Replays in game and use "show in folder" / the folder icon** (214302, 342976, confirmed 601729; 948256, 995584; 180477; 596959). On Mac, search "hotkeys" in Finder (405217); on Unix, `find / -name "Hotkeys" -type d` (653779).
- **If the file does not show up you are writing to the wrong Documents folder.** Win11/OneDrive redirection is the usual cause (180477, 528384, 898700); Kykeon's case was two account-number folders under `Accounts` (784981, 851409). There is no `Documents\StarCraft II\Hotkeys`, only the per-account one (394056).
- **Installing is two steps: drop the text file in that folder, then pick it under Options -> Hotkeys in game** (179262, 811903). After dropping a file in, close and reopen the hotkeys menu; no SC2 restart is needed (653683, 655942).
- **A profile that "lost all its binds" is usually the wrong profile selected, not a corrupt file.** Joli Boli's scare resolved that way; hotkey profiles sync to Battle.net, so an old one follows you between machines and can be picked by accident (405462, 643531). Two SC2 player profiles can end up with different binds from one downloaded file; the fix was deleting both and re-downloading (751818, 031051, 994695). Use a separate hotkey profile — ideally a separate account — for observing tournaments, since observer binds fight the multiplayer ones (414154, 851107, 915944).
- **If the editor shows abilities that no longer exist (e.g. Infested Terran), enter and exit a custom multiplayer game** to force the correct hotkey set to reload (754730).

## The file, the spreadsheet, and which one is authoritative

- **Since 2021 the answer is: spreadsheet over file, and the spreadsheet's top section over its
  bottom.** Edennil verbatim (222034): "1) Hotkeyfile and spreadsheet might be different. Usually
  spreadsheet is right. 2) Top section of spreadsheet and bottom section of spreadsheet might be
  different. Usually top section is right." The sheet is where Jak made late changes before
  regenerating files in batches, and on genuinely close calls either bind is defensible (433818,
  281546, 313042); #core-info says the same, that the spreadsheet is the most up-to-date source
  (quoted by ketchupfriend 652299). bunfoof, more bluntly: "the spreadsheet has quite a few
  discrepancies compared to the keybinds" (144896).
- **Through 2019 the rule was the opposite: the file was the source of truth.** Shown a camera
  mismatch on 2019-11-09, JaKaTaK answered "spreadsheet is wrong" (628706) and "file is correct"
  (751553). Bitstorm on 6c: "many mismatches with the spreadsheet, the keyfile is authoritive atm"
  (216261), "the hotkey file is correct, the spreadsheet hasn't yet been brought into line" (437147).
  Three days earlier the advice had itself been the reverse — "when in doubt, follow the spreadsheet …
  and modify the hotkey file to match the spreadsheet" (Edennil 258689, 856330). Heliac's version adds
  the changelog: "I have found several inconsistencies in the excel file... take the hotkeys file as
  truth, amended by whatever is mentioned in the changelog thread after the file upload" (130463).
  Individual calls that went to the file: drone and roach, where the sheet says drone `k` / roach `p`
  and the file has them reversed (Deleted User 396508; ScaryMouse 257557); and the stale duplicate
  rows — Nexus appears at both line 60 and line 126, Medivac is duplicated, and the probe on `p` is
  correct while the `k` row is stale, the sheet being Jak's original and never kept current (726239,
  848844, 436966, 085881). It is a US QWERTY sheet (457839).
- The 2019 mismatch that settled it, file version (Bitstorm 078996):

  ```
  CameraSave0=Control+Shift+0,Control+Alt+P
  CameraSave1=Control+Shift+9,Control+Alt+O
  CameraView0=0
  CameraView1=9
  ```

  The spreadsheet instead listed Create Cam 1 => Shift+9, Ctrl+Alt+P; Create Cam 2 => Shift+0,
  Ctrl+Alt+O; Jump to Cam 1 => 9; Jump to Cam 2 => 0. Note the comma: one command carrying two key
  combinations, the file-only syntax. Same pattern for `CameraSave7=Alt+U,Control+Alt+Slash`, where
  JaKaTaK's reason was "u is a cam now, not a cg" (Bitstorm 245579; 751553, 811530).
- **Catalogue of known discrepancies, none fixed upstream.** bunfoof, August 2021: void ray on `p` in
  the file against `/` on the sheet (509022); workers on `p` in the top section but `k` in the bottom
  (712768, 151932); gateway-to-warpgate on `C` and undocumented (981824), which Edennil notes is
  vestigial since the transformation became automatic in patch 4.7.1 (793128); medivac-only load on
  `-` rather than `\` (530217); neosteel armor on `]` on the sheet but `/` in the download (640720);
  load on `.` in the lower section (496686). From 2022: Mothership Recall should be changed to `k` in
  both places (552509); swarm host unburrow should move off `H` to `[` (580306); Unburrow shows as `-`
  in some spreadsheet cells and `]` in others on the same sheet — "it's not just a discrepancy with
  the file, but a discrepancy with itself" (JuicyJuuce 014593, 392832). Hofbr's v6 errata (829275):
  idle worker and cancel are switched, and "fifth" and "rally" are identical in the suggested-cameras
  table, which also shows ctrl+key to jump while the main table uses shift for cams 5-7. Core 5 has
  its own `Core 5.0` and `Core 5.0 PLUS` tabs at the bottom (895528, 449290), with a known error where
  the roach row shows a `.` inject that should be stop (851392, 274365). Cancel is on `7` in thecore6
  (JuicyJuuce 701120), superseding Edennil's earlier answer in the same period that it was on `/`
  (841950), which he conceded (970241).
- **A converter script generates all the locale and hand variants from one master**, so maintainers do
  not hand-edit about 20 files (ScaryMouse 844220). Known misses: eng bay, hold position and build
  ghost/raven/thor land on tilde instead of apostrophe in the German and UK files (ScaryMouse 539561);
  Corvid Reactor and Advanced Ballistics are bound in `TheCore6g.SC2Hotkeys` under `~\The Core 6.0
  Multiplayer Only\old` on the Drive but unbound in `TheCore6g_right_US_qwerty.SC2Hotkeys` (bunfoof
  119691, 636112).
- **Reading the sheet.** Only the column-A by key-row intersection matters; rows 42/46 are Jak's
  ordering notes (691240, 337735). Cell colours mean "this has synergy with another hotkey" — scan the
  column for the matching colour — and are not a difficulty or priority code (Edennil 287066, 260362,
  850280). Ignore the "unofficial race specific suggested hotkeys" section at the bottom of the FAQ
  doc: those are one person's (Vae) personal changes, for example caustic spray from `/` to `-`
  (240276, 922469).
- **The v6 key-placement rule, verbatim** (184955): zones represent how far a key is from home
  position; abilities are added to the highest zone first; within a zone the hotkey goes on whatever
  key produces that unit, and failing that on the furthest-left key in the zone, since further-left
  keys are easier to press. Earlier versions ignored unit-production synergy and took the easiest key;
  v6 feedback was that matching upgrade to unit is easier to learn (168483, 597632). Restated for
  anyone rebuilding it: keys are grouped into zones by distance from home; commands go to the highest
  zone available, then within a zone to a key with synergy, otherwise left to right (866612). Hence
  Marine on `;` and Marauder on `P` — "Marine is more commonly built, that's why it's on `;`"
  (866612). Challenged on the grounds that `P` is closer for a hand parked on JIOP: "let the hand
  float, don't be rigid with the position" (369472), and "if you prefer marines on `P`, just change
  it" (607400, 187444). **If you ever repeat a finger you are using it wrong — use the thumb** (262073,
  208829), answering complaints that `/-` (twilight council), `kk` (pylon) and `/;` (stargate) look
  like double index presses.

## Key names and how SC2 spells them

- **SC2 spells `/` as `Slash` in the file; a literal `/` in a bind line is ignored** (Siaal 504263,
  Trizztein 144330).
- **The general trick for finding SC2's spelling of any key: bind it to something arbitrary in the
  in-game editor, then read the spelling back out of the file in Notepad** (Trizztein 899157). Siaal
  used that by proxy to learn how a UK `#` is spelled, asking a UK user to look up `researchburrow=`
  (562644, 513522, 376852).
- The discovery method is to bind the key in the UI and read the file back: that is how `Minus`,
  `BracketOpen` and `BracketClose` were confirmed (PiG 612064, answer 650058); `SemiColon`, `Grave` and
  `Apostrophe` also appear in quoted lines.
- **Grave / `~` is mostly free space you can claim.** In the shipped file Alt+grave is a camera center,
  Shift+grave jumps to a notification, grave alone is trash, Ctrl+grave is unbound (226649).

## Key placement rationale in the shipped files

- **Some keys must not move.** Do not put the spawning pool on `;` — holding `;` cancels the build
  order into attack-move ground (440020, 972383). Do not move `K` at all: it is the most comfortable
  non-attack, non-rapid-fire key on the layout, which is why storms, fungals and biles live there
  (701581, 741765, 948360, 540610, 689921; Siaal argued Remko out of swapping `K` and `H`).
  **Buildings, by contrast, can be relocated freely** — they are grouped by priority, not race logic,
  which is why the engineering bay, armory and evolution chamber all sit on `'` (869892, 602934).
- **Why three premium ability keys, `P`, `/` and `K`** (Lord of the Posts 973108): `K` and `P` are the
  two comfiest keys and the split between them is rapid fire versus not. Storm and forcefield must not
  rapid fire, so they live on `K`; `P` is the rapid-fire one; injects sit on `/`, part of the
  five-finger inject position (Siaal 137182, 683901, 609769). `K` is the "activate in combat" slot
  generally — siege, hellbat, lurker burrow, warp prism warp-in (999489, 881725). Build advanced is
  pressed with the thumb even though the finger chart puts `/` on the index; the chart is a guideline,
  not a rule.
- **Use the build-basic key on a different finger than the building.** Edennil: "You always use the
  build key that is on a **different finger** than the building you are trying to build" (446359), so
  `P -> K` for pool — "k -> k is wrong, never do that" (216965); `K` if the building is on index, `P`
  if on ring (497364). Selecting larva on a different finger from the hatchery also moves the command
  card forward a screen (436161). Pylons and depots are `P` then `K`, not a double tap of `K` (jaydik
  233427). **Zerg build keys are meant to be held, not tapped**, except infestors and ultras, which
  overlap queens and lair/hive; for those, tap `k` for select-larva (ScaryMouse 631528, 126022).
  Overlord on `/`, thumb or index, either is fine (088787).
- **Contested: build-advanced on `P`.** will3285 binds `P` as build-advanced instead of a second
  build-basic alias, so armory becomes `P` `'` on the first two fingers and holding shift queues
  advanced buildings (637649, 981928). Poletes rejects it — finger repetition in build basic plus a
  hand shift, "so K shouldn't be the only build basic but P could be" (041867); bro: "really bad idea
  imo, just because pressing / with thumb, always, is very good" (934337).
- **Zerg should hit `/` with the thumb for injects**, because the main base is on camera 0 and the
  index is needed there, which lets you cycle four bases without moving the hand (013771, 814528); in
  v6 only ctrl, alt, shift and sometimes `/` are thumb keys (650122). `O` is the hatchery group and `I`
  the injector queens (jaydik 037254). ScaryMouse's general rule for `/`: thumb for build advanced and
  inject, index for unloading drops, otherwise whichever feels natural (844082, 249300). The inject
  sequence with camera switches reads `i 0 / 9 / 8 / u /` (fight.the.system 893611).
- **There are two home rows: `jkl;` for fighting and micro, `jiop` for macro; `J` is the pivot and is
  usually the main army** (jaydik 130816, 626836; Mell00yell00 698186; ScaryMouse 439015). Core 5's
  home position was o-i-l (jaydik 364092).
- **Production tab-through without mouse side buttons: use the keys TheCore leaves free.** `Ctrl` plus
  `[`, `]`, `'`, `-` and `/` are unbound, so put gateways, robos and stargates on separate control
  groups rather than tabbing (068875, 376073, 253258). **`-` is an ability key in Core 6, not a control
  group**: "Shift+- is not a default control group in thecore6, your hotkeys look normal" (229184); "In
  the images posted, red = ability key" (562331).
- **Spacebar is the popular rebind target** because by default it only hallucinates probes; people put
  idle worker or cancel there (756180). `F8`, or spacebar struck with the palm, serves as an escape key
  (858304, 270214). Mell00yell00 uses spacebar as idle-worker struck with the palm while the fingers
  stay home, combined with ctrl for select-all-idle (067402); Siaal puts **cancel on spacebar**,
  otherwise unbound, "i've never hit it accidently either" (517834).
- **Cancel is `7` in v6** — the spreadsheet's `6` is a known error (489396, 789342). Rationale (805716):
  "Priority was given to abilities over cancel, all of the index finger keys were needed for abilities
  (hatchery is the culprit here). 1 ability key was needed on the thumb for the most common inject
  method. The remaining non-ability keys are added to the closest available key in whatever order Jak
  felt was highest priority. 7 is just the next closest un-used key. It's only 2 keys away from home
  position." He explicitly blesses moving it (805716, 507699; Pokebunny 410250 confirms `7`). Reported
  moves: Laaxus put Cancel on a remapped right Win key and shifted Alt to Escape so his thumb rests on
  the modifier block (701632, 023132, 092059, 389193, via PowerToys 535167); Mell00yell00 puts Cancel on
  `F5`, frees `7` for the rally camera, and pulls the F6/F7 keycaps so he finds F5 by feel (838612,
  001640); pont uses `Cancel=6` to free Space for `IdleWorker=Space` (567923).
- **Attack move is `;` in v6** (290010, 717258, 891486), moved down from `P` "as part of the great
  un-tilting" (Siaal 720074, 486057), and `P` in 5.0 Plus (893851). **Plain Move stays on `A`
  deliberately**: "regular move is never pressed, you just right click" (942336), "it's just thrown out
  of the way on the opposite side of the keyboard" (664561). People repeatedly read `A` and conclude
  their file is stale (435880, 034472).
- **Other v6 positions quoted in 2020-10, US QWERTY unless noted**: changeling `/`, hold position `'`
  (jaydik 449375, correcting Poletes 708830, who deferred 821880); Terran armory `/` then `'` (Brammel
  002641); Mutate Lair/Hive on the US key between backspace and enter, the backslash (Minty 804591;
  jaydik 327336); lift/land on backspace, which Pokebunny likes as a big index-finger key (005889);
  menu is no longer `F10` and can be put back (Pokebunny 189490). Depot raise/lower is K/P in 6.0 and
  J/`;` in 5.0 (634364); the spreadsheet says K = raise, P = lower (548648), and Mell00yell00 inverts it
  because "K is lower than P" physically (179124). **Superseded: lift and land on `]`** — Mell00yell00
  advocated it and then recanted (739580), because SCV halt is also on `]` and you sometimes need to
  hold lift while a building finishes in order to swap addons.
- **Build Basic is `k` and `p`** (818203, 319562). **Build worker: the spreadsheet only puts it on `p`
  for Zerg**; Terran and Protoss have it on `k`, so the opening is `o` then hold `k` (064603, 651723).
  Edennil runs `p` as build worker on all three races so `o` -> `p` always makes workers, or you can
  swap the Build Probe and Recall hotkeys (761748, 735083); he updated the FAQ for it (103121).
- **Morph binds stay consistent across siege / liberator / lurker; do not move them.** Swapping Thor
  with Hellbat/Hellion inside the factory is fine (915274, 496744). Upgrades are ordered
  easiest-to-press first, `F`, `S`, `R` (226250), F offensive and S defensive (101505).
- **Terran bio: alternate-bind marines to `K`** so a six-marine batch is `;k ;k ;k` rather than `;;;;;;`
  (824799, 044161, 297354); same idea for finding marines, moving the reactor off `K` and
  alternate-binding find-marines onto it so finding and producing alternate fingers (096842, 597059).

## Control groups, add versus add-steal, and the trash group

- **TheCore uses add+steal, not plain add**: "we add + steal … not regular add … add to control group and take away" (Edennil 556417, 946434, 441505). A spreadsheet showing plain add for groups 3 and 6 while the Core+ 5.0 file used `Shift+Alt+key` throughout was the sheet being stale (Samsonn 760000, 360285).
- **Shipped modifier semantics, v6: Ctrl = add-and-steal, Shift = create** (720394, 170836; yjzhou 000906 checking a fresh 6G download after expecting the opposite, 803998). This is swapped relative to stock SC2 (995476); JaKaTaK on rearranging: "Go for it, but keep control and add/steal on the same key" (919977). Edennil's simplification for newcomers (441277): "always use Control + Key when you want to add to a control group. And always use Shift + Key when you want to create a new control group (overwrite what was already there)" — the Control bind being Add and Steal, which pulls units out of their other groups (Poletes 739156, 208003; Sora 423131). Control group 1 is recalled with `J` and both `Ctrl+J` and `Shift+J` write to it: "99% of the time you should be using ctrl j, to add/steal" (jaydik 000192); "select mines that are in cg O and then hit shift+I, which will add them to cg I but will not remove them from the original cg" (Mell00yell00 908407). MatosMachine's order is ctrl first then shift — add and steal, then create a new group (307732, 239947) — and he uses add rather than create on shift (276264). Edennil's own scheme is Control = Add+Steal, Shift = Create+Steal, Control+Shift = Add (430283). The three editor action names to look for are recall, append, and create/steal (gcask 572583, Bitstorm 926158); when editing, pick `Append and Steal`, not `Append to Control Group` (848832, 784469), which is also the fix when a keyboard locale makes the normal add-modifier combination unreachable (058562, permalink 781623754513973318).
- The 6c recalls as shipped, posted by gcask (302659):

  ```
  ControlGroupRecall0=G
  ControlGroupRecall1=J
  ControlGroupRecall2=I
  ControlGroupRecall3=K
  ControlGroupRecall4=V
  ControlGroupRecall5=N
  ControlGroupRecall6=H
  ControlGroupRecall7=M
  ControlGroupRecall8=Control+Comma
  ControlGroupRecall9=B
  ```

  and the matching appends, posted by Bitstorm (303361):

  ```
  ControlGroupAppend1=Shift+Alt+J
  ControlGroupAppend2=Shift+Alt+I
  ControlGroupAppend3=Shift+Alt+K
  ControlGroupAppend4=Shift+Alt+V
  ControlGroupAppend5=Shift+Alt+N
  ControlGroupAppend6=Shift+Alt+H
  ControlGroupAppend7=Shift+Alt+M
  ControlGroupAppend8=Shift+Alt+Comma
  ControlGroupAppend9=Shift+Alt+B
  ControlGroupAppend0=Shift+Alt+G
  ```

- **Accessible control group keys are `J I O L H N M`**; `B` and `G` are the weak ones (Pokebunny 861835; Siaal 981251). JimKlide cannot find `N` or `G` reliably (768021, 224193); jaydik finds `G` easy (035850); Poletes uses `N` constantly and says curl your fingers rather than move the hand (406603, 461384). `,` sits on the ring finger, which also owns `I` and `K`, so anything there risks finger repetition (387240). **Only two assignments are strongly recommended: town hall on `o`, production on `i`** — the rest is preference (708443, 171857, 480961, 392381). Zerg concretely: hatchery `o`, inject queens `i`, inject `/` with `-` as alternate, creep queens `h` (303041, 854027, 290334, 712657, 776513); burrow research is `=` on US (020163). Production buildings all on `I` plus tab, split across groups, or a hybrid — no consensus (277515, 967528, 639198). Allocation is race-specific and JaKaTaK's own scheme lives in the spreadsheet (570462) with a screenshot at 625802. The sheet and the shipped file list the groups in different orders (`J-I-O-L-M-N-H-B-G-,` against `J-O-I-L-M-H-N-B-G-,`), functionally identical, reorder to taste (013939, 185307, 239602, 810620). **For a fourth Terran macro group, put two extra groups on `Shift+I` and `Shift+L`** — you lose add-without-steal on them, which macro groups can live without (MatosMachine 297054, 253313); Siaal warns `Shift+K` will cause problems (427916). MatosMachine's Shift trick: production and town-hall groups rarely need create, so `Shift`+production selects warp gates and `Shift`+town-hall selects a farther group (082709; Poletes "that's genius" 676402).
- **Add without steal is deliberately hard, and that is the most-asked-about design decision.** Add/steal covers about 99% of use (jaydik 294559); Add+Steal and Create are the two easy binds, Add and Create+Steal made hard on purpose (Altafen 187137). bananian objected that alt+shift+ctrl is "not ergonomic at all" (202134, 122876); Edennil: "The intent is for you to use add + take away," and if you dislike it, "just swap 'add to control group' for 'add + take away'" (403182, 260544). **Edennil's three methods for getting one unit into two groups, written into the FAQ on 2023-03-08** (986163, 558410): (1) select the group, Control+click the unwanted units in the wireframe, then Create Control Group (shift+key), which deliberately does not take units away; (2) replace the "Create + Take Away" combination with plain "Add to Control Group" — "When the setup was made, Create + Take Away was used more often. Practices and times have changed and it generally is not seeing a lot of use now. You likely can safely make this change without impacting your play"; (3) change one specific group's Control+key from add-and-steal to plain add. Bose found (2) most useful and asked for the Core+ caveat to be stripped, which Edennil did (295505, 915411, 098762); the same call — create-and-steal is "pretty much obsolete now", rebind that third modifier to plain add — is made at 527282, 347109, 372641. Earlier workarounds: rebind add to plain `Shift+letter`, which Mullsy confirmed working (876937, 092877); rebind the production hotkeys from add+steal to plain add (Poletes 935090); ctrl-click the building and use create, "control click fact, control (rax key), shift (fact key)" (Poletes 673843). **The vikings problem** — one unit in two groups — is solved by turning a couple of the ctrl add-steals into plain adds, at most about 2 of the 10 (Edennil 784563, 914207), or by reusing a production group so shift+o add-steals production while ctrl+o adds to the main army (Mell00yell00 583400). Switching your main production group to plain add is a legitimate personal edit if you do not want new buildings pulled out of other groups (Altafen 528206, 015141).
- **Control and shift are load-bearing because SC2 hard-codes them; alt is deliberately underused** (335690): "- default position makes it less accessible - even if you move it, control and shift both have unchangeable functionality in sc2 that we try to synergize with." Ctrl+shift is Create/Steal and "isn't used super often" (388264). Order matters: `alt+shift` centers while `shift+alt` does not, and both orders are used deliberately (Altafen 953012); Poletes hits the same wall on QMK, which "requires the keys to be pressed in a specific order to be alt+ctrl", so he routes center-on-selection through a mouse DPI button sending `F8` (738544). **"Synergy" here means picking placements so a whole sequence runs under one held modifier** (Edennil 396480): hold Control, hit the rally cam, click the new unit, hit the control group, release — one hold, four actions (000834). Adding to an existing group from the rally camera: box or ctrl-click, then Ctrl+`j`, holding Control the entire time (Edennil 226981, answering 072385). Per race (Edennil 059749): Zerg, `Ctrl+click` the eggs in the wireframe as you make units; Protoss, add gateway units as you warp them and park a rally cam where robo and starport units land.
- **Guard the destructive commands.** Heliac kept hitting Shift and Ctrl together and resetting his nexus group, so he moved Create to `Alt-Shift` and Create/Steal to `Control-Alt`, leaving Add and Add/Steal alone (768444, 928412); jaydik just pops the keycap off (790762).
- **The trash group is control group 10 on `,`, with add and select inverted: a bare `,` add/steals into it, `Ctrl+,` selects it.** It exists because SC2 has no "remove from control group" command, so you dump unwanted units there instead (946880, 251399, 659452, 740432, 267761, 051365, 515904, 402419; Siaal 114544, 631621, 440576, 687656). It arrived in 6.0; 5.0 lacks it but it is worth adding (898792, 309052), and 5.0 Plus puts select-CG9 on Ctrl+`,` (915732). In Core 5 the equivalent is CG9 with add and select swapped (766166, 558219), and JaKaTaK spelled it out: "Select CG9 should be Ctrl+, add/steal CG9 should be , … This is your remove from control group function" (663218, 880192). Regular Core only; Lite does not have it (598167, 123261, 687690). Without one, select the group, shift-click the unwanted units out and re-create it (007208); it converts back into a normal tenth group if you prefer (080986, 623168). Building one yourself: rebind a group's select key to create-steal or add-steal, which the customization doc calls "practically the same", except create-steal lets you put the most recently trashed units back without dragging every earlier batch along (jaydik 948419).
- **Add+steal or create+steal for the trash key is a live disagreement.** It ships as Add+Steal; Poletes and jaydik both changed theirs to Create+Steal — "I just checked, the hotkeys were set up to add/steal for `,`. I changed it to create/steal though" (438376), "trash is not supposed to be add steal, that defeats the point" (725806). JaKaTaK defended add — "add is like recycling bin, create is more like trash", "this way you never lose a unit you put in there" (987713, 134590) — then conceded "it seems like create has more utility" (154812). The confusion traces to Marre's customization doc for roughly 4.0+, which specified create (580575; JaKaTaK 831135). Symptom of add+steal: pulled workers accumulate and the group can no longer recall the latest batch (AvroArrow 441618; Poletes 545951), which is why AvroArrow prefers create+steal for drone pulls (689291). Mell00yell00's own variant is ctrl = add/steal, shift = add, with create/steal on control group 10 (980426, 109342, 441419); jaydik adopted it and confirms it works (588244).
- **What the trash key is for**: box a subset of your army and hit `,` once and they leave the main group in one press — runbys, ling/bane micro, scouting lings, pulling workers off a drop and sending them back with `Ctrl+,` (jaydik 951588, 388493; Poletes 360192). The point is the single press, not the removal (598382). Mell00yell00's uses (767381, 989285, 582319): "its just a trash bin," never cleared — "It will be overwritten as soon as you trash something else" (352272) — plus temporary harass groups, grabbing marines from the main army, stimming them at a side base and trashing them so the main army no longer recalls them (700822, 105448), and for a medivac drop, group marines and medivacs, load, shift-click the drop, trash, then "double click `,`" on arrival (871252). Scouts and run-bys go there too (159666). Poletes does not use it and finds it of little use for Protoss (062544).
- **Trash key instead of trash control group (2020-09).** Bind the inner thumb key next to space, usually Alt, as the trash *key* so `,` stays a plain recall: single-tap create, single-tap recall (Mell00yell00 838897; jaydik 730755). Constraints for that key: nothing used with or right after a modifier, and no double-taps, since double-tapping with the thumb "is as slow as shit" (053269, 238817). Implemented with AutoHotkey making the key output `z`, then binding `z` as create/steal for a high control group (346250, 664656). Field report, jaydik after 9 ladder games (2020-09-11): his thumb pulled in preemptively and built "a ton of queens I didn't want", but "it feels way more accurate to hit alt over ," and a recall-only `,` makes accidental trashing almost impossible; he kept it (033789). **JimKlide went the other way**: deleted the furthest control group and moved a real group onto the trash key, giving up the recall, because his trash uses — splitting banelings and lurkers, trashing larva, splitting overseers, pulling stray workers — never need one (343411), parking the displaced group on `G` as Mell00yell00 suggested (938296, 142082).
- **Zerg larva trashing: the sequence is `O ; ,`** — hatch, select larva, trash — run after every production cycle. JaKaTaK: "it is done after every production cycle. So i make hydras and press O;, That's part of the advantage, you can make it an automatic habit more easily because it's exactly the same" (064650), though he is not satisfied with it when you are also adding to the `L` group (351034, 302912, 504641). Step by step (jaydik 311565, 999547, 734788, 131082): with 10 larva, make 5 into lings, add all 10 eggs and larva to the army group, then reselect hatches, select larva, trash — "The same three keys every time, very easy to muscle memory". Faster than ctrl-clicking eggs because the last step never varies (022501), and mouse selection at speed drags in overlords and drones (ScaryMouse 934272). Risk: if the larva is already spent you trash the whole hatchery group, which "takes forever to re-cg" (383600) — the reason he keeps a recallable trash CG (094507). JuicyJuuce's variant is `O` then `P` then `,` after morphing, recovering a mis-trashed hatchery group with `control+,`, `control+click` the hatcheries, then `control+O` (822824, 104844, 039298, 544358). **Edennil dissents: control-click the eggs instead.** "select hatcheries -> larva -> trash after every time you add army units felt more effort than just control clicking," and it "led to more mistakes from times that you actually used all your larva and didn't have any" (252581, 707780); trash has a prominent key only because "Jakatak liked that method and wanted to make it easy to do" (249480). JuicyJuuce still prefers trash for "not having to aim the mouse" (038387).
- **Overlapping control groups are intentional.** Zerg: banes and lings on one key, banes alone on another, so you a-move everything then pull just the banes off tanks (Sora 739463). Terran: tanks inside the army group and on their own for quick siege (ScaryMouse 399336). Hatcheries and upgrade buildings deliberately share one group in v6 "so that building workers might remind you to check upgrades, and building upgrades might remind you to build workers" (Siaal 184346, jaydik 975602, 245599); you start upgrades by selecting that group and tabbing to the upgrade building without moving the camera (jaydik 495271). Burrow and unburrow get separate keys on non-lurker units because burrowed and unburrowed units share a tab group, so a split lets you handle a mixed selection in one press (Puddingkruste 220620, Mutaller 367334).
- **Select-all-army is not bound in v6.** jaydik does not rebind it and clicks the button above the minimap (548816); Siaal suggests `Ctrl+F8` or `Ctrl+BackSlash` (511787). **Warp In (select all warp gates) is also unbound**: "if you're not playing random, the select all warp gates hotkey is best, otherwise use a control group" (JaKaTaK 275720); it selects warp gates only, not un-transformed gateways (Sora 290130), and Trebhin's report that the bind was broken turned out to be the arcade unit tester map (772412). Warpgate placement is an open patch on top of 6.0 — Edennil's two options (973125): "1) Bind Shift + Back Mouse Button (Or Shift + Forward Mouse Button) to Warpgate  2) Bind Back Mouse Button to Warpgate (And use forward mouse button as next subgroup.)"; not in the shipped file (Eruci 061235, Edennil 933958), approved for 6 by JaKaTaK (838138).
- **Idle worker lives on `6` in v6** (jaydik 175232). Mell00yell00 moved it to space so he can hit it with his palm and moved cancel to `7` (722580, 766698, 961598); Siaal tried idle worker on `F8` with cancel on space and does not recommend it (218394).
- **Move and the rally commands are deliberately left off the layout**, because right-click sets both Zerg rallies depending on what you click (Poletes 606100, 344819, 181916, 055230). jaydik's heuristic: "if you see anything and go 'how the heck am I supposed to hit that', it usually means you aren't supposed to" (408100).

## Cameras

- **The design is seven base cameras plus one rally cam** (Edennil 003050). Base cams are created on
  Alt, which also centers the view on the current selection, so every base camera ends up framed the
  same way on its town hall and the mouse muscle memory carries between bases (787924, 150923,
  permalink 773650333352198164; JimKlide 141570; 472208). The eighth is the rally cam, deliberately
  *not* centered and therefore on Control, giving it synergy with grabbing rallied units (490334,
  000076, 781948, 382673; jaydik 130904, ScaryMouse 130240, Siaal 819694). Rally-cam uses vary by race
  — Protoss warp-in, Terran drop or add-on, Zerg creep or third (226116, 839461, 661377, 132339,
  645196, 365184); the one non-alt location hotkey was originally Terran-only (740416). In 5.0 the
  rally cams were `Ctrl+K` and `Ctrl+SemiColon` (794929). Alt does double duty — create camera and
  center-on-selection — which is why a Control+camera bind exists at all: the rally cam, because Alt
  is already taken (607627, 933849, 311134, 452825). Camera 8 sits on `Ctrl+0` / `Ctrl+9` rather
  than the Alt layer exactly so it can be dropped on arbitrary ground (387922, 948220, 064428, 924740;
  restated as jump-to-location 4 on `Ctrl+J` not `Alt+J`, 800573, 599746, 203979, 250580); ScaryMouse
  corrected Borg's assumption that camera 5 was the rally cam — 5, 6 and 7 are just further bases
  (017025, 114890, 102164). Camera keys run right to left, `0` is location 1 and `9` is location 2,
  "mostly just legacy"; change it if you want (Poletes 469569).
- **6g binds, exactly**: create on `Alt+0`, `9`, `8`, `U`, `P`, `O`, `I` and `Ctrl+0`; jump on `0`,
  `9`, `8`, `U`, plus `Shift+9`, `8`, `U`, plus `Ctrl+9` and `Ctrl+0` (423951, 797168, 534539).
  Cameras 1-4 are unmodified; 5-7 are cameras 2-4 plus an extra modifier, the seventh being `Alt+I` /
  `Shift+U` (Siaal 350036, 226188). `Ctrl+0` and `Ctrl+9` already exist in the v6 file (jaydik
  516147). Stated again as shipped: "Jump to Cams 1-4 are `0,9,8,u` / Jump to Cams 5-7 are `Shift` +
  `9,8,u` / Jump to Cam 8 is `Control` + `9`" (393408).
- **Camera creation is the single most-asked question in the channel** (McDeJay 209512, Borg 201130,
  itcat 305607), and the answer is always the same: **hold Alt down continuously, move the camera with
  a minimap click or drag, press the location key, and do all of them in one pass at game start
  without releasing Alt.** Holding Alt does not continuously re-center, so several cameras can be set
  in one hold (279115, 702505, 937950; ScaryMouse 498206, 204850; astra 551303; Sora 459112, 509099;
  SwordSmith 408734, 750249; TOMES 264852, 219275; 344991, 994114, 076204, resolving 074345; Edennil
  925791 gives the order `0`, `9`, `8`, `U`, `P`, `O`, `I`). Pressing Alt before moving the screen is
  the operative detail: "When you set the cam, press alt first, then move the screen to where you want
  the cam to be" (JaKaTaK 072532, 642518; Altafen 782145; TOMES 371706; JaKaTaK 222816; Altafen
  278933). MicroMacroMarco, 2023-03-04: "a common question. you hold down ALT while creating the
  second camera location" (867516, 794570). Full sequence for bases that do not exist yet: click the
  town hall, hold Alt, press the camera key, keep holding, click the minimap at the next base, press
  its key, repeat (Edennil 733130, FAQ 499594; Altafen 696479); Lite uses `Alt+Shift`, or `Shift+Alt`
  without the centering (Altafen 815985). Alternative from JimKlide: hold a click on the minimap while
  pressing the location hotkey, which suppresses the centering, dragging around the minimap to cycle
  them (950144, 005952); or lay them all off the main hatch and recreate each once its base is built
  (Sora 130142, 657108; recreating is the same hotkey with a command centre selected, 050369). You
  should not need to clear your selection first if you set them all in one go (ScaryMouse 231060). The
  newcomer trap is that Alt with a unit selected jumps the view to that unit (000038, 751308); click
  the minimap first, then press the camera key, Alt held throughout (340562, 676487; Altafen#6776
  429958). It is in the FAQ channel (456825, 164078). The cost of the design is that you cannot set
  all bases at game start and cannot set a camera on empty ground (217283); the intent is stated as
  "centre camera is put on the same key as create camera intentionally / the idea being you'll select
  your town hall and then centre on it before you create your camera hotkey" (064976, 439971). The
  workaround is the same alt-hold: hold Alt, hit `J` to put the town hall on control group 6, then set
  every base camera before releasing (671356, 187250, 359115, 890693, 153665, 000872).
- **Re-make each camera once the building exists and it re-centers itself.** After expanding, select
  the CC, add it to the macro group and remake the camera (Altafen 737920, 184513, 598656, 915083;
  099505). JuicyJuuce's variant: "as soon as a hatchery starts building, select it, then do alt+9...
  that makes sure that the camera is exactly centered on the hatchery, making quick queen injects as
  you go through your cameras cleaner" (228905). Mell00yell00 sets 1-5 at game start anyway as a
  warm-up ritual while agreeing it is unnecessary (389714). To re-set one: nothing selected, hold Alt
  and click the minimap, then set the camera; with something selected, click the unit or building
  first (011637, 763709). This answers the most repeated newcomer bug report, "all I do is jump back
  to my natural" (592380).
- **The opening sequence is mandatory** — skip it and an unset camera will steal units. JuicyJuuce
  reported `Ctrl+Shift+K` pulling queens into control group `K` (139925); JaKaTaK: "This is a part of
  all versions of TheCore. The opening sequence is mandatory because it ensures every camera is set to
  something" (694465). It is the same for every race, Zerg just adds the overlord step (447424,
  352276; permalink 773650629737971763), and the exact keys should not be quoted: "He shouldn't have
  put exact keys, because those change even within the same version... depending on your keyboard
  layout" (485535, 145321). The FAQ version is missing the alternate add-to-control-group press — "Add
  that as step 2.5" (676810, 227305); inject also has an alternate on `v` (904202), and the principle
  is "It should just be an alternate keybind, not the primary one" (948240, 745887).
- **If Alt-centering bothers you, rebind center-on-selection rather than the cameras** (ScaryMouse
  270784; 693524; 907362, 435008 — especially as Terran, where auto-repair yanks the camera away). A
  user who "fixed" a camera problem by disabling Center on Current Selection was warned he had given
  up the select-base-then-save-a-centered-camera flow (Bitstorm 406610, 741328). Without the Core+
  remap you can hand-roll it: gcask bound center-on-selection to `Shift+0,Shift+9,Shift+8,Shift+U`, so
  for the first four bases click the town hall, `Shift+0` to center, `Ctrl+Shift+0` to save (895233).
- **Jump-to-camera should be on no modifier or on Control, never Shift or Alt** (282113, 894216,
  913690). "Jump to location on shift forces you to either lift modifier or forces you into shift
  queue inject methods" (914068); "Jump to location on alt forces you to lift modifier" (121715). Two
  further constraints (251679): base cameras need a way of centering on selected, and "At least 1
  camera should have the option of being set without centering on selected. This is for a rally cam."
  Edennil prefers Control over Shift for cameras generally (599657) and moved 5-8 to `Control` +
  `0,9,8,u`, leaving 1-4 alone (821952); Mell00yell00 did the same (818158).
- **Edennil's replacement camera scheme, verbatim** (871573, restated 060718):

  ```
  Jump to Cam 1 - 0        Create Cam 1 - Alt + 0
  Jump to Cam 2 - 9        Create Cam 2 - Alt + 9
  Jump to Cam 3 - 8        Create Cam 3 - Alt + 8
  Jump to Cam 4 - U        Create Cam 4 - Alt + U
  Jump to Cam 5 - Ctrl + 0 Create Cam 5 - ALT + P, Shift + 0
  Jump to Cam 6 - Ctrl + 9 Create Cam 6 - ALT + O, Shift + 9
  Jump to Cam 7 - Ctrl + 8 Create Cam 7 - ALT + I, Shift + 8
  Jump to Cam 8 - Ctrl + U Create Cam 8 - Shift + U
  ```

  Rationale (810142, 175398, 043240): jump on Ctrl so a held modifier cannot shift-queue, and so you
  can jump, ctrl-click select-all and ctrl-add to a control group without lifting the thumb. Create
  5-7 either with Alt plus the key below the camera key — letting you hold Alt through `0 -> 9 -> 8 ->
  U -> P -> O -> I` — or with Shift plus the camera key, which does not center and so doubles as a
  rally cam. Camera 8 is settable without Alt for that reason (801208, 486840). As of 2023-03 this was
  the only change Edennil still recommended that was not already default in the newest v6 file (789716,
  359106, Izoughe 788708). **He calls the stock v6 camera binds the design's weakest point**: on
  `Alt + P` to create but `Shift + 9` to jump, "I don't think the intent landed very well",
  "ultimately, I think it fell short" (867996, 716561) — the intent was four keys covering eight
  cameras while keeping Alt as the base-centering create modifier. His three suggested v6 upgrades as
  of 2022-07 (608229): "1) Slightly lower priority on Trash Control Group. Swap Trash Control Group (on
  `,`) with something slightly further away (either `M` or `N`) 2) Change cameras 5-8 (only works for
  Core+) 3) [swap the command on `.` with the control group on `,`]." He also warns the spreadsheet's
  "suggested cameras" section is simply wrong (219772, 258463) and that any edits based on it should
  drop the Ctrl+Alt+Shift column (563742).
- **Shift on cameras collides with shift-queueing, and this is the most common rebind.** Holding
  `Shift+0` to queue a unit home can recall base 5; Siaal moved cameras 5-7 onto Control and left the
  Shift versions unbound (350602), at the cost of a new home for the rally cam and of preempting
  Control at the first four bases (430784). Mell00yell00's variant keeps set/recall for 1-4 and recalls
  5-7 on `ctl+0/9/8` (797727). MatosMachine instead dropped the Shift add/create variants on his
  production and town-hall groups and uses Shift there as set-rally-cam (111977). Siaal's same fix for
  Puddingkruste, who was losing Shift mid-inject: rebind 5-7 to `Ctrl+number` so Shift stays free
  through the first four injects (896590, 308218), adopted (069333, 046997). Shift is deliberately
  avoided for Zerg camera jumps so you are never forced into shift-queuing injects (675841, 908423);
  Phayil wanted `Shift+0/9/8` for extra cameras and Edennil allowed it for his playstyle (498304) but
  pointed him at the Lambo inject guide first (054436) and said that if he insists on shift-injecting
  he should move inject to `P` (587157, 872714). **`Shift+Y` is ruled out outright: it destroys queued
  patrol** (Harri 408785; jaydik "I shift patrol regularly, every game at least once" 967488; Edennil
  963486). `Ctrl+Y` would work but loses the warp-in synergy (618509). Related: in a shift-queued
  patrol chain, only the last patrol stays a patrol (Poletes 034440).
- **Putting everything on Shift for Protoss is the counter-argument, and it is unsettled.** Poletes:
  "if you are going to main protoss you make your cameras all on shift, cuz often you warp in
  defensively... you want that synergy with every camera" (591080); Siaal has 5-7 on Ctrl instead
  (448853); Harri's mockup puts bases 1-6 and the rally cam on Shift and duplicates 5-7 on
  `Ctrl+Shift`, at the cost of create/steal on control group 4 (030195). For a second Protoss
  rally/warp-in cam specifically, Siaal argues for a Shift key since you are already holding Shift for
  warp-ins (718258); options offered were `Ctrl+K`, `Ctrl+P`, `Ctrl+SemiColon`, or moving the seventh
  cam from `Alt+I` / `Shift+U` to `Ctrl+U` / `Shift+U` (436629, 470994, 226188). MicroMacroMarco landed
  on `Ctrl+8` / `Ctrl+U` for set and recall (929444) and kept both `Ctrl+U` and `Shift+U` as recall
  (721438).
- **In 6g the second-layer cameras are set with `Alt+P`/`O`/`I` but recalled on `Shift+9`/`8`/`U`**,
  and several people rebound recall to `Shift+0`/`9`/`8` so it sits under the set keys (JimKlide
  762442; NReilingh 457721; Mell00yell00 431444). NReilingh's guess at the shipped choice: not wanting
  three cameras on `0`, which also carries the rally cam (457721).
- **`Alt+Control+key` is not a Core 6 combination** — it is a leftover from Core 5.0+, where you
  physically pressed shift and control (369984, 831646). On UK qwerty, Alt Gr sends ctrl+alt as far as
  SC2 is concerned, so a camera bind can look like it needs two modifiers when it does not (ScaryMouse
  778462, 476463; Wolta Horo 055488, who found alt alone sufficed). A file from the wrong keyboard
  region silently breaks camera keys: SieStein's v5 cameras would not save or recall, the cause being
  the file not matching his layout rather than a bug (937503, 341696, 819047) — he runs a Croatian
  layout on a Danish keyboard (375421).
- **The Core 5 camera block, for anyone still on 5 or rebuilding a broken file** (Siaal 162826):

  ```
  CameraSave0=Alt+P            CameraView0=Control+Shift+P
  CameraSave1=Alt+O            CameraView1=Control+Shift+O
  CameraSave2=Alt+I            CameraView2=Control+Shift+I
  CameraSave3=Control+P        CameraView3=Control+J
  CameraSave4=Alt+SemiColon    CameraView4=Control+Shift+SemiColon
  CameraSave5=Alt+L            CameraView5=Control+Shift+L
  CameraSave6=Alt+K            CameraView6=Control+Shift+K
  CameraSave7=Alt+9            CameraView7=Control+Shift+9
  ```

## Rapid fire and the non-rapid-fire spell keys

- **`J` is deliberately not on rapid fire**, so there is a non-rapid-fire option for storms,
  forcefields, fungals and biles (Siaal 318539, 735765). Corrosive bile has an alternate that *is*
  rapid-fired — `;` in v5 — so you get both (Siaal 379966, 782484). ScaryMouse reads the same off the
  sheet: bile on `K` and `P`, "one option without rapid fire and one with" (623136).
- **As of 2020-05-05, `K` is the only non-rapid-fire spell key.** A second would have to be `-`, since
  `'` is hold position and stop cannot be taken, unless you cut into rapid-fire warp-ins (Poletes
  105674; JaKaTaK 900948, 596881, 926132). JaKaTaK acknowledged the case for a non-rapid-fire feedback
  and left it open (004042).
- **Rapid fire is a scarce resource.** Poletes has only two rapid-fire keys; recall and chrono cannot
  be rapid-fire, and load/unload constrains where the planetary-fortress worker goes (875763, 799752).
  His advice for Terran and Protoss is to make unload rapid-fire and `/` not, moving unload to `[`
  (889647, 642149, 320583); not worth it for Zerg (363059).
- **Rapid fire is already configured in the shipped files** (Poletes 043385), and `K` is supposed to
  be the one non-rapid-fire key so that spells and warp-ins on `K` do not repeat. AvroArrow checked
  his file and found it was not (Poletes 600627; AvroArrow 509106). Symptom: `K` firing twice and
  building a pylon instead of a cybernetics core (632031), blamed on his 150 ms key-repeat delay
  (839026).
- **Rapid-fire key preference order is `P` first, then `[`, `-`, `/` in whatever order suits you.** `P`
  is preferred for comfort; the rest are "pretty controversial" and Siaal is not sure what the default
  priority was (314369, 930197, 043029).
- **Larva's alternates are load-bearing, so do not reclaim them.** `;` selects larva *and* builds a
  zergling in one rapid-fire press, so hatch group then `;` pumps lings with no select step; queen is
  on `'` (jaydik 497350, 511105). SuperSquare wanted `;` for queen and was talked out of it (459284).
- **Ravager bile is on `P` for rapid fire** — "one of the best uses for rapidfire imo" (jaydik 952558).
  5.0 also had bile on an alternate, so bind it to `P` and `K` and "hit k 3x per tank to break siege
  lines instead of trying to time out the holding for 3 biles" (409749, 729118).
- **Liberator siege wants rapid fire; tank siege does not** — the liberator's is targeted and fires one
  at a time (Edennil 614954). Mell00yell00 moved liberator siege to `K` for consistency with the other
  Terran transforms, lost rapid fire, and added `[` as an alternate for siege mode to get it back
  (171594, 800405).
- **Put overlord speed where rapid fire cannot reach it**, so holding the key cannot mass-produce
  overlords (Siaal 831306).
- **Prefer left click for placing buildings — avoid keystroke repetition where possible** (SwordSmith
  965663; ScaryMouse 146206).
- **Mules do not need rapid fire** (935967, 058026), but you can add the mule key to the rapid-fire
  line in the text file if you want it (Mell00yell00 468103); TitaniumPilgrim says they already are in
  v6 (984833).

## Abilities the shipped files leave unbound, and known errata

- **Anything Blizzard adds after a release ships unbound; bind it yourself.** JaKaTaK on the nexus
  ability in an upcoming patch: "unlikely" that it would be added (AvroArrow 957908, JaKaTaK 439545,
  Poletes "na just add yourself" 718018). The named post-6.0 cases are Battery Overcharge, Research
  Tectonic Destabilizers (himaji 484352, ScaryMouse 711131, Edennil 398795; Mell00yell00 264788;
  ScaryMouse 986187, 701652), Stasis Ward, the medivac speed upgrade, the big EMP, and arm/call nuke
  (414022, 751720, 581268, 934987, 949928, 781984); the canonical how-to is the message at permalink
  904420673760395274 (813568, 670612). **`[` is the community's default dumping ground** (Stefan
  515550; 871754, 951672, 677150; jaydik 379324, 222356, 649011; ScaryMouse 633034; Edennil 930226,
  751059, 771976). Two better-reasoned placement rules compete with it: ScaryMouse picks whichever of
  `k`, `;` or `/` has no nexus ability on it (668948); Edennil says **bind by association, not by
  hunting for a free key** — mag field on the cyclone key, medivac speed on the medivac button, the EMP
  upgrade on the EMP button (516116, 445854), and Altafen notes "people stick it on `[`" but says check
  for conflicts first (922379, 692702). The formal procedure: open the version's spreadsheet, find the
  unit on the "Buildings Units Spells" tab, and take the leftmost free key in the lowest available Zone
  (Zone 1 > 2 > 3 > 4; lower zone means closer to the home row), moving things to taste within a zone
  (Edennil 623037, 940689, 965928).
- **Battery Overcharge, the worked example.** Reworked and bound for the first time in June 2020, with
  no mechanical constraint on placement. Choices in use were `-` (Mutaller 969020), `[` (Siaal 171251,
  who found `;` "too comfortable" for it, 790992, and whom Mell00yell00 backed because "matches repair
  for terran", 741854), `;` (jaydik 271091), and `;` in the v5 US QWERTY file (Siaal 827924, 017300).
  Through 2020-06-13 Poletes held that a double-castable spell needs a non-rapid-fire key, "so put it
  on '" (307520); ScaryMouse pointed out the 60-second global cooldown removes the double-cast risk
  (811625, 279313, 544981) and Poletes withdrew the constraint on 2020-06-14 (850396). It still had no
  official 6.0 binding as of 2020-09-27, with no updated file in existence (TTarps 084714), and the
  original v6 US QWERTY leaves it and tectonic destabilizers unbound — reported five times (452619,
  026782, 305630, 442522, 829275) — with the Juuce file as the fix, though an older Juuce build also
  missed the Protoss build-basic alternate (407178, 649227).
- **Known errors in the shipped 6.0 files**, surfaced June-July 2020: `load` (Prism, Medivac, Overlord,
  Nydus), evolve burrow and summon adept hallucination are unbound (Stefan 074193, Poletes 953226),
  with the spreadsheet saying `load` should be `.`, which is also the stop key (Hoplite 084306); Sentry
  Hallucinate is missing its `/` alternate (Edennil 729296, Poletes 807455, JaKaTaK 072572); Cyclone
  lock-on is missing `P` in the download but present in the spreadsheet (NReilingh 720272, 283591);
  lift/land came out on Backspace instead of `]` (Sam Pound 372837, JaKaTaK 766422); Terran "Select
  Builder" is on `C`, which jaydik called ugly and suggested might belong on `=`, though Hoplite judged
  the hotkey useless enough that `C` is fine (307616, 467458, 025876, 579488).
- **Missing from the v6 betas, left for players to add by hand**: Terran SCV build ("should have benn o
  and ;") and Advanced Ballistics in 6b (Such 175936; JaKaTaK 490014);
  `Summon2ScoutHallucinations/Sentry` (wolfsha 885504); the build-basic alternate on `K` and some spell
  alternates added only after 6f shipped, so they lived in the beta channel and not in the released
  file (Siaal 932800, Altafen 132490); Zerg upgrades such as adrenal glands in 6f (Siaal 637908). If a
  v6 upgrade such as research advanced ballistics is unbound, check you are on 6g and not 6b (683136),
  and download from the Drive folder rather than the `old/` subfolder: TheCore -> 3. Download TheCore
  -> TheCore 6.0 Multiplayer Only -> pick your keyboard (Edennil 519550, 210907, 793741).
- **v5 is no longer updated, so anything Blizzard added recently is unbound there** — lurker upgrades
  and microbial shroud were named (Sora 345600, Siaal 803359). **v5.0 US QWERTY Right also ships with
  control group 9 broken**: `,` is bound to add/steal CG9 and select-CG9 is unbound because the file
  reads the invalid line `ControlGroupRecall9=Control+sC` (NReilingh 425483, 367336; thecynic 588706).
  Siaal treats it as known and asks new v5 users to check (445043); Sora patched it by hand (343751);
  the cause was a last-minute add/steal-versus-recall swap and the fix is to bind `Control+Comma`
  yourself (Siaal 149086, 923295, 277565).
- **Where file and spreadsheet disagree, trust the file** — read it, or look the command up in the
  in-game hotkey menu (Coyotebd 947572, 705492; Sora 834013). Known mismatches: the 6g sheet lists
  Command 2 on `I` when it should be `K` (enterprises 857730); uproot spine/spore shows `;` but is `-`
  in the 5.0plus file (JimKlide 296522, 264617); the building priority chart shows an alternate for
  `/k` that does not exist, probably a typo (Coyotebd 996738, jaydik 414982); a v5.0 Right Plus
  download briefly contained left-handed keys (Coyotebd 885240); create-camera-8 and jump-to-camera-8
  are swapped between the v6 spreadsheet and the file (AvroArrow 186418; Poletes 494933); the
  spreadsheet suggests `Ctrl+9`, `Ctrl+8`, `Ctrl+U` for cameras five through seven while the table
  beside it puts jump-to-cam 7-9 on shift (carlitos_mit_Auto 278170, no reply); and the
  letter-to-number control-group mapping differs between the v6 spreadsheet (`I` = group 4) and
  MicroMacroMarco's co-op pack (`I` = group 2) (Onikoroshi 660587) — the answer there being that the
  numbers do not matter, only the letters (Mell00yell00 214761; jaydik 478401). **The 6.0 spreadsheet's
  top section is authoritative; the per-race sections at the bottom are stale**, because JaKaTaK
  designs in clumps that affect all three races, so changes landed in the top section and did not all
  propagate down (jaydik 484132, 080977, 818563, 357922, 003420). **The "core considerations" doc is
  stale** where it says one key should serve both burrow and unburrow: 6g uses two, as did v5, because
  burrow overlaps with cloak and is a good infestor button (JimKlide 972540; Siaal 242590).
- **The 2020-08-21 patch added `Spray` plus `LoadOutSpray@1..14` and unbound `BurrowUp`.** pinion's
  edited block (542170):

  ```
  BurrowUp=SemiColon
  Spray=Period
  LoadOutSpray=
  LoadOutSpray@1=
  ```

  through `LoadOutSpray@14=`. The fix is to bind every new spray entry to a key you will never press
  (Edennil 581313); jaydik used `` ` `` and `1` (400982). `F13`, `F14` and up work as SC2 hotkeys and
  are unreachable on a normal board, Edennil's preferred dumping ground (191702, 384532); on a
  tenkeyless, numpad binds are "completely inaccessible" (jaydik 740241). Heliac's cleanest version
  (2020-08-23): keep the spray menu on `\` as 6g has it, then `Insert`, `Delete`, `Ctrl + Numpad 0-9`,
  `Numpad /`, `Numpad *` — exactly 14 keys, no conflicts (652434); if Blizzard ever enables sprays 2-13,
  move "Use Item Slot" to `Ctrl+NumpadX` and put sprays on plain `NumpadX` (526979). Mell00yell00's
  variant: menu on `\`, sprays on `1 2 3 4 5 q w e r t a s d f`, conflicts pushed to `z x c v` (201972).
- **"Banished" functions sit on `Ctrl+Shift+Alt+key`** so the game shows nothing unbound while the
  combination is never physically pressed (711219, 381629, 523813, 346635); rally point is handled the
  same way (442827). Edennil dissents on select-all-army being banished — bind it somewhere non-prime,
  such as `7` (unused in 5.0) or an unused control group, citing the HeroMarine video (496650, 419934,
  230794); TOMES counters that "there's always the button" (558528). It has no accessible default
  otherwise; spacebar, `F9` or a spare control group are the suggestions (345994, 960970, 644989).
- **Rally is deliberately unreachable — use the mouse.** Right-click a mineral patch or gas on a
  hatchery for the worker rally, right-click anywhere else for the unit rally (687937, 335776, 032474,
  088166, 835975, 597120, 167861); rally sits on `z` only because TheCore does not use it. Bose's
  general rule: "If it's on the other side of the keyboard, you should understand it as 'most likely
  you shouldn't bother'" (830593). Deselect one unit from a selection with Shift+left-click, on screen
  or in the console (902052). There is no surrender keybind either — Menu -> Surrender, or Rewind
  (195870).
- **Next/previous subgroup lives on mouse buttons MB4/MB5, not on the keyboard**, and is missing from
  the spreadsheet entirely (334421, 919070, 999730). With no side buttons, move Patrol off `Y` and put
  next-subgroup there (130569).
- **Ping is not `Alt+LMB` (Alt is center camera) and not `Ctrl+LMB`** — Ctrl collides with the rally
  cam drag and with adding to a group then commanding (Edennil 238702, 473233). Rough consensus is
  `Ctrl+Shift`+click (Edennil 057438; Poletes 209543); Mell00yell00 uses the forward side mouse button
  (190926). **Map ping lives under Unit Management in the in-game editor, not Global -> UI** (AvroArrow
  587340; Poletes 948041), suggested on `F7` or `Ctrl+Shift` plus something (932786). **`F10` moved to
  `F3` in the file for no documented reason** — Poletes guesses misclick avoidance (091718, 443698);
  safe to change if nothing else is overwritten (156161). **`F2` is left unbound** by jaydik and
  Mell00yell00, with cancel-building floated as a future use (825178).
- **Burrow splits on whether the unit needs the upgrade**: "for every unit who can burrow without
  researching burrow, it's on K/P, but for all other units it's `[` `]`" (jaydik 173596). Spine and
  spore root/uproot are `K` and `P`, distinct from burrow (Zandak 880531). **Speed upgrades live on
  `;`** as a rule (jaydik 314049), which is why Heliac's proposal to move observer speed to `P` was
  declined, though jaydik allows that banshee speed and raven energy look backwards (019206, 043787).
  Ultras on backspace is the one bind everyone agrees is too far when the index rests on `;` (079956,
  928906). Open bug (2024): robo -> disruptor is on `k` with no alternate, breaking the `i`/`k` finger
  rule; Edennil guessed it should be `[` and said he would investigate (800960, 836116). Stasis Ward on
  `'` collides with Hold Position (ketchupfriend 492461).

## Personal edits people made, and why

- Lair/hive morph moved to `'` with select-larvae on `;`, because `;` morphs both the hatchery and an
  overlord, so with no larva left you morph your hatchery by accident (JimKlide 449887, 324836;
  Edennil did the same in 5.0, 093935).
- Viper moved to `\` because `=` mispresses produced vipers instead of corruptors (Mutaller 362832);
  TOMES has the mirror problem, `=` for backspace giving overlord speed instead of lair (714610).
- Left alt remapped to emit `z`, used as create-steal / trash (Mell00yell00 513533).
- Town halls moved to `I` and the command key `K` to `O` so a Zerg never leaves reach of the cameras;
  Siaal calls it a lot of work, traded against building units off `L` (767977).
- Create, add-steal and create-steal added by hand to every v5 control group that did not collide with
  a camera key (314179).
- Charge unbound entirely so alt-clicking can never disable it (Poletes 980809).
- streetplay's custom layering, verbatim (690344): "I had already switched add to O as alt + - as I
  found that easier than alt+J. And from there I layered two more control groups on shift + O and
  shift+I. And set add to I as ctrl + . and ctrl + [ and ctrl +] as add to the layered keys. And I
  keep my scout (overseer) on shift+I and creep queens on shift +O, since I found that in general I'm
  holding shift for the next command for these anyway".
- **Poletes' undocumented v6 optimizations**, posted verbatim in-channel because they never reached
  the docs (024499):
  1. Implemented rebinds noted in comments.
  2. Bound warpgates to `Shift+back mouse button` — no functionality change, just nice to have.
  3. Created an alternate rally cam jump on `Shift+0` so that warping in is correct.
  4. Changed `/` to be non rapid fire for chronoboost since it should not be; added an alternate
     inject bind on rapid-fire `-` and rapid-fire supply drop on minus as well; put adept and glaives
     on `-` to be on rapid fire.
  5. Battery overcharge gets `[`.
  6. Caustic spray gets `-` instead of `/`.
  7. Added an alternate to parasitic bomb of `-`.
- **Freeing a thumb key (2020-10).** Mell00yell00 pulled the Windows keycap and used AutoHotkey
  `RWin::Tab`, with Tab bound in game to "last event", putting it under his thumb's home position
  (429224, 455339); bro cannot do the same because his equivalent is an FN key handled in firmware
  (739489). Related keycap tricks: pull the key below `/` so the thumb finds it (719272), and pull `6`
  and put a contrasting artisan cap on `7` so cancel stands out (966356). The key left of the pulled
  key becomes a trash hotkey (271666).
- marin unbound `K` entirely because the ring-finger reach felt unnatural, moving primary spell to
  `P`, secondary to `/`, third to `-` (696990, 785153).
- Protoss tweak from majinmojo (2024-08): **move Research Gravitic Drive from `K` to `/`** so every
  Robotics Bay upgrade sits on the key that builds the unit it affects — `P` for observer speed also
  builds observers, `;` researches thermal lance and also builds colossus (691102, 901798, 649520).

## Moving modifiers outside SC2

- **What Ctrl, Shift and Alt do is hardcoded by Blizzard and cannot be changed in the hotkey file.**
  Shift-queue and Ctrl-select-all-of-type are not SC2 hotkeys at all — Siaal: "it's less that it's
  'better' and more that it's 'literally only possible'" (601172); "you can't rebind things such as
  ctrl click or shift to queue things" or "alt to toggle auto cast" (333706, 046360); Poletes: "you
  can't do that in this game, control only has certain functions", and you cannot make shift+click
  select all units on screen (054506, answering AvroArrow 394701). Stated again at 997340, 043911,
  336168, 748265, and by Edennil and Altafen (147978, 377120). The only route is changing what the
  keyboard sends — keyboard firmware, AutoHotkey, SharpKeys or the Windows registry (jaydik 839958;
  027665); "rebind" here means changing what the keyboard sends, not editing a hotkey line (SwordSmith
  560870). That constraint is also why TheCore arranged the control-group modifiers to synergize with
  the hardcoded ones. On macOS, Karabiner does the remapping (Bose 456193). Keyboard macros violate
  SC2's terms of service; AutoHotkey modifier remapping is the legal limit (466599, 428574).
- **The Core+ remap, spelled out**: physical Shift becomes Control, physical Control becomes Alt,
  physical List/Menu (left of control) becomes Shift (Edennil 154079, Altafen 377120; jaydik 888596;
  Siaal 394966 verbatim "in an ideal world everyone uses the core plus bindings where / shift is bound
  to control / list is bound to shift / control is bound to alt"; 650946). jaydik strongly recommends
  it "if its an option" (646531) but prefers mapping Alt to Shift over using the list key (211187),
  and rates Fn as Shift "far better, highly recommend" (493953); binding list to alt also works
  (474307), and List->Shift is the step people vary on (805548). Using the physical alt key as alt is
  "the least comfortable of the three" (497457). Minimal version: just make List/Menu into Alt — "a
  modification I definitely recommend" (689354). Edennil's rule is that there is no right answer,
  priority **Control > Shift > Alt** (848208). Some vendor software will not remap those keys
  (837177). Scope a remap to SC2 only with AutoHotkey if you do not want it system-wide (Siaal
  170099); Siaal himself used keyboard driver software for the list key (614683).
- **v6 never asks you to press `Alt+Ctrl` or `Alt+Shift` together** (Siaal 490189), which is why
  Hoplite's keyboard with the Windows and Fn keys physically removed is still fine (629308, 621527).
  **Anything in the "Global" section of the hotkey menu can be layered under a modifier** (Siaal
  034513; Mell00yell00 "u can layer and layer and layer" 711765) — the mechanism behind the
  camera-on-a-modifier schemes.
- **Do the race-independent work in keyboard firmware.** Poletes on QMK: a camera layer where the
  warp-in keys send with Shift, one key sends with Alt, cameras are single keys and ability keys are
  `Shift`+key — "Took me like 10 min to do in qmk" (988010, 974912); he rates standard the closest
  thing to race independence "without something like qmk" (303427). His modifier layer (2020-10) binds
  Alt as `MO` to layer 4, so Alt technically does not exist as a modifier: on that layer `alt+o` emits
  a plain `o` (his inject key), alt+anything-else emits an unused key such as `f24`, and `alt+L` alone
  passes through as a real `alt+L` for auto-repair, turning off charge and turning off battery heal
  (107752, 738480, 887711, 238165). SwordSmith suggested the inverse, disabling alt except for the
  specific cases (834730); Poletes says the setup is "in line with bliz tos" (770054).
- **Heliac's SharpKeys + AHK setup** (629996, 088900): physically swap the right Ctrl, Alt and Menu
  keycaps (all one size) so Menu sits in the old Alt spot, Ctrl in old Menu and Alt in old Ctrl;
  SharpKeys permanently swaps L-Alt/R-Alt and R-Ctrl/R-Shift; AHK swaps Right-Control and Right-Shift
  only, its toggle on Scroll Lock so the LED shows whether it is live.
- **Do not remap onto AltGr: AltGr is ctrl+alt on most layouts** and fires center-on-selected when you
  wanted only alt; map to left Alt instead (Edennil 826709, diagnosing himaji 414376). ScaryMouse's
  counterpoint: if your board has AltGr, your locale's file should already use it as the alt key, so no
  remap is needed (074624).
- **The Fn key cannot be remapped by AutoHotkey, only in keyboard firmware** (Edennil 544202), and SC2
  does not see Fn at all (David Adam Monroe 153930). Superseded: Edennil's 5.0-era trick of an Fn key
  next to control, so Fn+key produced F1-F25, replacing every alt+key and giving a holdable inject on
  Fn+J (386024); he marks it obsolete — "6.0 fixed the issues with alt + keys, so it isn't an
  advantage" (462619).
- **SC2 does not distinguish left from right ctrl/shift/alt** (937280, 403247, MatosMachine 895808,
  Izoughe 666621). One user did hit a Ctrl+left-click asymmetry that swapping the keys fixed (774464,
  221440).

## Non-US keyboard layouts

- **Converting by hand: check for unbound keys after you swap.** Siaal posted untested hand-converted
  Spanish (736856, 512640), German (987486, 866180) and one further file (707368), each with the same
  instruction — "tell me if there are any strange keys or literally anything unbound".
- **UK QWERTY: everything on `\` moves to `#`.** ScaryMouse walked maxisq through it; evolve burrow
  and load SCVs both land on `#` (616104, 024882, 924793, 261066, 911648, 257050). The position
  matters, not the character: "this is for US qwerty, other keyboards have different layouts so you'd
  need to switch it for whatever key is in that position on yours" (077096).
- **UK layout was broken and is now fixed.** The US file's `BackSlash` binds came out as `Enter` in
  the UK file, and SC2 silently unbinds all of them because chat is on Enter (Fang Xianfu 609214). The
  cause is that UK key names are inverted relative to what you would guess: the `'@` key right of
  semicolon is called `Grave`, and the `#~` key next to Enter is called `Apostrophe`. The working fix
  is a straight swap — everything on `Apostrophe` moves to `Grave`, everything on `BackSlash` moves to
  `Apostrophe` (Siaal 875881). Blamed on the converter (441444). A later apparent relapse turned out
  not to be the file at all but a hidden US layout still installed in the Windows registry (026823).
- **Scandinavian and Swiss right-hand variants were still broken as of 2020-07**: the converter emits
  a plain US QWERTY file for them, while the left-hand variants and the Colemak/Dvorak outputs are
  fine (Poletes 417493, 851968, 145266, 595250). That bug is what blocked the seed-file update
  (837945).
- **Unresolved German-locale bug**: the in-game `ö` key reads as `Attack=SemiColon` on Kubuntu but
  `Attack=Grave` on Windows (929768, 419409, 130546).
- **Non-US layouts translate through the OS and can go wrong.** The file stores key names — "It's
  funny, because the hotkeys file just has 'Slash'" (Syfogidas 269104) — and with a Hungarian layout
  active it landed on `ü` (967680, 613992); SC2 "updates the helper hotkey text on the buttons ingame
  if you switch layouts" (426917). Syfogidas also suspects a bug in the UK v6 file: EngineeringBay/Scv
  sits on `Grave` in UK but `Apostrophe` in US, positions that do not correspond (997634, 310564).
  Bore's Swedish case: switching layout moved Spray, but Backslash's only other use is an alternate for
  Load, so the impact is minor (825867, 746866). **Download the file matching your keyboard layout, not
  your keyboard size** (424818).
- **Try plain US QWERTY first.** Some European boards send US scancodes underneath (561792), and the
  Brazilian ABNT2 case resolved to exactly that (860874).
- **Turkish QWERTY:** no file fit, so Juuce built one from key rows Tekabe posted (183690); Turkish has
  both `İ`/`i` and `I`/`ı` (225572). **Italian:** none exists; Federichech ran the Portuguese file fine
  (077676). General procedure (578196): take the nearest keyboard's version, map the differences,
  rewrite only those keys. **French AZERTY** exists; the finger diagrams are drawn on QWERTY but the
  physical positions are identical (265290, 411280).
- **Non-US files are generated from the US file by a conversion script, one `.ini` block per layout.**
  Turkish (JuicyJuuce 440706), whose comment explains why the special letters need no remap:

```ini
# it turns out the special turkish letters on turkish keyboards don't send those letters to the
# OS but instead send the US Qwerty key for that position, so we don't need to remap those keys
[Turkey]
AltGr=0
Minus=OEM8
Equals=Minus
BackSlash=Comma
Comma=Slash
Period=BackSlash
Slash=Period
```

  UK QWERTY (505310), posted while chasing the bug below; he suspects `BackSlash=Enter` is the gotcha:

```ini
[UK Qwerty]
AltGr=1
Grave=OEM8
BackSlash=Enter
Apostrophe=Grave
Enter=Apostrophe
```

- **Open bug (2024-07): `TheCore6g_Juuce_1.2.2_right_UK_Qwerty` leaves Evolve Burrow, Spray and
  Hallucinate Adepts unbound**, reproduced from a fresh copy (503358, 506582). The US file binds all
  three; Evolve Burrow uses `\`, which is `#` on a UK board (964275). JuicyJuuce thinks the file was
  generated against a different UK physical layout, and asked for a keyboard photo and the amended
  keyset (591752, 505537, 285339, 674782). No fix shipped in this chunk.
- **Debugging a foreign-layout file by hand**: compare key by key against the US QWERTY file, and
  rebind through the in-game editor to learn what StarCraft calls the key, "because sometimes what
  starcraft calls the key is different than what it is actually called" (142216, 662808, 365845,
  148121). Uploading the US file to the visualizer helps you see positions (470814). The scalable fix
  is adding your layout to TheCoreConverter (418431).
- The UK QWERTY gap was still open in the 2024-08+ chunk: bind Evolve Burrow, Spray and Hallucinate
  Adepts to `#` (564567), though ScaryMouse prefers `[` for Evolve Burrow (578836).

## Game settings and modes that interact with the file

- **Switch to Default or Grid before launching arcade** — the cleanest way to stop SC2 rewriting or
  merging your profile (056320). Coop, campaign and arcade all do it, and people in early 2020 lost
  or corrupted binds that way (530665, 750404, 222922).
- **The hotkey editor showing an unfamiliar command set is not a broken file.** Arcade and campaign
  games create Protoss/Terran/Zerg Story hotkey sets and the editor displays the set for whatever
  mode you played last; entering a multiplayer game or an empty custom restores the normal view
  (769748, 163328, 985865).
- **Version 6 is not co-op or campaign compatible**, and players swap to standard hotkeys for those
  and for custom games (613770, 269315, 638585).
- **Don't practise creep spread in "Don't touch creep or die"** — that arcade map uses the Heart of
  the Swarm inject at 40 seconds; spread creep in an empty custom game instead (401094, 370927).
- **Turn off Smart Camera Pan**, at the bottom of Mouse and Keyboard, or alt-centering in the opening
  sequence feels delayed — "that setting is stupid, it shouldn't exist" (Poletes 612295; AvroArrow
  confirmed 628965).
- **Turn off Simple Command Card** (Options -> Interface) so the card shows real hotkeys and
  stop/hold/patrol appear; also enable clicking on enemy units and set flyer helper to Always (Siaal
  137984, 411389; Trebhin confirmed 088552).
- **Uncheck the "go to latest announcement" option in game settings** so a stray click does not
  teleport your camera (643689, 280774).
- **Uncheck "smart camera pan" or camera jumps drag instead of snapping.** Undocumented and effectively
  mandatory (Bose 868806, 958932, 582986).

## Co-op and campaign files

- **v6 cannot be made consistently campaign- and co-op-compatible, and the reason is structural.**
  Burrow and cloak share a key in TheCore, but campaign and co-op turn that into a conflict, so you
  must sacrifice efficiency — and you must make that call many times over, which is what destroys
  consistency (MatosMachine 814880; SwordSmith calls this the FAQ answer, 556492). The recurring case
  is Stukov's Infested Banshee, which has both cloak and burrow, so with those commands shared across
  units both cannot sit on `[`/`]` (ScaryMouse 312410, Edennil 501716, 005850; Siaal 568090; 949204,
  222663; MatosMachine 162334, who adds "Co-op has so many conflicts that it can be good to create a
  separate layout per commander" 610526; JuicyJuuce first read it as an SC2 bug, 754064). Fixes are a
  second hotkey profile, per-session rebinds, or alternates — `V` and `F` in JuicyJuuce's file
  (486814). Edennil runs one file for multiplayer, campaign and every commander except Stukov, plus a
  Stukov file (887646); Mell00yell00 keeps 2nd and 3rd files, "to swap to a dif layout takes less than
  2 seconds" (832453, 059777). **Campaigns conflict with other campaigns, not with TheCore**, so one
  file per campaign and per co-op commander is fine (Siaal 723861; Mell00yell00 414096); per Siaal,
  co-op, the WoL/HotS/LotV campaigns, arcade and custom campaigns are each a separate hotkey mode
  (698817).
- **There is no official 6.0 co-op set.** Applying 6.0 leaves campaign and co-op commands unbound,
  showing as blank hotkeys in the editor (Onikoroshi 564550); Edennil confirms nobody has made one
  (639309). His per-commander recipe (588127): "1) Look at spreadsheet and see the abilities are on:
  `; K P / [ ' . - ] = Y`. 2) Open up a co-op game. Then quit. (Just to get the in-game editor to show
  co-op.) 3) For every command card unique to that hero I literally just add new abilities in the
  order I found in step 1." It works for about 90% and breaks on commanders with both cloak and
  burrow. The co-op maps are also in arcade under the `[MM]` tag, which skips the start-and-quit step
  (035787). MicroMacroMarco built an unofficial co-op/campaign version of 6g — Terran on 2020-05-25
  (634218), all races on 2020-05-26 (596365) — "all I can really do without changing the original"
  (463630), unoptimized because he does not play co-op (664213). Still unbound after his pass:
  Hercules "Load", Raynor on Char "Penetrator Round", Tech Reactor on Barracks "Research Nitro Packs",
  Tech Reactor on Starport "Research Corvid Reactor" and "Research Wraith Cloak", and Merc Compound
  "Dusk Wings" (Onikoroshi 785415). Known upstream defects: Mengsk is missing keybinds entirely and
  Tychus's SCV is on the wrong key (Moss 156484).
- **If you volunteer to make co-op files, follow the patch channel and nothing else.** JaKaTaK's terms
  (400520): US QWERTY, only changes that come out of the patch channel, and "The goal is to make all
  coop keys as close to the multiplayer version as possible without changing the multiplayer version.
  When you're done, post the file and I'll check it for unbounds/issues."
- **Custom and arcade maps show commands as unbound** because the map makers did not set their
  abilities to inherit hotkeys from a vanilla ability (719326). "Top bar powers" in the global hotkeys
  are for co-op and campaign (982493, 537300); in co-op, Alt+Ctrl top-bar abilities re-center on your
  selection, fixed by turning off center-on-selection or changing the top power bar's modifier
  combination (456488, 329344).

## Other software and OS layers eating keys

- **German AltGr is a real blocker** (goldsteal, 2020-03). AltGr registers as `Ctrl+Alt`, which
  collides with the second camera layer and the rally cam; and his non-Windows E1 layout driver
  (DIN 2137-1:2018-12) does not register in SC2 at all (420505).
- **A non-default key repeat rate can make `Alt+P` fire a stray attack in v5** if you release alt
  slightly before `P` (JimKlide 338316, 319337). Others could not reproduce it (SieStein 619594, Sora
  501875). Sora: regedit sets the repeat rate lower than the Windows slider allows (172072).
- **SC2 cannot bind mouse scroll up or down** without external software (Sora 200110, Trebhin 303012).
  Extra mouse buttons are handled by mapping them to keyboard keys in Razer Synapse or Logitech G Hub
  (717810, jaydik 260989).
- **`Ctrl+0` can be eaten by the Windows language-switch shortcut** — a recurring cause of a dead rally
  cam even when the in-game menu looks right (nostrocker 705573, 872425).
- **Don't lean on OS key-repeat instead of a second bind.** JimKlide holds `k` and lets auto-repeat
  walk him to the pool (148566); Siaal says `kp` beats `k-k`, it matters more for pylons and depots
  than a once-a-game pool, and registry hacks only lower the repeat delay so far before the computer
  becomes unusable (205588, 579506).
- **Ctrl+Alt+K is silently swallowed by the Kindle desktop app on Windows 10** (378014, 793990).
- **Ctrl+Shift+0 not working is Windows, not SC2** — it is the default "switch input language"
  shortcut, the cause "99% of the time" (824987, 547477, 855767). Win10: Language Settings > Keyboard >
  Input language hot keys > Advanced Key Settings, set "Between input languages" to Not Assigned
  (149978). Win11: settings > time & language > typing > advanced keyboard settings > Input language
  hot keys (485049). Dívell's case never resolved (895967). Separately, AMD Super Resolution takes
  Alt+U before SC2 sees it (349504).

## Rebinds forced by game patches

- **June 2026 patch, US QWERTY** (Edennil 489296): Load Nearby on `-` with regular Load moved to `=`
  (Load is shared by three units, so bind all of them); Gateway to Warpgate transform on `[`; Warpgate
  back to Gateway on `]`; Gateway/Warpgate Dark Templar moved to `-`. Edennil flags these as
  provisional: "This is a starting point, not necessarily the end" (329351).
- **Patch 5.0.14, US QWERTY** (Edennil 456007): Nexus Energy Recharge on `;`; Hydralisk Lunge on `k`
  (alternate on `/` or `-` if you want rapid fire); Hydralisk Morph to Lurker on `P`; Hydralisk Den
  Nanomuscular Swell on `P`; Factory Tech Lab Mag-Field Accelerator on `.` and `[`.

## Where the files come from

- **Betas live in a BETA folder in the Google Drive as raw files**, with the beta Discord channel
  carrying the newest build before the Drive catches up (JaKaTaK 670932; Siaal 927239; Edennil
  744896).
- **There is no changelog between lettered betas** — "no, but the files are all in the drive"
  (JaKaTaK 260776). Bitstorm's workaround is diffchecker (505294); Edennil's is "Then run a diff on
  the 2 files to see what has changed" between versions (604490).
- Distribution has a git ambition that never landed: "the dream has been to transition from the
  google drive to a git repo but we never finished that project" (JuicyJuuce 529074,
  github.com/TheCoreHotkeys). Nobody in the channel recommends version control for a personal file.
  See [tools-and-scripts](/tools-and-scripts.md) for the converter and generation pipeline.
- **The current file is `TheCore6g_Juuce_1.2.2_right_US_Qwerty.SC2Hotkeys`**, at the end of channel
  506640283946188820 (348753, 895317, 943238); 1.2.1 held for most of 2023 and **1.2.2 shipped
  2023-09-29** with the balance-patch binds (591003). **The Google Drive is Jak's and is no longer
  maintained** (652552, 003075); the spreadsheet is frozen too, with anything newer in channel
  1151009323800088636 (446762, 571325).
- **Juuce's public v6 deliberately omits Edennil's camera changes** to stay aligned with the official
  layout; they live in `6g_right_us_qwerty_updates.txt` (279188, 756437).
- **Only files with "Juuce" in the name are current.** "The Juuce ones are the correct ones to
  download. They are the ones that are updated. The ones you linked are the original files that don't
  have the updates from recent patches and don't have coop or campaign" (799844). Asked whether every
  file in Jak's Drive is outdated, "Yes" (062076); "We don't control the drive, it's jaks" (907425).
  Symptoms of the old files: unbound Research Interference Matrix, Battery Overcharge and Research
  Tectonic Destabilizers (890982, diagnosed 946768) and Attack still on `A` (065531, 570875); the same
  diagnosis recurs at 015131, 063500 and 137731.
- **Since 2024-08 the current download is Juuce v6 version 1.2.3**, filenames of the form
  `TheCore6g_Juuce_1.2.3_right_US_Qwerty` (268756, 844234, 797790). The v5 files and the original v6
  files are no longer patched; the Juuce builds also carry the campaign and co-op keys (000862,
  607371).
