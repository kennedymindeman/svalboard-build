---
type: Reference
title: TheCore Discord overview
description: What #general of TheCore Discord is, the eras it passed through from the 5.0 release to the community-maintained "Juuce" files, who answered what, and what this distillation of 2019–2026 does not cover.
tags: [thecore, starcraft, discord, overview]
source: "TheCore Discord #general 389438169520799746, 2019-08-24..2026-08-27"
---

# TheCore Discord overview

Message ids in parentheses are the last 6 digits of Discord snowflakes in `discord/raw/channel-389438169520799746.jsonl`; a few 6-digit suffixes collide in the 23k-message export, so disambiguate by date if a lookup returns two hits. Agreement counts are floor estimates.

## What the channel is

- **#general is the front door of TheCore Discord and has run as a support desk for most of its life**, for TheCore, JaKaTaK's family of StarCraft II hotkey layouts. 23,419 messages, 2019-08-24 to 2026-08-27, distilled in 18 date-ordered batches of 1,302 messages (the last is 1,285).
- Three things dominate every era: newcomers asking which file to download and where it goes, people six months in asking why a bind is where it is, and regulars arguing design over cameras, control groups and modifiers.
- Other channels carry work #general only points at, so their contents are outside this distillation; in the export they appear as raw ids: `<#651526731517132839>` patches and changelog, `<#530711772496396288>` keyboards, `<#506640283946188820>` finished files, `<#506642591861964801>` dota, `<#440141641907437570>` file uploads (788576, 130463). A v7 channel `963200528022663208` opened 2022-04-11 (016239). Poletes created and curated #faq (961056).
- Files and editing: [layouts-and-variants](/layouts-and-variants.md), [hotkey-file-editing](/hotkey-file-editing.md); dated releases: [patches-and-timeline](/patches-and-timeline.md).

## Eras

**Current state: v6 is the last version JaKaTaK shipped, and since 2022 the files people are told to download are JuicyJuuce's community builds of it.** Edennil, 2023-11: TheCore "doesn't really have any active developers anymore. It's all community based at this point" (113163).

### 5.0, through 2019 and into 2020

- The capture opens with 5.0 as the stable release, and it stays the all-languages, all-modes version well into 2020 while version 6 exists only as betas in another channel.
- It stays the co-op and campaign recommendation for years because v6 never got those binds (Siaal 032401, ScaryMouse 132673); Siaal ran v5 for co-op, v6 for ladder. Hand-size variants were dropped after version 3 and never returned. Edennil later drew the 5.0 and 5.0-Plus layout images on request (959555, 236724).

### The version 6 betas, 2019-10 to 2020-01

- Five lettered betas ship 2019-10-26 to 2019-12-08 — 6b, 6c, 6d, 6e, 6f — each moving keys, so most traffic is which to learn and whether it is safe to commit (954006, 615828, 870741). JaKaTaK designs 6 live on stream and announces the betas in-channel (628706, 488832, 620224).
- 6e shipped with no file — "6e has no file, many tiny decisions need to be made" (532929) — so people playing "6e" worked from screenshots and stream VODs (680064, 816001).
- The spreadsheet and the published `.SC2Hotkeys` files drift apart, and which is authoritative reverses within weeks. Bitstorm diffs the beta files and posts key lines reconciled against the spreadsheet (078996, 216261, 586183).
- gcask is the loudest critic: pinky load, loss of center-on-selection, production checking (198879, 529044, 328203). The era ends with 6f as what most active members play.

### TheCore 6g / 6.0, 2020-01-13 to late 2020

