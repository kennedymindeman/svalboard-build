---
type: Reference
title: Patches and timeline
description: Year-by-year record from 2019 to 2026 of the StarCraft II patches that changed or unbound hotkeys, the fixes the channel adopted, TheCore and Juuce releases, maintainer changes, and channel news.
tags: [thecore, starcraft, discord, timeline]
source: "TheCore Discord #general 389438169520799746, 2019-08-24..2026-08-27"
---

# Patches and timeline

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-389438169520799746.jsonl`; a few 6-digit suffixes collide in the 23k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## 2019

- 2019-08-25 — **Rebinding at the keyboard is tournament-legal; installing software on the tournament PC is not.** Edennil: "Altering your keyboard is fine. It's allowed. As long as you can make the change with keyboard firmware and dont need to download a program on the tournament computer to make the change", citing pros who buy boards for faster repeat rate and delay (046016, 684608, 018928). Core+ "is just movinn the location of keys away from the standard keyboard" (989130). gcask re-asks on 2019-11-24 and gets no second confirmation (902666).
- 2019-10-11 — Legacy versions get no support, only self-maintenance: "taking an older version and updating it as you find unbounds" (JaKaTaK 687745).
- 2019-10-19 — How much the layout will change after BlizzCon gets no firm answer (bean 265868).
- 2019-11-19 — Core 6's release is targeted at the major design patch, "to have it fully released either right when the major design patch goes live or as shortly after as possible" (Edennil 009349).
- 2019-11-26 — **A patch breaks hotkey assignment.** Infestor hotkeys "cannot be set, they return to unassigned" (Ninjury 754241); Eleven confirms binds revert on joining a new game and that it hits non-Core users too (328778, 925279).
- 2019-11-27 — A worse variant kicks players out of 1v1 with an autoloss (FredericK 096960), matched to a Reddit thread showing it on standard hotkeys too (954058). JaKaTaK: "I don't think your hotkey layout is causing the issue since it's happening to standard players" (810905), and "this patch is buggy, cutting the Sc2 team is finally starting to create problems we're not used to seeing" (768340).
- 2019-12-06 — A video for 6 comes only after 6 is finished; requests declined because the layout is still changing (Edennil 539915; JaKaTaK 475182). Bitstorm: "strictly speaking it's probably more alpha than beta atm" (979393).
- 2019-12-20 — A 4.0 user asks whether he must keep fixing binds after every patch (Pstv 870741); JaKaTaK: "at most you just need to add a couple of new upgrades or w/e. Not too tricky" (620224).

## 2020

- 2020-01-12 — Stukov's infested banshee collides with multiplayer binds; cloak and burrow land on keys already in use, with no fix. SPARROW: "No magical fix rn / I tried a lot of things, impossible" (149915, 643147, 497924).
- 2020-01-13 — Streamer cdnthe3rd watches Jak's camera-hotkey videos (829509, 622080).
- 2020-01-15 — The SALT mod puts the town hall off-centre at game start; Jak's workarounds are to wait for the broodlings to vanish before picking a race, or to rewind and resume (951315, 064596, 730399).
- 2020-01-21 — JuicyJuuce offers to pitch TheCore to Lowko. Jak: "Lowko would be one of the biggest pickups we could have.  We'd have to build a statue for you" (999199, 610462).
- 2020-01-23 — RoboZerg posts a 6g file with the patch-channel changes already applied — a community build, not an official release (110731, one attachment).
- 2020-01-24 — TheCore is still under development: "We can always improve" and "I will work on TheCore for as long as I have the time to do so" (JaKaTaK 549767, 153664). A v7 is mentioned, not described (061646).
- 2020-01-28 — Justice41 updates the arcade hotkey trainer to patch 4.11 (832704).
- 2020-02-24 — Drekken makes and posts a TheCore video (012754, 545478).
- 2020-02-26 — Pros are overwhelmingly on standard or grid; ShowTime and Neuro are the two named Core users (783995, 667295, 618128).
- 2020-03-24 — `K` and `I` are swapped in a recent 6-beta revision, which matters if you learned from an older diagram (285002, 831691).
- 2020-03-24 — **There may never be an official 6.0 release.** JaKaTaK: "This is a passion project full of volunteers. I'm in a start-up creating an RTS, so TheCore got a huge priority drop once I started full-time. 6g is baller as fuck and I highly recommend it, but getting it coop/camp compatible AND making sure it works for all keyboard languages is a task I don't foresee having time for for a long time" (638585, 337792).
- 2020-04-01 — SC2 4.11 removes infested terran, which is why Hotkey Trainer maps updated for 4.11 behave and older ones do not (Siaal 187476). 4.11 is still current on 2020-05-18 (Sora 096533).
- 2020-04-07 — LotV made injects queueable, so rapid fire is no longer the recommended main inject method — it just sends queens wandering. Its remaining use is queueing injects fast when you have been missing them (Siaal 128454, 975059).
- 2020-04-12 — Tournament rules on firmware remapping asked again, never answered (JimKlide 558474).
- 2020-04-18 — v5 predates several units and upgrades, so lurker upgrades and microbial shroud are unbound in it (Sora 345600).
- 2020-05-21 — A new nexus ability is announced for the next patch (AvroArrow 957908); TheCore will not cover it (JaKaTaK 439545).
- 2020-05-22 — **The TheCore website is about four versions out of date; do not use it.** "The core site is like 4 versions ago... there is literally nothing that is the same" (Poletes 624628). Use the Drive spreadsheet (904677).
- 2020-06-01 — Rapid-fire inject confirmed dead. Poletes: "rapidfire inject does not work anymore, lotv busted it" (007008), confirmed by TOMES (807646). AvroArrow proposes holding `/` through the camera sequence instead of tapping (456854); holding rapid-fires on the first hatch and pulls every queen there (673829), and streetplay finds it selects the hatchery and sticks on spawn larva (151294). The tap sequence stands (jaydik 716836).
- 2020-06-03 — Battery Overcharge is reworked to be "less niche" and bound for the first time; 60-second global cooldown (Siaal 840788, ScaryMouse 544981). Poletes rates it above Recall (697893).
- 2020-06-07 — Warp gate transformation is automatic now, so gateways no longer need a control group to be transformed (Poletes 110578, 293876, 966167, 629894).
- 2020-06-16 — A patch breaks replay playback: "ree the patch came out so i cant watch replays" (Poletes 845414).
- 2020-06-17 — **The shipped 6.0 files predate Battery Overcharge**, so the Nexus ability has no bind anywhere (515550). The Hotkey Trainer arcade map is versioned against 4.12.0, and an older copy from the arcade list gets an outdated trainer (663892; Siaal 819551 on 2020-07-13).
- 2020-07-30 — Battery overcharge ships unbound in 6.0 (jaydik 379324) and is absent from 5.0 entirely (Edennil 690965, 2020-08-10).
- 2020-08-01 — Raven energy is "fairly new" too, the reason banshee speed and raven energy break the "speed on `;`" rule (jaydik 043787). Microbial shroud marks a current Hotkey Trainer build (Siaal 405117).
- 2020-08-14 — Terran upgrades are broken in the trainer (Harri 311918); SwordSmith finds only a 4.7 build, with a mislabelled "neosteel frame" (177028).
- 2020-08-20 — Named Core users: ShoWTimE, Neuro (Hoplite 572008), PiG (JaKaTaK 860810).
- 2020-08-21 — **An unannounced balance patch adds a spray menu**, 14 sprays plus a menu-access key (Edennil 802886; pinion 852670). In existing files `Spray` and `BurrowUp`/Unburrow (typically `;` for zerg) come out unbound along with two more submenu sprays (jaydik 885105), so every match opens with an "essential hotkeys are unbound" popup.
- 2020-08-22 — **Partial rollback.** The 14-entry submenu no longer appears on the worker spray ability and `LoadOutSpray` lines are no longer written when you save from the UI (pinion 924139; jaydik 932376), but 5 unbounds remain on both core4 and core6 (839296). pinion: "really going out of their way to break things that worked perfectly for years" (358416).
- 2020-09-05 — Newer, more relaxed inject mechanics get a passing mention, never described (Oɱι 757648).
- 2020-09-07 — Battery Overcharge was added after the core6 file was built, hence unbound (Edennil 930226).
- 2020-09-21 — Poletes keeps a real `alt+L` in QMK to turn battery heal off (238165).
- 2020-09-27 — Battery Overcharge still has no official 6.0 binding; the convention is `[` (TTarps 084714; jaydik 355934).
- 2020-10-21 — **FrostGiant's unannounced RTS.** JaKaTaK: "Soooo... do we make a version of TheCore for the FrostGiant RTS?" (366292). Siaal: "All games that can be core-ified, probably should be core-ified" (415701); nothing is known about the game yet (Sora 041152).
- 2020-11-04 — The #faq channel is created with advisor-only posting, seeded with the camera and v5-vs-v6 answers (JaKaTaK 945026; Poletes 833129; ScaryMouse 805909 on 2020-12-01). Channels by id: <#773643919992160288> (FAQ), <#506640283946188820> (docs and the Drive link), <#651526731517132839> (patches/updates).

## 2021

- 2021-01-27 — Ctrl+shift camera jumps stop working on Core4 and a season change is suspected; it is a dead ctrl key, not a patch (pinion 545714, 867018).
- 2021-02-13 — **Battery overcharge and researching tectonic destabilisers were added after v6 was finalised, so they are unbound in every official v6 file** — the direct consequence of v6 being frozen (ScaryMouse 701652, 303552 on 2021-03-21).
- 2021-08-03 — Gateway-to-warpgate transformation became automatic in patch 4.7.1, which is why the bind still on `C` is undocumented and unnecessary (Edennil 793128, 988358, answering bunfoof 981824).
- 2021-09-10 — Battery Overcharge, Research Tectonic Destabilizers and Stasis Ward all postdate 6.0, hence the unbound keys new users keep finding (ScaryMouse 711131; Edennil 398795 on 2021-09-29).
- 2021-11-02 — Infested Terran no longer exists, but the editor may still show it until you reload the hotkey set (Edennil 754730).
- 2021-12-20 — Core+ in keyboard firmware is fine at a LAN; Core+ in AutoHotkey probably not, because you play on the venue's machines (uduntuntu 463936, Edennil 310363).

## 2022

- 2022-01-28 — Blizzard keeps adding abilities after Core 6 shipped and they arrive unbound (751720; 934987 on 2022-02-14). Core 5 masks this because SC2 silently assigns non-conflicting defaults to commands the profile does not mention.
- 2022-04-02 — Pros listed in the handbook as Core users: showtime, pig, probe, nxz, neuro (911191).
- 2022-04-09 — TheCore itself is tournament-legal. Mell00yell00: no external software is technically allowed in competition, but one keypress producing one input is fine, while binding one key to emit Ctrl+Shift would be cheating (058162). Whether the AltGr trick is legal gets only "keyboard advantage, i guess" (907998, 552640).
- 2022-05-09 — Edennil points newcomers at a post listing everything tagged "NEW ABILITY," noting "They will apply to both 5.0 and 6.0" (704286). No Blizzard patch in this stretch changes hotkeys.
- 2022-06-25 — **Stormgate becomes the forward-looking topic.** JohnKavinski asks whether a Core-style layout will transfer given the devs want it to feel like SC2 (533618); Mell00yell00 links Frost Giant's own reply (179517), which JohnKavinski reads as confirmation that "its still worth switching to the core" (075979).
- 2022-08-27 — SC2 has no select-all-barracks command: "Correct you have to add them to a cg or click on them every time" (MatosMachine 252391, confirming Pastah 893636). Edennil says TheCore would support both approaches if it existed (457478).
- 2022-11-07 — A TheCore for Modern Warfare 2, "rev 0.5 beta" (259348).
- 2022-12-17 — A Dota 2 layout (059926).

## 2023

- 2023-01-31 — xQc streams SC2 to roughly 50,000 viewers and briefly revives channel interest (268949).
- 2023-02-09 — Abilities added and removed since v6 are why the file has unbound commands (566950; 004416 on 2023-02-21). Gateways now auto-convert to warpgates, making the banished select-all-warpgates bind worth reclaiming (012018). **Queens can now be commanded during the inject animation, which broke the old hold-base-cam rapid-fire inject — superseded** (770483, 793866, 201364).
- 2023-02-12 — No official Stormgate version is planned (771217).
- 2023-09-11 — Edennil settles the cyclone key ahead of the release: the speed upgrade gets `[` **and** `.`, because `.` was the old upgrade's key in the file and `[` is what the spreadsheet used, so users can pick unit-production synergy or the more comfortable key (620884, 433818).
- 2023-09-21 — **The 2023-09 community balance patch changes four hotkeys; Juuce's 1.2.2 implements them** (proposal 149662, agreement 066900):
  - Mothership cloak: `[` — matches ghost and banshee cloak, and zerg burrow.
  - Cyclone speed upgrade (Hurricane Thrusters, replacing Mag-Field Accelerator): `[` and `.`.
  - Medivac energy upgrade in the Fusion Core: `/` — matches the same-named campaign ability. Edennil mildly preferred `[` but had no objective case and deferred, the patch being live.
  - Raven interference matrix research in the tech lab: `K` — matches the ability key on the raven.
- 2023-09-22 — Jak has moved to Immortal (channel 440141641907437570), said to ship core-like hotkeys at launch (652552, 003075).
- 2023-09-29 — 1.2.2 signed off, shipped and pinned (Edennil 622516; JuicyJuuce 591003; Edennil 873450).
- 2023-10-03 — Older files still load after the patch, just with the new abilities unbound (531897). A claim that the October 2023 update "killed" Core Lite does not survive testing: cthulhug says Lite is unplayable (497768), Altafen plays a game on it and cannot reproduce (306154, 636678). Kykeon's parallel problem is a second account folder (784981).
- 2023-11-03 — A 2023-11 balance update adds a few hotkeys, already in the current file (409573).
- 2023-11-25 — Nobody has done an AoE4 layout (393564).
- 2023-12-06 — Stormgate requests are routed to the per-game forum post (Lunarnova 675402, Edennil 825030).

## 2024

- 2024-01-19 — Battery Overcharge gains a hotkey in the 2023-11 update (Z3R0GT 015666).
- 2024-02-05 — Another Stormgate request, routed the same way (091231).
- 2024-02-07 — A Stormgate demo lands with custom hotkeys (Norax 810324, 767976).
- 2024-02-28 — Advanced Ballistics moves from the Tech Lab to the Fusion Core (Edennil 979840).
- 2024-03-06 — **New patches can add hotkeys whose defaults override Core bindings and unbind others** — the mechanism behind "my old v5 file has unbound keys" (Edennil 989128). See [hotkey-file-editing](/hotkey-file-editing.md).
- 2024-03-08 — Rapid fire is allowed in tournaments, and the day's balance patch cites rapid fire as the reason for a quality-of-life change (798175).
- 2024-04-19 — Brood War has its own forum post and allows far less rebinding, rejecting `-` and `=` (Z3R0GT 558025; MatosMachine 835477).
- 2024-04-20 — The channel moves from a channel-per-game to a forum-post-per-game (Edennil 418276).
- 2024-05-17 — Battle.net restoring hotkey files from its online backup is reported as the cause of profiles reverting (Ryoga_P_Chan 697566), and again on 2024-06-07 (TurgidLeafMan 002049, 170802).
- 2024-05-25 — StarCraft Evolution Complete has no layout; rebuild it from the Brood War post (Edennil 527428).
- 2024-07-30 — Stormgate request routed to the per-game post again (Edennil 401213).
- 2024-08-14 — Saltese posts a year-long AoE4 keyboard project and is routed to the other-games post (823834, 200193; Edennil 284799).
- 2024-10-06 — Stormgate's keybinding process is discussed (Edennil 720352).
- 2024-10-21 — **Patch 5.0.14 changes ability priority and breaks several binds.** The PTR notes and Blizzard's "highest-priority available ability key" policy are the root cause (Edennil 212870).
- 2024-11-19 — A thread is created for ZeroSpace (Edennil 238044).

## 2025

- 2025-01-04 — The Frenzy-on-`P` collision with Hydralisk and Lurker keys is explained (JuicyJuuce 110495), and **JuicyJuuce commits to updating all language variants on each patch** (143956).
- 2025-02-09 — A thread is created for Heroes of the Storm (Edennil 176624).
- 2025-04-26 — AoE4 comes up again (Ser 466112).
- 2025-05-20 — League of Legends gets a dedicated thread (Icyeye 016094; Edennil 183016). Edennil writes up his generic porting method (057649): move modifiers to the thumb; make action sequences alternate fingers (in SC2 that means control groups and abilities never share a finger); rank your keys by ease of press and your commands by frequency-plus-urgency and match the lists; and use modifiers more than feels natural, since they are usually under-utilised.
- 2025-05-22 — **The Mass Recall campaign mod has broken hotkey handling** — cancel does not work at all, stim and cloak cannot share a bind, load and unload break — and nobody has a clean fix. The only method offered is to read the hotkey file and work out what each entry connects to, which still leaves entries missing (Milkyway 384242; MatosMachine 862484, 657128 on 2025-05-23).
- 2025-06-16 — Beyond All Reason comes up as a port target (Lunarnova 835123).

## 2026

- 2026-06-10 — An onboarding site is under construction by Edennil (993774).
- 2026-06-25 — A second onboarding site is under construction in parallel by DeathDealer (536085, 592782). JaKaTaK makes a cameo return, after what the channel calls "14 years" (866360, 627388).
- 2026-07-03 — **A June 2026 patch adds Load Nearby and reworks the Gateway/Warpgate transform**, needing rebinds (Edennil 489296). See [hotkey-file-editing](/hotkey-file-editing.md).
- 2026-08-27 — There is no archipelago.gg randomizer profile for TheCore (Skippy 587389).
