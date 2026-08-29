---
type: Reference
title: FAQ
description: The questions TheCore's Discord answers over and over — version, install, co-op, modifiers, cameras, control groups, unbound abilities, learning time — and how the answers changed between 2019 and 2026.
tags: [thecore, starcraft, discord, faq]
source: "TheCore Discord #general 389438169520799746, 2019-08-24..2026-08-27"
---

# FAQ

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-389438169520799746.jsonl`; a few 6-digit suffixes collide in the 23k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## Which version should I download?

- **Take v6 in JuicyJuuce's build — `TheCore6g_Juuce_1.2.3` from 2024 on, `1.2.2` before — unless fluent in an older one** (476478, 268756, 799844, 088832, 146752, 857927). It is the maintained continuation, not a side branch: Core plus campaign, co-op and post-v6 abilities (531971, 212211), quoted in full as `TheCore6g_Juuce_1.2.2_right_US_Qwerty.SC2Hotkeys` (943238, 145770).
- "5 or 6?" recurs across the whole period, 2019 to 2024 (954006, 615828, 513098, 870741, 532865, 378378, 019674, 017694, 913812, 082556, 145351, 669594, 329530, 944064, 499088, 202282, 410827, 226586, 035594, 388402), with "should I switch from v5?" alongside (981576, 897857, 075881). The answer moved:
  - To 2019-11-11, stay on 5 (361556). From 2019-11-26, take the 6 beta and don't relearn each change (203371). From 2019-12-20, "Switch now unless you care about coop and camp keys" (620224, 098187).
  - Through 2020, 6g from the beta channel plus the changes under it, then Core+ if wanted (798464, 187914, 336266, 795995, 869318, 989740, 132673, 818292, 032232, 970791, 380353, 880598, 375101, 432907, 623860, 096380, 663563, 227578). Zerg starting fresh should weight v6's cameras and injects (561392, 464341, 071233); don't switch if comfortable on 5 (854605); 1 to 4 are legacy (032401).
  - 2021–2022 softened it: "marginal difference; take v6 unless you run a customized v5 or have pinky trouble" (757087, 460180, 514813); both fine, v5 for control group feel, v6 for cameras and injects (136336, 010428).
  - From 2022-09, JuicyJuuce's updated build (704050, 992754, 914489, 523452).
- **No size or race variants** since v4 (811469, 941886).

## Right or Left, Core or Core Lite?

- **"Right" and "Left" mean the mouse hand**, not the writing hand, asked and answered every year (383741, 727135, 360650, 419264, 128628, 151098, 041994, 520701, 886601, 760441, 379724).
- **Core Lite is a different author's layout with the same goal**: compact, all left-side, for laptops and boards with too few keys. Take full Core if your thumb reaches all three modifiers (571093, 310914, 043134, 763427, 937579, 046548). Lite is not "Left" — Left is for left-handed mousing (508969, 855946) — and lives on GitHub with its own docs (527306, 271472).

## Where do I download it, and where does the file go?

- **The pinned info channel <#506640283946188820>; take the last Juuce file there**, not Jak's Drive (515358). Before that, Jak's Drive folder "TheCore 6.0 Multiplayer Only": pick your keyboard, skip `old/` (710740, 371840, 519550, 210907, 609888, 294258, 806146, 119360). Binds added after a beta shipped were posted under it, so scroll the beta channel rather than re-download (876554, 132490). Old versions are there too, but the OBSOLETE VERSIONS spreadsheet is "a disorganised dumping ground" (215528, 679680).
- **The file goes in `C:\Users\<yourname>\Documents\StarCraft II\Accounts\<numbers>\Hotkeys`**, or the same path under `Library/Application Support` on Mac — never Program Files or the install directory (416906, 027028, 748648, 092991, 757753, 590046, 167971, 226607, 163941).
- **`Hotkeys` doesn't exist until you save a custom profile in the editor once.** Save one or make the folder by hand; fastest route there is right-clicking a replay, "show in folder" (214302, 051925, 616682, 311121, 948256, 995584).
- **SC2 doesn't see the file:** reopen the options menu; still missing means OneDrive-redirected Documents or a second account folder (653683, 898700, 784981).
- **All my binds disappeared:** check the selected profile before assuming corruption; profiles sync from Battle.net (405462, 643531).
- **The editor shows keys I don't recognise:** you last played arcade or campaign, so it shows the Story set; start a multiplayer or empty custom game (769748, 163328).

## Co-op, campaign, arcade and team games

- **Since 2023 the Juuce files include campaign and co-op, so "multiplayer only" no longer applies** (748729, 558016, 433208, 875229).
- Through 2022 the answer was no, use v5 for those modes (889812, 361862, 038972, 879746, 439420, 277672). Stukov's infested banshee had nowhere to go; the campaign has unbound units and no public zerg file (917717, 355020). None was ever planned (825213, 814880); several people converted one themselves in 10–20 minutes (267445, 117021), or per commander (691345).
- **"Multiplayer only" never excluded team games**: 1v1 and team ladder both work, only campaign and co-op binds are missing (019059, 047336, 234024, 778887, 367662, 627012, 544683, 122375). Under those old files, arcade or campaign play could damage the profile: back it up, switch to Default or Grid for arcade (195286, 847616, 056320, 118484).
- "Top bar powers" in the command list are the co-op and campaign ones (982493, 537300).

## TheCore+ and moving your modifier keys

- **In v6 there is no separate Core+ file. "Plus" is just moving physical Shift, Ctrl and Alt onto better keys outside the game; the file is identical** (062870, 861488, 310914, 549470, 574450, 123080, 522842, 735121). Ergonomics only, no extra actions (843777, 335098); a separate file in 5.0 and earlier (771328, 106590, 850635). You need neither it nor a remappable keyboard, since 6g works on a stock board (067085, 230708).
- **"Rebind your modifiers" changes what the keyboard sends, not the SC2 hotkeys**: physical Shift → Ctrl, Ctrl → Alt, List → Shift, via firmware, AutoHotkey or SharpKeys, never the hotkey file (888596, 601172). SharpKeys for permanent, AutoHotkey to scope it to SC2 (175814, 480897). Swapping Windows and Alt: permalink 901361363685879808 (654131).
- **Don't remap onto AltGr.** On ISO boards the right Alt is AltGr and registers as Ctrl+Alt, so use the left; a dead Alt or cameras that won't jump is almost always this (964173, 611614, 790696, 227398, 826709).
- **Under Core+, Shift moved to the appskey**, so "my shift key does nothing, I can't deselect or queue" means pressing a key that no longer does that job (312210, 866567, 734353).

## Where do my fingers go, and do I tilt the keyboard?

- **No single home row: `jiop` for macro, `jkl;` for army and micro** — jaydik's "two home rows" (598722, 837504, 069643, 689039, 944636, 168274, 436523, 542993, 569607, 965142, 205298, 921791, 518535, 677652). The thumb sits on `/` in `jiop`, on the modifiers in `jkl;` (579794, 389440, 554803). Earlier: "JIO; or JKL;, index on semicolon, not HUIL" (920714, 164574, 805120), and the named positions "wasd" (jko;) and "arc" (jio;). A pinned #general image marks the home keys yellow; the TL.net gif is 5.0, stale (646679, 485746). Per Luna Cancels, none of it is written down outside the Discord (765979).
- **Follow the finger chart while learning, then let comfort and accuracy win** (486740, 762132). Charts in the pins (563906, 272144); keyboard-layout-editor for ISO (989683).
- **Tilt is required in v5, optional in v6**, which is designed flat (370004, 681802, 970857, 484104, 129738, 461461). Most regulars tilt anyway: v5 wanted 30–45 degrees, v6 people try 10–15, one answer 30 clockwise (842618, 697237, 254952, 057936). Tilt means rotating off the desk edge, not raising the feet (842618); if you can't tilt far enough to reach the modifiers, slide the board left (126155, 258540).
- **v5's finger positions mostly still apply**, but v6 is flat, attack is on `;`, `/` is thumb-only for build-advanced (172618, 052500, 325477, 145385). On `/`, index by default, thumb when the index would repeat (836352, 119936).

## Camera locations and the Alt key

- **Alt is centre-on-selection on purpose, and create-camera shares a key with centre-camera. Hold Alt through the whole opening — minimap click, camera key, click again — never release** (064976, 671356, 924740, 782145, 344211, 447036, 736917, 730132, 498206, 551303, 459112, 344835, 371601, 408734, 000038, 038528, 264852, 340562, 429958, 867516, 794570, 344991, 011637). Sora, 2020-06: "its a more or less frequently asked question" (994925).
- If that's awkward, set cameras off the main hatch and remake them as bases go up (950144, 130142).
- **Camera 8, the rally cam, is the exception**: set `Ctrl+0`, recall `Ctrl+9`, no Alt, and use it for arbitrary spots (130904, 130240, 017025).
- **`Ctrl+0` or `Ctrl+Shift+0` doing nothing is Windows** eating it to switch input language (824987, 149978); the other dead-camera-8 cause is confusing create with recall (705573, 588316).

## Control groups

- **Ctrl adds and steals; Shift creates and overwrites** (441277, 739156); Shift also adds to a second group without pulling units out of the first (630746).
- **Assign and select share a key, differing only by modifier**; the one extra alternate is `Alt+J`, adding to the town-hall group (763453, 090010, 079125, 195295).
- **"Add to control group" on Ctrl+Shift+Alt is not meant to be pressed**; use add-and-steal on Control (288833, 023360, 982151, 684896).
- **The trash key is a control group with add and select swapped**, so the comma group assigns instead of recalling (578094, 114544, 971813, 646080, 069256); "What is SALT?" comes up in the same breath (307389, 330771).
- **Select-all-army on `Ctrl+Alt+Shift+Y` is deliberately impossible**; learn control groups, or click the button above the minimap (734721, 640168).
- **`N`, `B` and `G` are hard on the pinky — avoid them** unless you have a plan for groups 8 to 10 (988412, 116800, 427783).
- **Tab between unit types on the mouse side buttons**, next and previous subgroup by default; older versions used Tab (285662, 895400, 123156, 877844, 281809, 306556, 096778, 312199).
- **Groups that don't match the spreadsheet** mean the wrong file for your keyboard, or a stale sheet (232980, 645672).
- Five schemes were posted in 2020. jaydik's zerg v6 set, twice (203433, 158251): `O` hatch and upgrade structures, `I` inject queens, `J` main army, `L` micro army, `H` spellcasters, `G` creep queens, `M` scout/detection, `N` harass, `B` home and drop defense, `,` trash. Siaal's moves creep queens to `I`, drops injects, puts upgrades on `B` (255648). TOMES' (795679) splits the army across `J`, `K` and `L`, evos on `N`. Poletes' protoss set (407488): `J` main army, `I` non-warpgate production, `O` nexus, `L` spellcaster, `M` micro air and scout probe, `N` second a-move army, `H` prism with army, `B` secondary air, `G` scouts and drop defense, Shift+back-mouse warpgates.

## Why is this command unbound?

- **Blizzard added it after your file shipped — bind it yourself, by association** (751720, 516116); check the patch rebind lists when an unfamiliar name appears (456007, 489296, 193567). Method: spreadsheet ability order, most efficient free key first, adjusted for synergy (628968, 770631); the rest go on any free ability key (751059, 771976).
- **Battery Overcharge, Tectonic Destabilizers and Stasis Ward postdate 6.0.** Convention: leftmost free key in the lowest zone, usually `[`, the standard answer for Battery Overcharge (484352, 711131, 701652, 264788, 667275).
- **Holes in the shipped 6.0 files:** load, evolve burrow, summon adept hallucination, Battery Overcharge, Sentry Hallucinate's `/` alternate, Cyclone lock-on's `P` (074193, 515550, 729296, 720272).
- The August 2020 patch left Spray and Unburrow unbound and popped a dialog. Bind new entries to keys you never press: `F13` up, Insert/Delete/Numpad, `` ` ``, `1` (802886, 652434); doesn't always suppress the popup (704702).
- **"This key does nothing"** in early 2020 was 6f's missing alternates; upgrade to 6g (944734, 332225). Check your version (6b vs 6g, 5 vs 5.0plus): v5 has unbound recent upgrades and a broken control group 9. Look the command up in the in-game menu (803359, 425483, 705492).
- Or a conversion artefact (on UK QWERTY the `\` binds move to `#`), or a deliberately banished command. Check the key's position, not its character (024882, 924793, 655680).
- **Attack sits on `;`**, "a very comfortable key for a very important button"; reports of it unbound mean an accidental unbind or a non-US board (271296, 225236, 211392). Attack on `A` is the pre-Juuce file (946768, 570875); otherwise `A` is Move, parked away on purpose (942336, 664561).
- **Warp-in is unbound by default**; use select-all-warp-gates or a group (545356, 106216, 275720, 453077).
- **Rally is on `z` and TheCore doesn't use it**; right-click sets it (088166, 516362, 830593).
- **Cancel on `7` is deliberate:** abilities got the near keys, `7` was next unused; move it if you like (805716, 507699).
- **Stop, hold and patrol need Simple Command Card off**, in Options → Interface (137984, 088552).
- **`J` is deliberately not rapid-fire**, so storms, forcefields, fungals and biles cast one at a time; bile has a rapid-fire alternate (318539, 691008, 818050).
- **Inject is on `/` because `/` is a thumb key**, pairing with a camera on every other finger; `;` would repeat the index already on camera 1 (272801, 466651).
- **A building needing the same finger twice** is what the alternate build-basic key is for: `k` and `p` pair, so a spawning pool is `p` then `k`; the thumb on `/` covers build-advanced (391067, 457468, 331074, 446359).
- **Editing binds yourself is explicitly encouraged** (121428, 490014, 134430), in the `.SC2Hotkeys` file, not the editor, which caps you at two binds per action where TheCore needs more (949022, 940483, 896641).

## Non-US keyboards

- **Run TheCoreConverter, or add your layout to it and share the result** (385488, 438559, 795200, 418431); it handles AltGr. Use a localized file if one exists — German for 5.0, none for 6 (658606) — else compare key by key against the US file and rebind in-game; for ABNT2, just use US QWERTY (245349, 142216).
- v6 was US QWERTY right-handed only as of 2020-03; the fallbacks were a hand-converted copy from Siaal or 5.0, which ships all languages (765127, 563098, 693707, 090708, 714507, 834906, 016795). UK QWERTY works if you have AltGr; AZERTY exists for 5 and unofficially for 6; QWERTZ has none and needs customizing (923816, 414696, 341501).
- Collisions: German puts attack on the wrong key and drops Select Hotkey Group 9 (555723, 326039); AZERTY lands Engineering Bay on `²` at the top of the board (603864, 942440); Russian, closest to UK QWERTY, collides morph corruptor, hatchery and gather resources on grave (885279). Even UK and German differ on square brackets, "which actually screws with everything" (120129).

## What keyboard do I need?

- **Match the layout, ignore the size, check where Fn sits** (424818, 816498, 940958, 211156). A 60% is fine if you can move Fn (128474, 197226, 090708); a laptop with half-size arrows is not (714507).

## How long does it take, and how do I practise?

- **Two to three weeks to feel normal; expect your APM to halve on day one** (968197, 470979, 512283). Earlier answers agree: a week of hard drilling or four weeks casual to ladder-ready, a month from standard hotkeys to competent (faster from an older Core or a modified standard), 100 hours to confidence, months to your old level, with a several-hundred-MMR dip and pinky soreness over the first 40–60 hours (051780, 364790, 542720, 893765, 181246, 621259, 044392, 963242, 686972, 805960, 428574, 912960, 273858, 200003).
- **It won't ruin your typing** (681395, 470794).
- **Practise against very easy AI or in customs, not on ladder**: one build order, quit-and-rewind, ~15 minutes of the arcade Hotkey Trainer (802432, 547432), then the jump build drill (315099, 499129). One facet at a time, but cameras and control groups from game one (806780, 139028).
- **Start on Core rather than default hotkeys** (361694, 171153); whether a brand-new player should is contested, see [learning-and-practice](/learning-and-practice.md).
- **The Hotkey Trainer is on the arcade**: Custom → Arcade, "Hotkey Trainer LotV Patch 4.12.0" or "Hotkey Trainer LotV 4.1.4" by era; take the last entry, highest version wins (066522, 832704, 355765, 431814, 819551, 541020, 132283, 614564, 177028).

## Documentation, spreadsheets and the FAQ

- **The whole layout is in the Drive spreadsheet, not on the site** (904677, 624628), stale in places (139586, 726239). There's a visualizer too, and Core Lite has GitHub docs (884143, 060379).
- **When the spreadsheet and the file disagree, trust the file** — the position since 2019-11-09 (628706, 751553, 216261); before that, the spreadsheet (258689). The 2020 refinement: its top section is good, the per-race sections at the bottom are stale (484132, 080977).
- **The start sequence is in "The Course", section 3.0**, and in the FAQ channel (060352, 163680); the beginner path is the Drive copy of The Course plus the Hotkey Trainer map, Simple Command Card off (352229). HoboWizard's objection that "the faq seems more geared toward more veteran sc2 ppl" drew no reply (928522).
- **TheCourse on YouTube is v4/v5 and out of date on keys** — nothing current, nothing Protoss-specific (927050, 382302).
- **When the FAQ names a key that isn't yours** ("hold `P`" when SCV is on `-`) it was written for another version: "Press and hold the scv button, whatever it is for your version" (225485, 285890).

## Is it legal in tournaments?

- **Yes in keyboard firmware; no if it needs software on the tournament machine** (094110, 046016, 684608). A 1:1 AutoHotkey remap is the same in principle and fine online, but probably not at a LAN (953651, 418482, 463936, 058162).

## Other games, and is TheCore still maintained?

- **No official Core for Stormgate, AoE4, Brood War or SC Evolution**, just a forum post per game (401213, 284799, 527428, 675402). For Brood War and SC:Remastered see the Brood War channel's pinned post; some binds need AutoHotkey-class software (946004, 938774).
- **TheCore is not maintained and hasn't been for years** (234856, 508018). JaKaTaK left for Immortal: Gates of Pyre, and v7 is too early to wait for (890635, 864563).