- **6g shipped 2020-01-13** (798464), US QWERTY right-handed only at first, the default for new players while v5 stayed the co-op and campaign answer. Finished by late May (657958), no longer "in development" by late July (787732, 872004).
- Poletes authored v6 optimizations that shipped undocumented (024499) and became the person who edited the seed file and reran the converter.
- JaKaTaK posted a three-message design manifesto 2020-06-16 (427065, 039040, 845683) and a follow-up on reading pro replays (907677, 922332). He conceded documentation was the weak point (786716), started a weekly Saturday 12:00–12:30 PDT check-up (383942), and opened FAQ editing to the Advisor role so others could write docs without him (898247), while repeatedly saying he was working on SunSpear Games (394304).
- Roles followed the load: Mell00yell00 moderator 2020-04-24, pushing for a real FAQ (796827, 960535, 060378); jaydik community role 2020-06-01 (448509).
- An unannounced Blizzard spray-menu patch on 2020-08-21 unbound keys in everyone's file. A Swedish user debugged the Scandinavian generator output 2020-09-25..27; pro player Pokebunny logged his switch daily 2020-10-15 to 10-18, about a fifth of the traffic in that month.
- By late 2020 files are named `TheCore6g_right_US_qwerty.SC2Hotkeys`, and the line is that v6 is current, finished and getting no further official updates (ScaryMouse 825213).

### Post-JaKaTaK, 2021-03 to 2022

- Jak (Tom) went full-time on Immortal: Gates of Pyre and stopped SC2 content, so 6.0 became the final version (Mell00yell00 178436, jaydik 357898, Edennil 816188). By late 2021 Edennil: "the core isn't being actively maintained by anyone" (457994, 163520). In 2021-10..2022-05 JaKaTaK appears once, to ban a spammer (642453).
- **The binding constraint was edit rights, not effort.** Nobody left could edit the Drive documents or Core-Info, so the docs and spreadsheet froze with known errors and the Discord FAQ became the only correctable surface (890635, 785326, 421888, 367976). bunfoof: "the only one who has access to edit the sheet isn't working on thecore anymore" (694218, 273163).
- Edennil's summary: JaKaTaK "moved on to Sunspear Games", the project "hasn't been actively maintained or updated in years", the community "just sort of floated in limbo" answering questions with nobody able to ship changes (334598).
- Three revival attempts ran and none landed. Altafen#6776 pushed for a community-maintained "6h" bugfix release (402718). A v7 channel opened 2022-04-11 planning docs on GitHub and a Discord reorganization (016239, 860426), which Edennil told newcomers not to wait for — "super early in the concept stage... far off" (864563, 287710). Edennil, who had mod permission, proposed doing the Drive-to-GitHub move and the reorganization in a screen-shared voice call (334598, 368124, 606336). SwordSmith raised succession directly (019368, 859550).
- Lady Interstellar offered a campaign/co-op-compatible v6 (444885); the only outcome in the capture is her own Terran campaign fix (843988).

### The community "Juuce" files, 2022 onward

- **JuicyJuuce filled the maintainer gap on the files.** In 2022 he released a TheCore6g with the co-op and campaign binds v6 had always lacked (101372, 282591), then kept maintaining it: updated files adding co-op and campaign support and filling unbound commands (704050, 281030), and the current Google Drive (303189). He is also the one who tells people to open the `.SC2Hotkeys` file in a text editor (483486, 363230).
- By 2023 the "Juuce version" came with national-keyboard variants and patch updates (591003); by 2023-11 the files everyone is pointed at are the Juuce series, e.g. `TheCore6g_Juuce_1.2.2_right_US_Qwerty.SC2Hotkeys`, and he owns the non-US conversion script (286706, 505310, 440706).
- From 2024-08 the Juuce builds are the current release (268756) and he volunteers to update every language variant whenever Blizzard patches (143956). He is also the channel's AutoHotkey expert (675146, 694394). See [tools-and-scripts](/tools-and-scripts.md).

### Maintenance and support desk, 2022-09 to 2026-08

- The standing answer to "is there a v7" is no. Edennil: "It's not actively worked on anymore, it hasn't been worked on for several years" (234856, 508018), repeated each time (004416, 141534, 151450, 539523). Jak's Google Drive is legacy only (422255, 256933, 331092) and the Discord forum FAQ has replaced the old Handbook (368584, 083423).
- Around 2023-09 the server gained FAQ forum posts and a new-hotkeys channel, and answers shift from prose to links (272509, 199899, 279997). Bose wrote the pinned plain-language explanation of TheCore's logic (580246) for users asking "can I change this, will it break"; Edennil pins community material (055521, 051536).
- JaKaTaK left to build a new RTS, Immortal, said to ship core-like hotkeys at launch (652552, 003075); by 2025-26 he is a mentioned cameo (866360). Two late Blizzard patches broke binds and Edennil wrote the patch-day rebind lists (456007, 489296).

## Recurring voices

- **JaKaTaK** ("Jak", Tom) — creator, and the authority on design intent while present. 2019: designs 6 on stream, rules on what a bind is meant to be, announces betas (628706, 488832, 620224). 2020: appears in bursts to settle questions argued for a day, often several stacked at once (919977, 245378, 638585, 208189, 343501), plus outreach (999199). Volume falls all year — 38 messages in late May, six in August (069451, 326220, 623026, 784539, 860810), five in September, three in October (656854, 450438, 366292) — and by late 2020 he is mostly server admin (945026). Two messages are empty (674571, 796197).
- **Edennil** — moderator throughout, most durable voice, de facto maintainer of the answers from 2021. Early: installs, tournament legality, keyboard buying, camera walkthroughs (046016, 477156, 733130), then long-form design rationale and keyboard firmware (271710, 558424). Did the replay research behind core6's control group and camera design and is Core6's co-developer, the nearest thing to an authority after JaKaTaK; switched at 2.0 over pinky-to-Control wrist pain (691072, 664391). From mid-2021 he mostly answers by linking a permalink he wrote earlier; writes and edits the pinned FAQ posts in-channel (986163, 558410, 098762), owns the design rationale ("Every decision is a tradeoff" 080577), writes the canonical long answers (571093, 310914, 805716, 064160). No longer runs the Core: from 2022-02 a Redox split ortholinear built by 1:1-mapping Core 6 onto it then adjusting (660914, 634675, 921680, 529395, 495781), and by 2023-11 a modified v6 on a custom board with an ASDF home. Maintains a keyboard visualizer (721402); explains v5 versus v6 (138206).
- **Siaal** — dominant answerer 2020-01 to mid-2020, handling most newcomer threads end to end and filling in when the creator is busy (958708, 830144). Zerg, small hands, no punctuation or capitals; called "the press secretary" and "painfully helpful" (975827, 043584, 936149, 306389). Keeps hand-converted non-US-layout files and hands them out (563098, 736856), fixed the UK files, gives the clearest explanations of the home rows, spell placement and rapid fire (029536, 685142), and explains the co-op problem, "core plus" modifier rebinds, the trash key and why individual v6 choices were made (361862, 394966, 114544, 184346, 788372, 268628). Built his own campaign hotkeys.
- **jaydik** — Zerg, came from grid, ~3.3k MMR D3 NA (302294, 640159). Highest-volume greeter mid-2020 to late 2020 and loudest v6 advocate; explains the two home rows, control-group and camera mechanics; volunteered to fix the language/handedness parser. Community role 2020-06-01 (448509).
- **Poletes** (addressed as Vae / VaeVictus by JaKaTaK, 919146) — Protoss, diamond 2, 16 cm hands; 320 messages in late May 2020 and the most opinionated answerer of that period. Runs a "frankencore" of 3.0-5.1 plus 6.0 (212938), later a custom QMK layout on the v3.0 footprint (353340). Strongest dissenting voice in the design arguments, citing ShoWTimE and Stats replays (017728, 178400). Maintained and regenerated the files, authored the undocumented v6 optimizations (024499), owned the broken language/handedness parser, vouched that "the current versions on the Google drive are fine" (895666), created and curated #faq (961056).
- **Mell00yell00** — Terran (later described as diamond zerg), moderator from 2020-04-24 (796827, 960535, 060378), second-most-active advisor through 2020; six months into the layout in early 2020 (942685). Asks the "why is it designed this way" questions that pull JaKaTaK in; says he pushed JaKaTaK on burrow/cloak/load consistency during design (197714). TheCore Lite evangelist, keycap-puller, AutoHotkey tinkerer, trash-key-on-thumb proponent; built his own campaign+multiplayer file and gives the multi-file multiplayer/campaign/co-op advice; posts role-pinged announcements such as the April AutoHotkey breakage (827870); camera and inject customizations (150951, 929638); runs a 2-macro control-group setup (659784, 114311); offers spare keyboards to newcomers.
- **ScaryMouse** — UK QWERTY Terran on laptops, stock modifiers, no external remapping (493618). Second-line helper in 2020 who ran TheCoreConverter for people (628867) and gave the v5-for-co-op line (132673); then the main answering authority 2020-10 to 2021-07, explaining *why* v6 is built as it is — camera modifiers, key budget, rapid fire — rather than what the bind is. States no further official updates are expected (825213).
- **JuicyJuuce** — in 2020 the person who knows the repo and site history, still on core5, filing bugs (139925). From 2022 the file maintainer; see the Juuce era above.
- **Altafen#6776** — 2019 to the end. CoreLite user; install paths, banished functions, picking a variant, file-level AutoHotkey detail, correcting others' AHK claims (106079, 152754, 507092). The one person pushing for a community "6h" (402718).
- **Bitstorm** — 2019 beta era: diffs the beta files, maintains the LotV Hotkey Trainer map, modifies firmware (078996, 216261, 586183).
- **gcask** — 2019 Terran beta tester, loudest critic of version 6 (198879, 529044, 328203).
- **SwordSmith** — 2020-08 to 2021. Devil's advocate on training theory, critic of the teaching materials, proposer of FAQ entries (556492), and the one raising who could take over maintenance (019368, 859550).
- **NReilingh** — 2020 v6 learner, clearest explainer of the alt-key and control-group interactions (052570, 282508).
- **JimKlide** ("dima") — 2020, big hands, detailed v6 dissenter and main hardware tinkerer (463318, 648464); switched 5 to 6 in a week (171520).
- **SPARROW** — AZERTY conversions, maintains the AZERTY files for v5 (118376, 953162, 235010).
- **bunfoof** — 2021-08, new Terran on a 75% board who catalogues the spreadsheet-versus-file discrepancies and reports that nobody can edit the sheet (694218, 273163).
- **Bose** — Scandinavian-keyboard learner from early 2023 who turns into a documentation critic and volunteer (800986, 612594, 269971) and wrote the pinned plain-language explanation of TheCore's logic (580246). Good source for what the docs fail to explain.
- **Laaxus** — 2023-11 to 2024-08, learner-turned-answerer (six weeks into SC2, one week into the Core as of 2024-07-08, 008455) giving newcomers his own frequently dissenting advice.
- **DeathDealer** — per-race hotkey graphics, cheat sheets, voice/screen-share onboarding (925771, 821788, 367451).
- **Switch diaries**, the main source for how long the layout takes: Joli Boli, RoboZerg and Thwonk in January 2020; Coyotebd in spring 2020, logging every place the docs lose him (393724); Pokebunny in October 2020, last seen weighing v6, Lite and giving up (309150); JohnKavinski from optimized-standard in 2022 (220817, 506048). See [learning-and-practice](/learning-and-practice.md).
- Second-line answerers and recurring names, roughly in order of appearance: **Sora** (stayed on 5.0), **Mutaller**, **TOMES** (Zerg, camera explainer), **streetplay**, **SieStein**, **Hoplite**, **marin**, **MatosMachine** (co-op, QMK, finger charts, X-Bows remap), **AvroArrow** (Niz Plum Micro 82, found file/sheet mismatches), **bobo38** (author of TheCore Lite), **Heliac** (SharpKeys/AutoHotkey), **andylytical** (a file generator), **Syfogidas** (rebuilt the visualizer), **Fix** (v5 veteran, argues base cam over camera locations, 822481), **bro** (Zerg, own Core6/Lite merge — listed separately from Poletes despite both being called "vae"), **will3285**, **Kasslim**, **Vinouko**, **Guinpenza**, **Cleverwolf7**, **Aedus**, **Ryoga_P_Chan**, **mahik**, **Mahowrath**, **#!/usr/bin/env tangy**, **Kidze**, **Limpy**, **Kykeon**, **Posey**, **Alpako**, **cthulhug**, **Harri** (layout mockups), **Moss** (grid hybrid), **Slum**, **LordEng1ish**, **Colston**, **Bore**, **bananian**, **The Bee's Knees#4435**, **ReinFórce**, **NoTruePunk**, **Muon**, **DesertRat**, **deine**, **Phayil**, **nirsoXD**, **S-Kill-a**, **vorinvictus**, **Wolta Horo**, **Trasher** (left-handed conversions), **TobyTheKiwi** (370004), **J1mm1ny**, **MicroMacroMarco** (co-op/campaign packs), **Onikoroshi**, **Lady Interstellar**, **zelph** (Ergodox Infinity), **Lv35 Chungus** (Core+ AutoHotkey), **Shrike** (40% ortho), **curiosikey**. **PiG** appears once, asking for AutoHotkey help (772090).
- In spring 2020 several distinct people appear as "Deleted User", so attributions there are unreliable.

## Traffic and mood

- **The mood is patient support, not development, in every era.** Even in the busiest design periods roughly half the volume is one-on-one onboarding, and there is very little pure chat.
- **2019-08 to 2020-01:** anxiety about committing to a moving target — which beta, whether to switch now, spreadsheet or file — plus German, AZERTY, Russian and UK users making a US-QWERTY file work (885279, 603864, 555723).
- **2020-01 to 2020-05:** an even split between newcomers announcing a switch, people asking why a bind is where it is, and modifier remapping ("TheCore+", "core plus") done outside the game with AutoHotkey or SharpKeys. Two-thirds onboarding, the rest design rationale and hardware.
- **2020-05 to 2020-10:** almost no design work, 6.0 being finished. Instead, arguments over how many control groups and cameras earn their keyboard real estate, where cameras go for Protoss warp-ins, and how the thumb sits on the modifiers — plus bug reports against the shipped `.SC2Hotkeys` files and localization breakage.
- **2020-10 to 2021-10:** onboarding dominates (download location, two keys arriving unbound, misbehaving camera binds, learning time, what keyboard to buy), with a second strand auditing shipped files against the spreadsheets. Ergo boards a minority interest.
- **2021-10 to 2022-09:** the same, plus people discovering campaign, co-op or arcade modes corrupted their multiplayer binds; the tone shifts to explaining nothing will be fixed because nobody has edit rights.
- **2022-09 to 2023-11:** almost entirely onboarding plus customization from people six months to two years in. By volume: which version and where the file goes; camera binds, the most argued point; national keyboards and OS key interception; the 2023-09 balance patch; custom split-keyboard design.
- **2023-11 to 2026-08:** newcomers with one specific blocker, plus "is there a Core for game X?" and "can I use TheCore on this weird hardware". In 2025-26 roughly half is install/config support, a quarter hardware (60% boards, split ergo, gamepads), the rest layout theory, learning-curve reports, and two Blizzard patches that broke binds. Answers increasingly point at links.

## What the distillation does not cover

**The largest structural gap is that the load-bearing artifacts are mostly not text.** Files, layout images, finger diagrams and keyboard photos live in Discord attachments and in channels outside this capture, so anything that lived only in an image or only in the files channel is unrecoverable.

### File contents and syntax

- **No complete `.SC2Hotkeys` file is quoted anywhere**, and whole stretches show no file lines at all: 2020-05-19..06-03, 2020-06-03..06-17, 2020-07-27..08-20 and 2020-09-18..10-27 discuss every bind by key name or editor-UI name and never show a `Command=Key` line. Files lived in `#440141641907437570`, the changelog in `#651526731517132839` (788576, 130463).
- No `Hotkey=` syntax, no `[Settings]` or inherit-file mechanics, no account of how alternates are written. No install path (`Documents\StarCraft II\...` or otherwise) and no install instructions beyond "it's in the Drive folder" and "check the pins" (May–June 2020); in early 2020 the file location is assumed known.
- **Rapid fire is named constantly and never explained.** It is "built in to almost everything" (021629) with the syntax never shown; in June 2020 it appears once as a constraint that turned out not to apply to Battery Overcharge (307520, 850396).
- The only adjacent fact on editor-versus-file capability is the reverse of what you want: the game refuses to let Ctrl and Shift trade roles, which is why "plus" happens outside the game (054506). No multi-command binds appear. In 2021 only individual `Command=Key` lines are quoted, never the header or section format; in 2023 the format is again undocumented, with one example of appending a key to a line (692856). The one exception in early 2020 is the broken `Control+sC` / `Control+comma` control group 9 bind (942420, 945216); every other edit is prose. See [hotkey-file-editing](/hotkey-file-editing.md).

### Missing attachments and images

- 2019-08..2020-01: SPARROW's shifted layout (228608), JaKaTaK's finger picture (604608).
- 2020-03-31..05-19: the official home-keys image (125632), the camera mind map (300148), Siaal's converted Spanish, Colemak and other 6g files (382813, 067478, 976937).
- 2020-05-19..06-03: J1mm1ny's control-group list (567972), Sora's settings screenshot (204928), MicroMacroMarco's co-op and campaign packs (634218, 596365), Onikoroshi's missing-hotkeys screenshot (564550), carlitos_mit_Auto's spreadsheet screenshot (278170). Marco's packs are never vetted (060378) and the strawpoll's race results are never posted.
- 2020-06-03..06-17: 049600, 217330, 960852, 940334, plus the "second pin" the camera answers refer to.
- 2020-07-27..08-20: the pinned home-key image, so the 6.0 home keys are only as described by Sora and JaKaTaK, who differ on whether `P` counts.
- 2020-08-20..09-18: the build-key finger diagram, popped-keycap variants, hand-position and rotation photos; "top" versus "bottom" keycap pull (859868) is unrecoverable from text.
- 2021-10..2022-05: the layout diagrams and keyboard photos that carry the argument (127781, 665876, 306344) — reasoning survives, images do not.
- 2023-11..2024-08: DeathDealer's per-race graphics, the v6 key-zone image Edennil cites for assignment order (805716, 866612), JuicyJuuce's UK keyboard photos, Laaxus's screenshots.
- 2024-08..2026-08: the ergo-setup and inject-method pinned posts, present only as Discord links (795450, 765644).
- Throughout 2020-10..2021-03 attachments appear as `<1 attachment(s)>` with no content, so screenshot answers cannot be reconstructed.

### Links, downloads and install paths

- **No download URLs anywhere in 2020.** Files come from a Google Drive linked through a channel reference and from pins, neither appearing as a URL (Poletes 894386, Sora 769236, 895666). No links for the GitHub repo, converter or visualizer, though all are recommended. In 2020-08..09 the website, layout files, "The Course" and handbook are cited constantly and never linked; only the "core considerations" doc has a URL. What could be salvaged is in [links](/links.md).
- **No macOS or Linux install recipe.** The one X11 Core+ request went unanswered (177152); mid-2020 Mac advice is to use Boot Camp instead (888998); later Mac threads (Magic Keyboard, Karabiner) assume the reader knows the Mac file locations, and Sebastian's German-on-Mac key mismatch is never fully diagnosed (930378, 156378). Linux is one Kubuntu locale report (929768) and a Karabiner Elements mention (209439).
- The two onboarding sites under construction in 2024–2026 (993774, 536085) are never shown finished and neither gets a URL.

### Variants, layouts and hardware

- **Nothing on Dvorak.** Colemak appears only as "no file exists" (mid-2020), "converted but untested" (646869, Siaal 268628), and two users running it with nobody addressing whether TheCore's finger-alternation logic survives translation (512666, 863844). The layout discussion is entirely national QWERTY/QWERTZ variants.
- **No v6 files existed for AZERTY, German or UK as of 2020-01-26**; SPARROW maintained AZERTY for v5 only (235010). Left-handed and hand-size variants are as thin: no left-handed v6 in early 2020, none in 2020-08..09 even though the generator takes QWERTY right or left as input, and nothing on medium or large hands beyond those variants being dropped after version 3.
- **TheCore Lite is praised constantly and never described.** No keymap, no link, no account of how it differs beyond "that side of the keyboard"; in mid-2020 it appears only as a note that ESChamp uses it (Poletes 543794) and twice more in passing with no recommendations (763908, 953012). Requests for a Lite control group guide and a Lite visual layout went unanswered (985482, 856465); nobody in 2020-09..10 runs it and its channel is dead (711355); in 2021 nothing beyond the Halt/Lift collision and "made for laptops"; it is named a supported variant and a stepping stone (490452, 713725) with no key assignments; whether it is still maintained went unanswered in 2023 (524969), and the claim that a 2023-10 patch broke it was disputed, not resolved (497768 vs 306154).
- **Version names are never defined.** "6g", "6G", "6h" and "6y" all appear as current-version labels with no statement of what distinguishes them (723540, 969020, 881931, 634266); Poletes says he uses "something totally different from 6g" without describing it (723540).
- **Ergonomic and split boards are largely absent before 2022.** Early 2020 has only Edennil naming his Redox (638722) with no QMK keymap, layer or ortholinear detail; several months-long stretches of 2020–2022 have none, and hardware talk there is conventional 60%, 65%, 1800, full-size, TKL, Ducky One/One 2, SteelSeries Apex Pro and the Niz Plum. Nobody posts a QMK keymap despite Poletes offering to (196294), and Edennil's promised Redox/QMK writeup (829639) never appears. No keypads or macro pads anywhere; whether a physical Core keypad exists is asked and unanswered. Mice appear only as "you need side buttons for subgroup navigation". No pricing, vendor or build-quality talk. What was said is in [keyboards-and-hardware](/keyboards-and-hardware.md).
- **No tournament or ladder rules on custom layouts or remapping software**, beyond Edennil's remark that you cannot install software at an offline event (981312) and his informal LAN caveat (418482). The only competitive angle is which pros use what (783995).

### Co-op, campaign and other game modes

- 2019-08..2020-01 has no co-op or campaign coverage beyond "6 does not have those binds"; two Mengsk co-op requests (928321, 879631) and one for Terran TheCourse material (521409) got no reply. No co-op/commander mapping existed as of mid-2020 and nobody claimed to be working on one (256707).
- himaji's request for a good 6.0 campaign layout on 2021-10-03 gets no answer (946960). "Where do I find the maps to practice thecore with?" goes unanswered (578756); arcade map names surface only later and incidentally (256539, 790273).
- fprefect's report that "SC2 has removed the core from the Hotkey list and I cant get it to read the Hotkey file once again" gets no reply at all (295764); whether it is the per-game-mode corruption diagnosed elsewhere is unresolved. Mass Recall is unresolved twice: the incompatibility in 2021–2022, and the missing hotkey-file entries in 2024–2026, never enumerated (384242, 657128).

### Threads that end without an answer

- **2019-08..2020-01:** the finger-split/tap redesign, the Zerg-versus-Terran modifier-layer conflict, the pinky-load complaint. No opening sequence for version 6 exists in the handbook or channel; JaKaTaK's own is "still pretty meh for me atm" (869929, 944790).
- **2020-01-07..01-26:** the spontaneous hotkey-profile merging bug, never diagnosed (122431, 056320); "why don't my fingers return to base home position?" (880001, 090433); a request for a split, quiet, wireless mechanical keyboard (243657, 090380). v7 is named once (061646) with no scope or timing.
- **2020-01-26..03-31:** goldsteal's German AltGr and E1 driver problems (905, 910, 911, 924) and the full list of correct UK binds for version 6 (533574).
- **2020-03-31..05-19:** the alt center-on-selection debate, camera recall on 9/8/U versus 0/9/8, the spine/spore uproot key, race-specific versions, zeky_85's rapid-fire inject workaround, and the period's one substantive Terran question — accidental anti-armor missile, EMP and tactical jump when trying to stim, and whether to move spellcaster spells off `J` to `[` — which got no reply (646332). The v5 control-group-9 bug is discussed in a channel not captured (NReilingh 602901).
- **2020-06..10:** Mothership-recall-on-K and the ping placement question end without replies; whether Poletes' seven optimizations (024499) reached the downloadable files or the spreadsheet is unresolved, and later "unbound" reports suggest they had not; the Scandinavian and Swiss right-hand converter bug is open at 2020-07-27 (595250), still diagnosed-but-unfixed in 2020-10, and jaydik's planned Linux VM investigation never reports back (996555). Pokebunny's outcome is unknown (309150) and his `IOHN` macro layout was provisional.
- **2020-10..2021-03:** no Blizzard patch is reported as breaking hotkey files; the one suspected case was failing hardware (867018).
- **2021-03..10:** the Method A / Method B egg-hotkeying comparison ends unsettled; bunfoof's discrepancy list is never resolved and no corrected file posted; the Razer TKL apostrophe-to-grave bug and the April AutoHotkey breakage both end without a confirmed root cause.
- **2021-10..2022-05:** the German-locale `Attack=Grave` / `Attack=SemiColon` discrepancy, NoTruePunk's AltGr+M bind failure and input delay, the fast-reload question, the Mass Recall incompatibility.
- **2022-05..09:** the known file errors — Unburrow `-` vs `]`, Mothership Recall, swarm host unburrow, UK Starport — are unfixed at the end of that period, and where to report file errors is never established (159037).
- **2022-09..2023-03:** the scroll-wheel token, conversion-script bug, siege/unsiege shared-key and triple-modifier failure questions. The GitHub landing page, FAQ revamp and Bose's proposed "what matters most" writeup are proposed here and none is shown completed.
- **2023-11..2024-08:** the UK QWERTY unbound-keys bug is diagnosed but not fixed and Mahowrath's amended keyset was requested and never posted; the robo/disruptor `k` finger-rule violation is left open; Edennil's three-finger-control-group design question got zero replies; the two reports on Blizzard's cloud file restore contradict each other.
- **2024-08..2026-08:** Beyond All Reason and ZeroSpace ports are proposed but no layout or file produced (835123, 238044); the 5.0.14 and June 2026 rebind lists are US QWERTY only, other language variants promised but the keys not posted (143956, 456007).
- The contested items are carried in [open-questions](/open-questions.md).

### Project direction

- **No release happens after 6.0 anywhere in the capture.** The proposed "6h" fixup (402718) and v7 (016239) are talk only, and no new official file beyond Juuce 1.2.2 appears in 2023–2024; anyone reading this for "what changed" after 2020 finds only the Juuce rebuilds and Blizzard's patch damage.
- Edennil states the intent to migrate the Drive to GitHub and reorganize the Discord (334598, 368124), then goes on vacation and gets sick; there is no resolution on the migration, the reorganization or a v7.0.
- The Drive documents and spreadsheet are repeatedly called wrong, but only a few errors are named — suggested cameras, the roach `.` inject, the missing next-subgroup entry, camera 8 not being settable with Alt, the missing 6.01 label. There is no complete errata list.
- **The FAQ channel's contents are not reproduced in this capture**, though Edennil and Mell00yell00 keep redirecting to it (105764, 164078). What was answered in #general itself is in [faq](/faq.md).
- No first-hand JaKaTaK design commentary exists after 2022; by 2025-26 he is a mentioned cameo (866360).
- No figures on learning time beyond "a couple of hours" worse at the start and "a couple of weeks" to switch later (171153); see [learning-and-practice](/learning-and-practice.md).

### Citation caveats

- Six-digit suffixes are not unique: 212861 is two different Poletes messages in 2020-08..09.
- Several ids in the early-2020 goldsteal thread appear in the source with fewer than six digits (905, 910, 911, 924), as do the Remko `K`/`H` exchange ids (781, 782-789); they are reproduced as they appear in the export.
- Poletes' identification as "Vae"/"VaeVictus" is an inference from JaKaTaK addressing him so (919146), not stated outright, and "bro" is separately called "vae" in the same period.
