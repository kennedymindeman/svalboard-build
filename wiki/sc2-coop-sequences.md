---
type: Reference
title: SC2 co-op command sequences, measured
description: Command frequencies, control-group use and event sequences measured from 943 StarCraft II Co-op speedrun replays, one set of numbers per commander.
tags: [starcraft, thecore, gaming, measurement, hotkeys, coop]
source: "starcraft2coop.com co-op speedrun archive; measured with tools/sc2_sequences.py"
---

# SC2 co-op command sequences, measured

The companion to [SC2 command sequences, measured](sc2-command-sequences.md), which measures 1v1 pro play. This page measures **Co-op Commanders** instead: 943 replays, 1089 player-games, 18 commanders, 13,806 minutes played. Co-op is where a hotkey layout is stressed differently: every commander has its own calldowns and top-bar abilities on top of the melee kit.

## Where the replays come from

The set is the community **co-op speedrun archive**: the replays behind the clear-time leaderboards on [starcraft2coop.com](https://starcraft2coop.com/), kept in the public Google Drive folder [0B0kAPEv3WqAeZlhmbzN5NWlDc1E](https://drive.google.com/drive/folders/0B0kAPEv3WqAeZlhmbzN5NWlDc1E), one directory per commander (`Dehaka Solo`, `Alarak-Co-Op`, ...). These are record attempts, not average games, so read every rate as the fast end of what a player does, not the median.

The archive is old and wide: 59 distinct game builds, 3.13.0.52910 to 5.0.15.95841. `replays/README.md` says how to fetch it and where it lives locally.

## What is counted

Definitions (command, control-group action, camera jump, sequence pair, the TheCore projection) are the ones on the [1v1 page](sc2-command-sequences.md#what-is-counted), with three co-op-specific points:

- **Who is a player.** A co-op replay has two player slots and a pile of Amon computer players. Human players are the ones with a commander; `replay.cooperative` is not used, because it is 0 on plenty of these replays. In a two-human run each player is counted under their own commander, so one replay can feed two commanders' numbers.
- **Hex-id tokens.** sc2reader has no name for many commander-specific abilities, so about 31.5% of commands here arrive as a numeric ability id, written `ability:0x....`. They are kept verbatim rather than dropped: the id is stable inside a build, so it counts and sequences correctly, and only the label is missing. Because the archive spans 59 builds, the same id can mean different abilities in different years — treat a hex token as a within-commander shape, not a name.
- **Camera hotkeys are invisible.** A replay records where the camera went, never which key sent it there, and co-op players lean on camera hotkeys and the minimap hard. The camera-jump counts below are an upper bound on camera hotkey presses, and no camera key appears in the sequences at all, so the real same-finger load is higher than the numbers here.

## Commanders

The archive holds 977 replay files. 33 are byte-identical duplicates of another file (the same run saved under two names) and are skipped, keeping the first path alphabetically; 1 is misfiled (a Mengsk + Raynor run sitting in `Zagara Solo/`, which names no commander either player plays) and is skipped as unattributable. All 943 remaining replays parsed with sc2reader 1.9.0 at `load_level=4`; none failed.

| Commander | Replays | Player-games | Players | Minutes | Commands | Commands/min | CG actions/min | Camera jumps/min | Distinct abilities | Hex-id share | On a TheCore key |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dehaka | 158 | 158 | 16 | 1727 | 69321 | 40.1 | 21.78 | 10.3 | 506 | 46.2% | 17.7% |
| Abathur | 90 | 90 | 13 | 844 | 22446 | 26.6 | 29.64 | 10.91 | 171 | 21.1% | 35.3% |
| Zagara | 72 | 72 | 19 | 1003 | 31891 | 31.8 | 22.89 | 8.85 | 196 | 24.9% | 38.2% |
| Alarak | 68 | 68 | 11 | 869 | 36486 | 42.0 | 25.11 | 8.59 | 138 | 29.5% | 35.6% |
| Artanis | 61 | 61 | 16 | 913 | 26957 | 29.5 | 14.08 | 10.05 | 131 | 14.6% | 47.5% |
| Swann | 57 | 57 | 8 | 816 | 37812 | 46.3 | 25.09 | 11.69 | 192 | 18.7% | 37.2% |
| Tychus | 57 | 57 | 5 | 797 | 28997 | 36.4 | 15.82 | 9.51 | 216 | 33.0% | 34.3% |
| Han & Horner | 55 | 55 | 9 | 731 | 23673 | 32.4 | 12.96 | 9.01 | 249 | 42.5% | 29.6% |
| Zeratul | 54 | 54 | 13 | 551 | 22943 | 41.6 | 17.51 | 9.61 | 196 | 35.7% | 16.0% |
| Fenix | 53 | 53 | 10 | 637 | 26734 | 41.9 | 21.63 | 9.52 | 190 | 19.2% | 45.2% |
| Nova | 52 | 52 | 12 | 723 | 25176 | 34.8 | 17.83 | 7.72 | 259 | 44.0% | 20.7% |
| Stetmann | 52 | 52 | 3 | 696 | 31211 | 44.9 | 23.07 | 6.82 | 204 | 45.3% | 18.8% |
| Kerrigan | 51 | 51 | 8 | 629 | 24314 | 38.6 | 25.72 | 10.65 | 166 | 32.6% | 28.6% |
| Mengsk | 48 | 48 | 6 | 590 | 25760 | 43.7 | 22.47 | 6.22 | 213 | 40.5% | 21.6% |
| Karax | 45 | 45 | 7 | 691 | 25172 | 36.4 | 14.48 | 8.55 | 119 | 26.3% | 41.7% |
| Stukov | 45 | 45 | 4 | 618 | 20926 | 33.9 | 18.68 | 8.08 | 164 | 33.8% | 23.6% |
| Vorazun | 45 | 45 | 14 | 615 | 17853 | 29.0 | 20.12 | 10.81 | 151 | 18.1% | 44.4% |
| Raynor | 26 | 26 | 5 | 356 | 15922 | 44.7 | 75.88 | 11.44 | 199 | 10.5% | 47.0% |

Control-group load is the number that varies most, and not with command rate: Raynor runs 75.88 control-group actions a minute (mostly recalls, on 356 minutes of play) against Han & Horner's 12.96. That spread may be the runner rather than the commander. The "Players" column counts the distinct handles behind the player-games, and the counts are small: Raynor's 26 player-games come from 5 players and Han & Horner's 55 from 9, with two or three runners holding a large share of the rows in every commander. Per-player rates inside one commander are about as spread out as the rates between commanders, so each row describes a handful of record holders at least as much as it describes the commander.

"On a TheCore key" uses only the bindings the hotkey file gives that commander (its own units, its race's melee units, and the global commands), so it is a fair per-commander coverage figure. The rest of each commander's commands are three things: right-clicks, which are a mouse action and no layout's business (36.1% of all commands here); hex-id commands, which have no name to look up (31.5%); and named commands the hotkey file does not bind (1.4%). Right-clicks are the largest of the three for 11 of the 18 commanders, so most of the gap is the mouse, not the missing names.

### Dehaka

158 replays, 158 player-games, 1727 minutes, 69321 commands: **40.1 commands per minute** (438.7 per game). 21.78 control-group actions and 10.3 camera jumps per minute. 46.2% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 14.51 | 36.13% |
| 2 | Attack | 6.07 | 15.13% |
| 3 | ability:0x11400 | 2.03 | 5.07% |
| 4 | ability:0x11300 | 1.5 | 3.73% |
| 5 | ability:0x113A0 | 1.15 | 2.85% |
| 6 | ability:0x11220 | 1.14 | 2.83% |
| 7 | ability:0x112A0 | 0.71 | 1.78% |
| 8 | ability:0x111C0 | 0.7 | 1.75% |
| 9 | ability:0x160A0 | 0.6 | 1.5% |
| 10 | HoldPosition | 0.59 | 1.47% |
| 11 | ability:0x11120 | 0.46 | 1.14% |
| 12 | ability:0x16420 | 0.44 | 1.08% |
| 13 | Stop | 0.34 | 0.84% |
| 14 | ability:0x11200 | 0.33 | 0.83% |
| 15 | ability:0x112C0 | 0.31 | 0.78% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.057 | 0 | 0 | 0.702 |
| 1 | 0.15 | 0.005 | 0.002 | 8.473 |
| 2 | 0.176 | 0.024 | 0.001 | 1.666 |
| 3 | 0.122 | 0.084 | 0.002 | 2.475 |
| 4 | 0.119 | 0.022 | 0 | 4.238 |
| 5 | 0.131 | 0.018 | 0.001 | 2.048 |
| 6 | 0.027 | 0.003 | 0 | 0.082 |
| 7 | 0.001 | 0 | 0 | 0 |
| 8 | 0.035 | 0 | 0.001 | 0.308 |
| 9 | 0.046 | 0.004 | 0 | 0.751 |
| all | 0.86 | 0.16 | 0.01 | 20.74 |

Busiest TheCore keys (of the 45.7% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| O | middle | 8.47 |
| P | index | 6.08 |
| K | ring | 4.24 |
| L | middle | 2.48 |
| 9 | middle | 2.05 |
| I | ring | 1.67 |
| Comma | ring | 0.75 |
| Period | middle | 0.7 |
| BracketClose | index | 0.59 |
| G | pinky | 0.34 |

Top pairs within 1s (43.0 per minute over 74175 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG1 > RightClick | 4271 | 27.03 |
| 2 | RightClick > Attack | 2460 | 15.57 |
| 3 | Attack > RightClick | 1985 | 12.56 |
| 4 | ability:0x11400 > RightClick | 1464 | 9.27 |
| 5 | RightClick > CG1 | 1461 | 9.25 |
| 6 | CG1 > CG5 | 1278 | 8.09 |
| 7 | Attack > CG1 | 1266 | 8.01 |
| 8 | CG1 > Attack | 1239 | 7.84 |
| 9 | CG1 > CG4 | 1181 | 7.47 |
| 10 | ability:0x11300 > RightClick | 1172 | 7.42 |
| 11 | CG4 > CG1 | 1158 | 7.33 |
| 12 | ability:0x11220 > RightClick | 1034 | 6.54 |

Same finger on the next key: **23.8%** of the 19210 pairs where both events map to a key. Of those same pairs, 8.1% are the same key twice (a repeat no layout can move apart) and **15.7% are the same finger on a different key**.

### Abathur

90 replays, 90 player-games, 844 minutes, 22446 commands: **26.6 commands per minute** (249.4 per game). 29.64 control-group actions and 10.91 camera jumps per minute. 21.1% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 11.37 | 42.76% |
| 2 | Attack | 5.45 | 20.49% |
| 3 | MorphDrone | 0.86 | 3.22% |
| 4 | ability:0x12060 | 0.75 | 2.83% |
| 5 | MorphMutalisk | 0.7 | 2.63% |
| 6 | HoldPosition | 0.57 | 2.13% |
| 7 | ability:0x11E00 | 0.49 | 1.86% |
| 8 | MorphOverlord | 0.48 | 1.82% |
| 9 | ability:0x11F20 | 0.36 | 1.34% |
| 10 | ability:0x143A0 | 0.31 | 1.15% |
| 11 | ability:0x14740 | 0.29 | 1.09% |
| 12 | ability:0x11C60 | 0.27 | 1.03% |
| 13 | ability:0x14540 | 0.2 | 0.75% |
| 14 | ability:0x11D00 | 0.19 | 0.72% |
| 15 | ability:0x14720 | 0.19 | 0.71% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.07 | 0.002 | 0 | 0.72 |
| 1 | 0.417 | 0.21 | 0.083 | 2.993 |
| 2 | 0.355 | 0.073 | 0.059 | 7.119 |
| 3 | 0.323 | 0.028 | 0.013 | 5.609 |
| 4 | 0.045 | 0.007 | 0.006 | 1.887 |
| 5 | 0.06 | 0 | 0.005 | 7.842 |
| 6 | 0.004 | 0 | 0.011 | 0.267 |
| 7 | 0.001 | 0.001 | 0 | 0.039 |
| 8 | 0.012 | 0.017 | 0.027 | 0.258 |
| 9 | 0.013 | 0.026 | 0.049 | 0.924 |
| all | 1.3 | 0.36 | 0.25 | 27.66 |

Busiest TheCore keys (of the 68.3% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| 9 | middle | 7.84 |
| I | ring | 7.12 |
| L | middle | 5.61 |
| P | index | 5.57 |
| O | middle | 2.99 |
| K | ring | 1.89 |
| Minus | index | 0.93 |
| Comma | ring | 0.92 |
| SemiColon | index | 0.77 |
| Period | middle | 0.72 |

Top pairs within 1s (37.0 per minute over 31270 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG3 > CG5 | 3306 | 36.73 |
| 2 | CG5 > CG2 | 2779 | 30.88 |
| 3 | CG2 > CG5 | 2553 | 28.37 |
| 4 | CG5 > CG3 | 2141 | 23.79 |
| 5 | RightClick > Attack | 1570 | 17.44 |
| 6 | Attack > RightClick | 989 | 10.99 |
| 7 | CG2 > RightClick | 943 | 10.48 |
| 8 | RightClick > RightClick | 709 | 7.88 |
| 9 | CG1 > RightClick | 517 | 5.74 |
| 10 | RightClick > CG2 | 487 | 5.41 |
| 11 | CG3 > RightClick | 405 | 4.5 |
| 12 | RightClick > CG1 | 395 | 4.39 |

Same finger on the next key: **36.1%** of the 18201 pairs where both events map to a key. Of those same pairs, 2.4% are the same key twice (a repeat no layout can move apart) and **33.7% are the same finger on a different key**.

### Zagara

72 replays, 72 player-games, 1003 minutes, 31891 commands: **31.8 commands per minute** (442.9 per game). 22.89 control-group actions and 8.85 camera jumps per minute. 24.9% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 11.21 | 35.24% |
| 2 | Attack | 8.46 | 26.61% |
| 3 | MorphDrone | 1.02 | 3.2% |
| 4 | ability:0x10DE0 | 1.02 | 3.2% |
| 5 | ability:0x10E40 | 0.85 | 2.67% |
| 6 | ability:0x6BA0 | 0.74 | 2.33% |
| 7 | ability:0x10DA0 | 0.64 | 2.0% |
| 8 | MorphOverlord | 0.59 | 1.84% |
| 9 | ability:0x10D40 | 0.55 | 1.73% |
| 10 | ability:0x110C0 | 0.4 | 1.26% |
| 11 | ability:0x6A80 | 0.3 | 0.95% |
| 12 | BuildHatchery | 0.25 | 0.78% |
| 13 | ability:0x76FD | 0.24 | 0.76% |
| 14 | ability:0x6B60 | 0.23 | 0.74% |
| 15 | BuildExtractor | 0.2 | 0.63% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.075 | 0.006 | 0.001 | 0.293 |
| 1 | 0.182 | 2.572 | 0 | 5.248 |
| 2 | 0.223 | 0.034 | 0.033 | 2.366 |
| 3 | 0.06 | 0.02 | 0.006 | 0.355 |
| 4 | 0.164 | 0.14 | 0.001 | 10.025 |
| 5 | 0.074 | 0.012 | 0.001 | 0.645 |
| 6 | 0.015 | 0.01 | 0.001 | 0.203 |
| 7 | 0.009 | 0 | 0.002 | 0.015 |
| 8 | 0.007 | 0 | 0.001 | 0.016 |
| 9 | 0.035 | 0.004 | 0 | 0.026 |
| all | 0.84 | 2.8 | 0.05 | 19.19 |

Busiest TheCore keys (of the 61.5% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| K | ring | 10.03 |
| P | index | 8.63 |
| O | middle | 5.25 |
| I | ring | 2.37 |
| Minus | index | 1.27 |
| SemiColon | index | 0.93 |
| 9 | middle | 0.65 |
| Apostrophe | index | 0.43 |
| L | middle | 0.35 |
| Period | middle | 0.29 |

Top pairs within 1s (32.2 per minute over 32295 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 2266 | 31.47 |
| 2 | Attack > RightClick | 1494 | 20.75 |
| 3 | CG4 > CG4 | 1478 | 20.53 |
| 4 | Attack > CG4 | 1354 | 18.81 |
| 5 | CG4 > RightClick | 1351 | 18.76 |
| 6 | CG1 > RightClick | 1234 | 17.14 |
| 7 | CG1 > CG4 | 1020 | 14.17 |
| 8 | RightClick > CG4 | 843 | 11.71 |
| 9 | CG4 > CG1 | 815 | 11.32 |
| 10 | Attack > CG1 | 699 | 9.71 |
| 11 | CG4 > CG2 | 674 | 9.36 |
| 12 | CG2 > CG4 | 613 | 8.51 |

Same finger on the next key: **29.4%** of the 13074 pairs where both events map to a key. Of those same pairs, 17.0% are the same key twice (a repeat no layout can move apart) and **12.3% are the same finger on a different key**.

### Alarak

68 replays, 68 player-games, 869 minutes, 36486 commands: **42.0 commands per minute** (536.6 per game). 25.11 control-group actions and 8.59 camera jumps per minute. 29.5% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 14.55 | 34.64% |
| 2 | Attack | 10.82 | 25.76% |
| 3 | ability:0x101A0 | 2.95 | 7.01% |
| 4 | ability:0x11F60 | 1.83 | 4.37% |
| 5 | ability:0x11C4E | 1.46 | 3.47% |
| 6 | BuildPylon | 1.38 | 3.28% |
| 7 | TrainProbe | 1.09 | 2.6% |
| 8 | ability:0x10120 | 0.91 | 2.16% |
| 9 | ability:0x11DA0 | 0.72 | 1.72% |
| 10 | ability:0x10160 | 0.45 | 1.06% |
| 11 | ability:0x15080 | 0.39 | 0.93% |
| 12 | ability:0x11DE0 | 0.3 | 0.72% |
| 13 | ability:0x118C0 | 0.28 | 0.67% |
| 14 | ability:0x1ACA | 0.25 | 0.61% |
| 15 | BuildAssimilator | 0.22 | 0.53% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.033 | 0.002 | 0 | 0.21 |
| 1 | 0.196 | 1.447 | 0.006 | 11.069 |
| 2 | 0.345 | 0.086 | 0.005 | 4.139 |
| 3 | 0.091 | 0.015 | 0.006 | 3.76 |
| 4 | 0.059 | 0.014 | 0.002 | 2.033 |
| 5 | 0.024 | 0 | 0 | 0.84 |
| 6 | 0.035 | 0 | 0 | 0.16 |
| 7 | 0.003 | 0.003 | 0 | 0.079 |
| 8 | 0.003 | 0.006 | 0.002 | 0.227 |
| 9 | 0.014 | 0.015 | 0 | 0.175 |
| all | 0.8 | 1.59 | 0.02 | 22.69 |

Busiest TheCore keys (of the 58.2% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| O | middle | 11.07 |
| P | index | 10.89 |
| I | ring | 4.14 |
| L | middle | 3.76 |
| K | ring | 2.03 |
| SemiColon | index | 1.43 |
| Minus | index | 1.36 |
| 9 | middle | 0.84 |
| BracketOpen | index | 0.42 |
| U | pinky | 0.23 |

Top pairs within 1s (47.4 per minute over 41164 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 2516 | 37.0 |
| 2 | CG1 > Attack | 2277 | 33.49 |
| 3 | Attack > RightClick | 1863 | 27.4 |
| 4 | CG1 > CG1 | 1570 | 23.09 |
| 5 | Attack > CG1 | 1407 | 20.69 |
| 6 | CG3 > RightClick | 1305 | 19.19 |
| 7 | CG1 > RightClick | 1299 | 19.1 |
| 8 | RightClick > CG1 | 1232 | 18.12 |
| 9 | Attack > CG3 | 1226 | 18.03 |
| 10 | CG2 > RightClick | 928 | 13.65 |
| 11 | ability:0x101A0 > Attack | 891 | 13.1 |
| 12 | ability:0x11F60 > ability:0x101A0 | 816 | 12.0 |

Same finger on the next key: **29.3%** of the 14077 pairs where both events map to a key. Of those same pairs, 15.1% are the same key twice (a repeat no layout can move apart) and **14.1% are the same finger on a different key**.

### Artanis

61 replays, 61 player-games, 913 minutes, 26957 commands: **29.5 commands per minute** (441.9 per game). 14.08 control-group actions and 10.05 camera jumps per minute. 14.6% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 10.92 | 37.0% |
| 2 | Attack | 8.5 | 28.81% |
| 3 | TrainProbe | 1.45 | 4.92% |
| 4 | WarpInStalker | 1.27 | 4.31% |
| 5 | WarpInZealot | 0.84 | 2.85% |
| 6 | ability:0xDDE0 | 0.53 | 1.81% |
| 7 | Stop | 0.31 | 1.05% |
| 8 | HoldPosition | 0.31 | 1.04% |
| 9 | ability:0xF3A0 | 0.29 | 1.0% |
| 10 | ability:0xF3C0 | 0.29 | 0.98% |
| 11 | ability:0xD229 | 0.25 | 0.85% |
| 12 | ability:0xAA00 | 0.25 | 0.84% |
| 13 | BuildPhotonCannon | 0.23 | 0.79% |
| 14 | ability:0xDD80 | 0.23 | 0.78% |
| 15 | BuildAssimilator | 0.23 | 0.78% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.011 | 0.027 | 0 | 0.23 |
| 1 | 0.695 | 0.477 | 0.003 | 4.246 |
| 2 | 0.379 | 0.045 | 0.001 | 2.297 |
| 3 | 0.081 | 0.018 | 0.027 | 0.744 |
| 4 | 0.104 | 0.024 | 0.001 | 1.866 |
| 5 | 0.064 | 0.007 | 0 | 0.758 |
| 6 | 0.076 | 0.005 | 0 | 1.565 |
| 7 | 0 | 0.001 | 0 | 0 |
| 8 | 0.002 | 0.013 | 0 | 0.025 |
| 9 | 0.012 | 0.035 | 0 | 0.239 |
| all | 1.42 | 0.65 | 0.03 | 11.97 |

Busiest TheCore keys (of the 62.6% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 9.66 |
| O | middle | 4.25 |
| Minus | index | 2.87 |
| I | ring | 2.3 |
| K | ring | 1.87 |
| 0 | index | 1.56 |
| 9 | middle | 0.76 |
| L | middle | 0.74 |
| G | pinky | 0.31 |
| BracketClose | index | 0.31 |

Top pairs within 1s (24.9 per minute over 22782 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 3610 | 59.18 |
| 2 | Attack > RightClick | 2312 | 37.9 |
| 3 | CG1 > Attack | 1084 | 17.77 |
| 4 | CG1 > RightClick | 558 | 9.15 |
| 5 | Attack > CG1 | 547 | 8.97 |
| 6 | CG4 > WarpInStalker | 515 | 8.44 |
| 7 | RightClick > CG1 | 505 | 8.28 |
| 8 | CG2 > RightClick | 442 | 7.25 |
| 9 | CG5 > CG6 | 391 | 6.41 |
| 10 | Attack > CG2 | 382 | 6.26 |
| 11 | CG6 > CG5 | 317 | 5.2 |
| 12 | RightClick > RightClick | 270 | 4.43 |

Same finger on the next key: **21.6%** of the 8579 pairs where both events map to a key. Of those same pairs, 12.4% are the same key twice (a repeat no layout can move apart) and **9.3% are the same finger on a different key**.

### Swann

57 replays, 57 player-games, 816 minutes, 37812 commands: **46.3 commands per minute** (663.4 per game). 25.09 control-group actions and 11.69 camera jumps per minute. 18.7% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 19.58 | 42.26% |
| 2 | Attack | 10.0 | 21.59% |
| 3 | TrainSCV | 2.21 | 4.78% |
| 4 | HoldPosition | 0.96 | 2.07% |
| 5 | BuildSupplyDepot | 0.91 | 1.97% |
| 6 | ability:0x2FA2 | 0.85 | 1.83% |
| 7 | ability:0x1467 | 0.82 | 1.76% |
| 8 | ScanMove | 0.71 | 1.54% |
| 9 | ability:0x125C0 | 0.61 | 1.32% |
| 10 | ability:0x1073 | 0.6 | 1.29% |
| 11 | ability:0x3BC0 | 0.51 | 1.11% |
| 12 | BuildBattleHellion | 0.37 | 0.8% |
| 13 | ability:0x1402 | 0.35 | 0.76% |
| 14 | SiegeMode | 0.34 | 0.72% |
| 15 | LowerSupplyDepot | 0.31 | 0.67% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.061 | 0.001 | 0 | 0.385 |
| 1 | 0.262 | 1.315 | 0 | 7.322 |
| 2 | 0.349 | 0.053 | 0 | 3.047 |
| 3 | 0.124 | 0.021 | 0 | 2.588 |
| 4 | 0.097 | 0.028 | 0 | 4.808 |
| 5 | 0.158 | 0.001 | 0 | 2.317 |
| 6 | 0.049 | 0 | 0 | 2.044 |
| 7 | 0.012 | 0.001 | 0 | 0.009 |
| 8 | 0.004 | 0 | 0 | 0 |
| 9 | 0.027 | 0 | 0 | 0.004 |
| all | 1.14 | 1.42 | 0 | 22.52 |

Busiest TheCore keys (of the 57.7% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 10.85 |
| O | middle | 7.32 |
| K | ring | 4.81 |
| I | ring | 3.05 |
| L | middle | 2.59 |
| Minus | index | 2.38 |
| 9 | middle | 2.32 |
| 0 | index | 2.04 |
| SemiColon | index | 1.59 |
| BracketClose | index | 0.96 |

Top pairs within 1s (50.8 per minute over 41479 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 4981 | 87.39 |
| 2 | Attack > RightClick | 3519 | 61.74 |
| 3 | CG1 > RightClick | 2242 | 39.33 |
| 4 | Attack > CG1 | 1425 | 25.0 |
| 5 | CG1 > Attack | 1150 | 20.18 |
| 6 | CG3 > RightClick | 1032 | 18.11 |
| 7 | RightClick > CG1 | 808 | 14.18 |
| 8 | RightClick > CG4 | 793 | 13.91 |
| 9 | Attack > CG3 | 763 | 13.39 |
| 10 | CG4 > TrainSCV | 732 | 12.84 |
| 11 | CG1 > CG5 | 714 | 12.53 |
| 12 | RightClick > RightClick | 680 | 11.93 |

Same finger on the next key: **27.3%** of the 13176 pairs where both events map to a key. Of those same pairs, 8.9% are the same key twice (a repeat no layout can move apart) and **18.4% are the same finger on a different key**.

### Tychus

57 replays, 57 player-games, 797 minutes, 28997 commands: **36.4 commands per minute** (508.7 per game). 15.82 control-group actions and 9.51 camera jumps per minute. 33.0% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 11.87 | 32.64% |
| 2 | Attack | 11.57 | 31.8% |
| 3 | ability:0x17F40 | 1.28 | 3.52% |
| 4 | ability:0x18480 | 1.04 | 2.86% |
| 5 | ability:0x18180 | 0.82 | 2.27% |
| 6 | ability:0x18360 | 0.71 | 1.94% |
| 7 | ability:0x18380 | 0.67 | 1.85% |
| 8 | ability:0x18460 | 0.58 | 1.61% |
| 9 | Stop | 0.53 | 1.47% |
| 10 | ability:0x17C60 | 0.51 | 1.41% |
| 11 | ability:0x17C40 | 0.51 | 1.4% |
| 12 | ability:0x18160 | 0.5 | 1.37% |
| 13 | ability:0x184A0 | 0.48 | 1.33% |
| 14 | ability:0x181A0 | 0.42 | 1.16% |
| 15 | ability:0x17F60 | 0.24 | 0.65% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.045 | 0.009 | 0 | 0.168 |
| 1 | 0.049 | 0.004 | 0.089 | 4.866 |
| 2 | 0.093 | 0.004 | 0.006 | 3.002 |
| 3 | 0.151 | 0.004 | 0.004 | 2.499 |
| 4 | 0.144 | 0.039 | 0.004 | 2.545 |
| 5 | 0.088 | 0.011 | 0.01 | 1.331 |
| 6 | 0.011 | 0.064 | 0.003 | 0.413 |
| 7 | 0.005 | 0.005 | 0.004 | 0.028 |
| 8 | 0.01 | 0.019 | 0.001 | 0.025 |
| 9 | 0.044 | 0.004 | 0 | 0.014 |
| all | 0.64 | 0.16 | 0.12 | 14.89 |

Busiest TheCore keys (of the 53.4% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 11.59 |
| O | middle | 4.87 |
| I | ring | 3.0 |
| K | ring | 2.55 |
| L | middle | 2.5 |
| 9 | middle | 1.33 |
| G | pinky | 0.53 |
| 0 | index | 0.41 |
| Period | middle | 0.17 |
| BracketClose | index | 0.12 |

Top pairs within 1s (33.9 per minute over 26994 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 3454 | 60.6 |
| 2 | Attack > RightClick | 1861 | 32.65 |
| 3 | CG1 > Attack | 876 | 15.37 |
| 4 | Attack > CG1 | 770 | 13.51 |
| 5 | CG2 > RightClick | 682 | 11.96 |
| 6 | Attack > CG2 | 638 | 11.19 |
| 7 | RightClick > CG1 | 444 | 7.79 |
| 8 | CG1 > CG3 | 441 | 7.74 |
| 9 | CG1 > RightClick | 431 | 7.56 |
| 10 | CG3 > CG1 | 413 | 7.25 |
| 11 | ability:0x18360 > Attack | 381 | 6.68 |
| 12 | Attack > CG3 | 381 | 6.68 |

Same finger on the next key: **23.3%** of the 7452 pairs where both events map to a key. Of those same pairs, 5.6% are the same key twice (a repeat no layout can move apart) and **17.7% are the same finger on a different key**.

### Han & Horner

55 replays, 55 player-games, 731 minutes, 23673 commands: **32.4 commands per minute** (430.4 per game). 12.96 control-group actions and 9.01 camera jumps per minute. 42.5% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 8.99 | 27.79% |
| 2 | Attack | 8.97 | 27.72% |
| 3 | ability:0x17120 | 1.22 | 3.77% |
| 4 | ability:0x12543 | 1.03 | 3.19% |
| 5 | ability:0x16E20 | 1.0 | 3.08% |
| 6 | ability:0x17060 | 0.81 | 2.49% |
| 7 | ability:0x127E3 | 0.69 | 2.12% |
| 8 | ability:0x170C0 | 0.66 | 2.04% |
| 9 | ability:0x173C0 | 0.66 | 2.03% |
| 10 | ability:0x16D60 | 0.64 | 1.98% |
| 11 | ability:0x127E5 | 0.37 | 1.14% |
| 12 | ability:0x16FE0 | 0.33 | 1.03% |
| 13 | ability:0x12544 | 0.29 | 0.89% |
| 14 | ability:0x12841 | 0.27 | 0.84% |
| 15 | ability:0x125A1 | 0.23 | 0.71% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.031 | 0.008 | 0 | 0.675 |
| 1 | 0.17 | 1.784 | 0.01 | 4.202 |
| 2 | 0.172 | 0.021 | 0.001 | 1.207 |
| 3 | 0.049 | 0 | 0.003 | 0.667 |
| 4 | 0.079 | 0.023 | 0.01 | 3.358 |
| 5 | 0.026 | 0.001 | 0 | 0.312 |
| 6 | 0.048 | 0 | 0 | 0.045 |
| 7 | 0.001 | 0 | 0 | 0.005 |
| 9 | 0.023 | 0.003 | 0 | 0.018 |
| all | 0.6 | 1.84 | 0.02 | 10.49 |

Busiest TheCore keys (of the 46.8% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 8.97 |
| O | middle | 4.2 |
| K | ring | 3.36 |
| I | ring | 1.21 |
| Period | middle | 0.68 |
| L | middle | 0.67 |
| 9 | middle | 0.31 |
| SemiColon | index | 0.21 |
| Slash | index | 0.12 |
| BracketClose | index | 0.11 |

Top pairs within 1s (24.4 per minute over 17858 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1298 | 23.6 |
| 2 | CG1 > Attack | 986 | 17.93 |
| 3 | Attack > RightClick | 917 | 16.67 |
| 4 | CG4 > ability:0x17060 | 397 | 7.22 |
| 5 | CG1 > CG1 | 383 | 6.96 |
| 6 | RightClick > CG1 | 356 | 6.47 |
| 7 | RightClick > CG4 | 343 | 6.24 |
| 8 | RightClick > RightClick | 340 | 6.18 |
| 9 | CG4 > CG0 | 299 | 5.44 |
| 10 | CG0 > CG4 | 294 | 5.35 |
| 11 | Attack > CG1 | 282 | 5.13 |
| 12 | ability:0x12543 > Attack | 281 | 5.11 |

Same finger on the next key: **25.7%** of the 4548 pairs where both events map to a key. Of those same pairs, 13.4% are the same key twice (a repeat no layout can move apart) and **12.2% are the same finger on a different key**.

### Zeratul

54 replays, 54 player-games, 551 minutes, 22943 commands: **41.6 commands per minute** (424.9 per game). 17.51 control-group actions and 9.61 camera jumps per minute. 35.7% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 16.19 | 38.9% |
| 2 | Attack | 4.74 | 11.4% |
| 3 | XelNaga_Caverns_Floating_BridgeNW8 | 3.81 | 9.15% |
| 4 | ability:0x17B40 | 1.61 | 3.87% |
| 5 | ability:0x185C0 | 1.48 | 3.55% |
| 6 | TrainProbe | 1.04 | 2.49% |
| 7 | ability:0x18A60 | 0.97 | 2.32% |
| 8 | ability:0x18761 | 0.84 | 2.01% |
| 9 | ability:0x18B00 | 0.67 | 1.61% |
| 10 | ability:0x17801 | 0.66 | 1.59% |
| 11 | ability:0x18AA0 | 0.47 | 1.12% |
| 12 | ability:0x17A40 | 0.4 | 0.96% |
| 13 | ability:0x185E0 | 0.4 | 0.95% |
| 14 | ability:0x18A80 | 0.37 | 0.88% |
| 15 | ability:0x187E0 | 0.3 | 0.72% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.063 | 0.069 | 0 | 1.301 |
| 1 | 0.141 | 0.258 | 0.069 | 5.375 |
| 2 | 0.838 | 0.098 | 0.005 | 2.373 |
| 3 | 0.19 | 0.036 | 0 | 1.204 |
| 4 | 0.176 | 0.011 | 0 | 1.33 |
| 5 | 0.138 | 0.018 | 0.005 | 2.752 |
| 6 | 0.007 | 0.005 | 0.004 | 0.156 |
| 7 | 0 | 0.011 | 0.004 | 0.374 |
| 8 | 0 | 0.071 | 0 | 0.034 |
| 9 | 0.004 | 0.074 | 0 | 0.31 |
| all | 1.56 | 0.65 | 0.09 | 15.21 |

Busiest TheCore keys (of the 38.5% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| O | middle | 5.37 |
| P | index | 4.74 |
| 9 | middle | 2.75 |
| I | ring | 2.37 |
| K | ring | 1.33 |
| Period | middle | 1.3 |
| L | middle | 1.2 |
| Minus | index | 1.04 |
| 8 | ring | 0.37 |
| Comma | ring | 0.31 |

Top pairs within 1s (39.3 per minute over 21649 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | XelNaga_Caverns_Floating_BridgeNW8 > RightClick | 1735 | 32.13 |
| 2 | RightClick > Attack | 917 | 16.98 |
| 3 | RightClick > XelNaga_Caverns_Floating_BridgeNW8 | 861 | 15.94 |
| 4 | CG1 > RightClick | 762 | 14.11 |
| 5 | ability:0x17B40 > RightClick | 489 | 9.06 |
| 6 | RightClick > CG1 | 476 | 8.81 |
| 7 | RightClick > RightClick | 476 | 8.81 |
| 8 | Attack > RightClick | 463 | 8.57 |
| 9 | CG5 > ability:0x18761 | 384 | 7.11 |
| 10 | CG1 > XelNaga_Caverns_Floating_BridgeNW8 | 370 | 6.85 |
| 11 | RightClick > ability:0x18A60 | 345 | 6.39 |
| 12 | Attack > CG1 | 336 | 6.22 |

Same finger on the next key: **24.0%** of the 3732 pairs where both events map to a key. Of those same pairs, 8.6% are the same key twice (a repeat no layout can move apart) and **15.4% are the same finger on a different key**.

### Fenix

53 replays, 53 player-games, 637 minutes, 26734 commands: **41.9 commands per minute** (504.4 per game). 21.63 control-group actions and 9.52 camera jumps per minute. 19.2% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 14.67 | 34.97% |
| 2 | Attack | 11.22 | 26.74% |
| 3 | TrainProbe | 1.65 | 3.92% |
| 4 | BuildPylon | 0.88 | 2.09% |
| 5 | TrainZealot | 0.75 | 1.8% |
| 6 | TrainAdept | 0.65 | 1.56% |
| 7 | WarpInZealot | 0.61 | 1.46% |
| 8 | ability:0x15B20 | 0.52 | 1.23% |
| 9 | BuildGateway | 0.48 | 1.14% |
| 10 | CancelLast | 0.44 | 1.05% |
| 11 | ability:0xDC20 | 0.4 | 0.96% |
| 12 | ability:0x0E80 | 0.37 | 0.89% |
| 13 | TrainImmortal | 0.33 | 0.8% |
| 14 | ability:0x15B40 | 0.3 | 0.72% |
| 15 | ability:0x113A0 | 0.28 | 0.68% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.024 | 0.099 | 0.005 | 1.172 |
| 1 | 0.347 | 0.571 | 0.019 | 6.638 |
| 2 | 0.148 | 0.035 | 0.009 | 2.432 |
| 3 | 0.11 | 0.071 | 0 | 1.969 |
| 4 | 0.072 | 0.041 | 0 | 5.399 |
| 5 | 0.022 | 0.017 | 0.003 | 0.308 |
| 6 | 0.006 | 0.002 | 0 | 0.089 |
| 7 | 0 | 0.013 | 0.009 | 0.195 |
| 8 | 0.014 | 0.038 | 0.008 | 1.07 |
| 9 | 0.017 | 0.061 | 0 | 0.588 |
| all | 0.76 | 0.95 | 0.05 | 19.86 |

Busiest TheCore keys (of the 62.8% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 13.01 |
| O | middle | 6.64 |
| K | ring | 5.4 |
| I | ring | 2.43 |
| Minus | index | 2.05 |
| L | middle | 1.97 |
| SemiColon | index | 1.65 |
| Period | middle | 1.17 |
| U | pinky | 1.07 |
| Comma | ring | 0.59 |

Top pairs within 1s (43.5 per minute over 27726 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 2896 | 54.64 |
| 2 | Attack > RightClick | 2024 | 38.19 |
| 3 | CG1 > CG1 | 1193 | 22.51 |
| 4 | CG1 > Attack | 963 | 18.17 |
| 5 | CG4 > CG4 | 820 | 15.47 |
| 6 | Attack > CG1 | 735 | 13.87 |
| 7 | CG4 > TrainProbe | 632 | 11.92 |
| 8 | CG2 > RightClick | 385 | 7.26 |
| 9 | CG1 > RightClick | 380 | 7.17 |
| 10 | RightClick > CG4 | 377 | 7.11 |
| 11 | CG1 > CG4 | 369 | 6.96 |
| 12 | CG4 > CG1 | 368 | 6.94 |

Same finger on the next key: **33.0%** of the 11760 pairs where both events map to a key. Of those same pairs, 22.6% are the same key twice (a repeat no layout can move apart) and **10.5% are the same finger on a different key**.

### Nova

52 replays, 52 player-games, 723 minutes, 25176 commands: **34.8 commands per minute** (484.2 per game). 17.83 control-group actions and 7.72 camera jumps per minute. 44.0% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 11.99 | 34.43% |
| 2 | Attack | 5.01 | 14.38% |
| 3 | ability:0x10660 | 1.11 | 3.2% |
| 4 | TrainSCV | 1.05 | 3.03% |
| 5 | ability:0x142E0 | 1.04 | 2.99% |
| 6 | ability:0x10600 | 0.74 | 2.13% |
| 7 | ability:0x14520 | 0.72 | 2.07% |
| 8 | ability:0x14660 | 0.7 | 2.02% |
| 9 | ability:0x106A0 | 0.61 | 1.76% |
| 10 | ability:0x14EE0 | 0.6 | 1.71% |
| 11 | ability:0x14F00 | 0.52 | 1.49% |
| 12 | ability:0x146C0 | 0.46 | 1.31% |
| 13 | ability:0x148A0 | 0.42 | 1.21% |
| 14 | ability:0x141A0 | 0.39 | 1.13% |
| 15 | ability:0x13AE0 | 0.35 | 1.01% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.021 | 0.028 | 0 | 0.234 |
| 1 | 0.19 | 0.191 | 0 | 6.356 |
| 2 | 0.289 | 0.019 | 0 | 3.909 |
| 3 | 0.156 | 0.017 | 0 | 2.02 |
| 4 | 0.1 | 0.015 | 0 | 1.644 |
| 5 | 0.147 | 0.001 | 0 | 1.097 |
| 6 | 0.094 | 0.001 | 0 | 1.034 |
| 7 | 0.025 | 0.003 | 0 | 0.122 |
| 8 | 0.001 | 0.011 | 0 | 0.007 |
| 9 | 0.014 | 0.029 | 0 | 0.051 |
| all | 1.04 | 0.32 | 0 | 16.47 |

Busiest TheCore keys (of the 46.1% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| O | middle | 6.36 |
| P | index | 5.18 |
| I | ring | 3.91 |
| L | middle | 2.02 |
| K | ring | 1.64 |
| Minus | index | 1.18 |
| 9 | middle | 1.1 |
| 0 | index | 1.03 |
| Period | middle | 0.23 |
| N | pinky | 0.22 |

Top pairs within 1s (34.2 per minute over 24747 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1073 | 20.63 |
| 2 | CG1 > RightClick | 939 | 18.06 |
| 3 | ability:0x142E0 > RightClick | 661 | 12.71 |
| 4 | Attack > RightClick | 595 | 11.44 |
| 5 | CG1 > CG2 | 582 | 11.19 |
| 6 | Attack > CG1 | 531 | 10.21 |
| 7 | CG1 > Attack | 523 | 10.06 |
| 8 | CG2 > CG1 | 482 | 9.27 |
| 9 | RightClick > CG1 | 475 | 9.13 |
| 10 | CG2 > RightClick | 448 | 8.62 |
| 11 | Attack > CG2 | 377 | 7.25 |
| 12 | RightClick > ability:0x10660 | 355 | 6.83 |

Same finger on the next key: **23.9%** of the 6270 pairs where both events map to a key. Of those same pairs, 9.4% are the same key twice (a repeat no layout can move apart) and **14.5% are the same finger on a different key**.

### Stetmann

52 replays, 52 player-games, 696 minutes, 31211 commands: **44.9 commands per minute** (600.2 per game). 23.07 control-group actions and 6.82 camera jumps per minute. 45.3% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 16.1 | 35.87% |
| 2 | Attack | 8.12 | 18.1% |
| 3 | ability:0x19860 | 3.33 | 7.43% |
| 4 | ability:0x198C2 | 1.26 | 2.81% |
| 5 | ability:0x19620 | 1.21 | 2.7% |
| 6 | ability:0x191C0 | 1.15 | 2.56% |
| 7 | ability:0x198C0 | 0.88 | 1.97% |
| 8 | ability:0x19640 | 0.82 | 1.83% |
| 9 | ability:0x19682 | 0.68 | 1.51% |
| 10 | ability:0x18F80 | 0.66 | 1.46% |
| 11 | ability:0x19A80 | 0.65 | 1.45% |
| 12 | ability:0x19A60 | 0.61 | 1.36% |
| 13 | ability:0x198C1 | 0.46 | 1.03% |
| 14 | ability:0x19680 | 0.44 | 0.98% |
| 15 | ability:0x18FA0 | 0.4 | 0.88% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.035 | 0 | 0 | 0.095 |
| 1 | 0.121 | 2.618 | 0 | 4.593 |
| 2 | 0.229 | 0.01 | 0 | 1.156 |
| 3 | 0.033 | 0 | 0 | 0.269 |
| 4 | 0.056 | 0.168 | 0 | 8.767 |
| 5 | 0.106 | 0.001 | 0 | 4.072 |
| 6 | 0.106 | 0 | 0 | 0.577 |
| 7 | 0.003 | 0 | 0 | 0.007 |
| 8 | 0.003 | 0 | 0 | 0.004 |
| 9 | 0.032 | 0 | 0 | 0.006 |
| all | 0.72 | 2.8 | 0 | 19.55 |

Busiest TheCore keys (of the 43.5% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| K | ring | 8.77 |
| P | index | 8.13 |
| O | middle | 4.59 |
| 9 | middle | 4.07 |
| I | ring | 1.16 |
| 0 | index | 0.58 |
| L | middle | 0.27 |
| Period | middle | 0.09 |
| BracketClose | index | 0.07 |
| Minus | index | 0.06 |

Top pairs within 1s (45.8 per minute over 31866 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1990 | 38.27 |
| 2 | CG4 > CG4 | 1603 | 30.83 |
| 3 | Attack > RightClick | 1550 | 29.81 |
| 4 | CG1 > RightClick | 1237 | 23.79 |
| 5 | CG4 > RightClick | 1018 | 19.58 |
| 6 | ability:0x19860 > RightClick | 821 | 15.79 |
| 7 | Attack > CG4 | 765 | 14.71 |
| 8 | RightClick > CG4 | 574 | 11.04 |
| 9 | RightClick > ability:0x19860 | 564 | 10.85 |
| 10 | Attack > CG1 | 523 | 10.06 |
| 11 | CG4 > ability:0x198C0 | 454 | 8.73 |
| 12 | CG5 > CG5 | 429 | 8.25 |

Same finger on the next key: **48.9%** of the 6171 pairs where both events map to a key. Of those same pairs, 37.0% are the same key twice (a repeat no layout can move apart) and **11.9% are the same finger on a different key**.

### Kerrigan

51 replays, 51 player-games, 629 minutes, 24314 commands: **38.6 commands per minute** (476.7 per game). 25.72 control-group actions and 10.65 camera jumps per minute. 32.6% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 12.47 | 32.27% |
| 2 | Attack | 6.78 | 17.54% |
| 3 | ability:0x6C40 | 2.07 | 5.35% |
| 4 | MorphDrone | 1.69 | 4.37% |
| 5 | ability:0x6D60 | 1.5 | 3.87% |
| 6 | BuildNydusCanal | 1.25 | 3.22% |
| 7 | ability:0x6BA0 | 1.16 | 3.01% |
| 8 | SpawnLarva | 0.9 | 2.33% |
| 9 | ability:0x6CC0 | 0.81 | 2.11% |
| 10 | MorphOverlord | 0.76 | 1.96% |
| 11 | ability:0x84A1 | 0.61 | 1.58% |
| 12 | ability:0x6E60 | 0.56 | 1.46% |
| 13 | ability:0x6C60 | 0.53 | 1.38% |
| 14 | ability:0x76F5 | 0.52 | 1.36% |
| 15 | ability:0x6D20 | 0.42 | 1.09% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.143 | 0.022 | 0 | 1.604 |
| 1 | 0.706 | 1.333 | 0.002 | 3.38 |
| 2 | 0.138 | 0.037 | 0.337 | 6.081 |
| 3 | 0.11 | 0.013 | 0.005 | 1.047 |
| 4 | 0.087 | 0.111 | 0 | 7.982 |
| 5 | 0.067 | 0.043 | 0 | 1.931 |
| 6 | 0.014 | 0.011 | 0 | 0.159 |
| 7 | 0.003 | 0 | 0 | 0.005 |
| 8 | 0.006 | 0 | 0 | 0.025 |
| 9 | 0.064 | 0.003 | 0.016 | 0.207 |
| all | 1.34 | 1.57 | 0.36 | 22.42 |

Busiest TheCore keys (of the 54.8% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| K | ring | 7.98 |
| P | index | 7.03 |
| I | ring | 6.08 |
| O | middle | 3.38 |
| Minus | index | 2.07 |
| 9 | middle | 1.93 |
| Period | middle | 1.6 |
| SemiColon | index | 1.1 |
| L | middle | 1.05 |
| H | pinky | 0.24 |

Top pairs within 1s (42.2 per minute over 26527 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1097 | 21.51 |
| 2 | CG2 > RightClick | 918 | 18.0 |
| 3 | Attack > RightClick | 733 | 14.37 |
| 4 | Attack > CG4 | 682 | 13.37 |
| 5 | RightClick > CG4 | 676 | 13.25 |
| 6 | ability:0x6C40 > RightClick | 675 | 13.24 |
| 7 | Attack > CG2 | 606 | 11.88 |
| 8 | CG4 > CG4 | 575 | 11.27 |
| 9 | CG4 > MorphDrone | 546 | 10.71 |
| 10 | RightClick > CG2 | 445 | 8.73 |
| 11 | CG2 > CG4 | 420 | 8.24 |
| 12 | CG4 > RightClick | 398 | 7.8 |

Same finger on the next key: **26.2%** of the 8809 pairs where both events map to a key. Of those same pairs, 11.9% are the same key twice (a repeat no layout can move apart) and **14.3% are the same finger on a different key**.

### Mengsk

48 replays, 48 player-games, 590 minutes, 25760 commands: **43.7 commands per minute** (536.7 per game). 22.47 control-group actions and 6.22 camera jumps per minute. 40.5% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 16.56 | 37.92% |
| 2 | Attack | 9.08 | 20.8% |
| 3 | ability:0x1A421 | 2.8 | 6.41% |
| 4 | ability:0x1A221 | 1.93 | 4.42% |
| 5 | ability:0x1A400 | 0.85 | 1.96% |
| 6 | ability:0x19FC0 | 0.67 | 1.53% |
| 7 | ability:0x19DC0 | 0.64 | 1.46% |
| 8 | ability:0x1A260 | 0.56 | 1.28% |
| 9 | ability:0x1A041 | 0.54 | 1.23% |
| 10 | ability:0x1A820 | 0.48 | 1.09% |
| 11 | ability:0x19DA0 | 0.44 | 1.0% |
| 12 | ability:0x19FA0 | 0.42 | 0.95% |
| 13 | ability:0x1A200 | 0.4 | 0.92% |
| 14 | ability:0x1A840 | 0.35 | 0.79% |
| 15 | ability:0x19DC2 | 0.33 | 0.75% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.051 | 0.081 | 0.007 | 1.27 |
| 1 | 0.181 | 2.539 | 0 | 6.786 |
| 2 | 0.147 | 0.136 | 0 | 1.887 |
| 3 | 0.217 | 0.032 | 0 | 1.441 |
| 4 | 0.158 | 0.069 | 0 | 5.416 |
| 5 | 0.075 | 0 | 0 | 0.659 |
| 6 | 0.063 | 0 | 0 | 0.232 |
| 7 | 0 | 0.005 | 0 | 0.002 |
| 8 | 0 | 0.076 | 0 | 0.115 |
| 9 | 0.041 | 0.085 | 0.002 | 0.683 |
| all | 0.93 | 3.02 | 0.01 | 18.49 |

Busiest TheCore keys (of the 44.9% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 9.08 |
| O | middle | 6.79 |
| K | ring | 5.42 |
| I | ring | 1.89 |
| L | middle | 1.44 |
| Period | middle | 1.27 |
| Comma | ring | 0.68 |
| 9 | middle | 0.66 |
| 0 | index | 0.23 |
| G | pinky | 0.15 |

Top pairs within 1s (43.7 per minute over 25808 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1903 | 39.65 |
| 2 | CG1 > Attack | 1641 | 34.19 |
| 3 | CG4 > RightClick | 1078 | 22.46 |
| 4 | Attack > RightClick | 983 | 20.48 |
| 5 | RightClick > ability:0x1A421 | 967 | 20.15 |
| 6 | Attack > CG1 | 780 | 16.25 |
| 7 | RightClick > ability:0x1A221 | 776 | 16.17 |
| 8 | Attack > CG4 | 765 | 15.94 |
| 9 | ability:0x1A221 > RightClick | 690 | 14.38 |
| 10 | CG1 > CG1 | 594 | 12.38 |
| 11 | ability:0x1A421 > RightClick | 470 | 9.79 |
| 12 | RightClick > CG4 | 440 | 9.17 |

Same finger on the next key: **18.7%** of the 6341 pairs where both events map to a key. Of those same pairs, 13.1% are the same key twice (a repeat no layout can move apart) and **5.6% are the same finger on a different key**.

### Karax

45 replays, 45 player-games, 691 minutes, 25172 commands: **36.4 commands per minute** (559.4 per game). 14.48 control-group actions and 8.55 camera jumps per minute. 26.3% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 11.49 | 31.54% |
| 2 | Attack | 7.0 | 19.2% |
| 3 | ability:0x14280 | 1.78 | 4.89% |
| 4 | TrainProbe | 1.57 | 4.32% |
| 5 | BuildPylon | 1.43 | 3.93% |
| 6 | ability:0x14440 | 1.4 | 3.83% |
| 7 | TrainImmortal | 0.82 | 2.24% |
| 8 | ability:0xF2A0 | 0.77 | 2.1% |
| 9 | WarpInZealot | 0.74 | 2.04% |
| 10 | ability:0xBAA0 | 0.63 | 1.73% |
| 11 | BuildPhotonCannon | 0.63 | 1.72% |
| 12 | ability:0xF280 | 0.62 | 1.71% |
| 13 | ability:0x141A0 | 0.54 | 1.48% |
| 14 | WarpInSentry | 0.52 | 1.43% |
| 15 | ability:0xBAE0 | 0.49 | 1.33% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.032 | 0.071 | 0 | 0.324 |
| 1 | 0.203 | 0.938 | 0.009 | 3.605 |
| 2 | 0.177 | 0.012 | 0 | 1.588 |
| 3 | 0.426 | 0.026 | 0.006 | 1.689 |
| 4 | 0.143 | 0.016 | 0.004 | 1.518 |
| 5 | 0.201 | 0.001 | 0 | 2.513 |
| 6 | 0.02 | 0 | 0 | 0.122 |
| 7 | 0 | 0.012 | 0 | 0.001 |
| 8 | 0.004 | 0.072 | 0 | 0.084 |
| 9 | 0.022 | 0.075 | 0 | 0.569 |
| all | 1.23 | 1.22 | 0.02 | 12.01 |

Busiest TheCore keys (of the 56.2% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 8.99 |
| O | middle | 3.61 |
| 9 | middle | 2.51 |
| Minus | index | 1.95 |
| L | middle | 1.69 |
| I | ring | 1.59 |
| SemiColon | index | 1.55 |
| K | ring | 1.52 |
| J | pinky | 1.4 |
| Comma | ring | 0.57 |

Top pairs within 1s (29.6 per minute over 20472 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1800 | 40.0 |
| 2 | Attack > RightClick | 939 | 20.87 |
| 3 | CG1 > Attack | 759 | 16.87 |
| 4 | ability:0x14280 > ability:0x14280 | 567 | 12.6 |
| 5 | CG2 > RightClick | 525 | 11.67 |
| 6 | CG1 > CG1 | 473 | 10.51 |
| 7 | ability:0x14440 > ability:0x14440 | 462 | 10.27 |
| 8 | CG3 > RightClick | 426 | 9.47 |
| 9 | ability:0xF2A0 > ability:0xF280 | 410 | 9.11 |
| 10 | Attack > CG3 | 396 | 8.8 |
| 11 | Attack > CG5 | 344 | 7.64 |
| 12 | Attack > CG1 | 327 | 7.27 |

Same finger on the next key: **21.7%** of the 6919 pairs where both events map to a key. Of those same pairs, 13.7% are the same key twice (a repeat no layout can move apart) and **8.0% are the same finger on a different key**.

### Stukov

45 replays, 45 player-games, 618 minutes, 20926 commands: **33.9 commands per minute** (465.0 per game). 18.68 control-group actions and 8.08 camera jumps per minute. 33.8% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 14.43 | 42.62% |
| 2 | Attack | 7.33 | 21.66% |
| 3 | ability:0x13702 | 1.44 | 4.26% |
| 4 | ability:0x138C2 | 1.28 | 3.78% |
| 5 | ability:0x132E0 | 0.87 | 2.57% |
| 6 | ability:0x13120 | 0.79 | 2.34% |
| 7 | ability:0x15240 | 0.72 | 2.14% |
| 8 | ability:0x15420 | 0.55 | 1.63% |
| 9 | ability:0x13122 | 0.48 | 1.41% |
| 10 | ability:0x132E2 | 0.45 | 1.32% |
| 11 | ability:0x13640 | 0.38 | 1.12% |
| 12 | ability:0x125E0 | 0.31 | 0.91% |
| 13 | ability:0x12760 | 0.27 | 0.8% |
| 14 | HoldPosition | 0.24 | 0.71% |
| 15 | ability:0x151A0 | 0.16 | 0.47% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.039 | 0.068 | 0.003 | 0.796 |
| 1 | 1.322 | 1.257 | 0 | 4.743 |
| 2 | 0.223 | 0.003 | 0 | 0.587 |
| 3 | 0.115 | 0.01 | 0 | 1.537 |
| 4 | 0.079 | 0.029 | 0 | 2.431 |
| 5 | 0.083 | 0.031 | 0 | 1.971 |
| 6 | 0.083 | 0 | 0 | 2.458 |
| 7 | 0.044 | 0.003 | 0 | 0.154 |
| 8 | 0.005 | 0.045 | 0 | 0.053 |
| 9 | 0.04 | 0.073 | 0.003 | 0.377 |
| all | 2.03 | 1.52 | 0.01 | 15.11 |

Busiest TheCore keys (of the 47.2% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 7.41 |
| O | middle | 4.74 |
| 0 | index | 2.46 |
| K | ring | 2.43 |
| 9 | middle | 1.97 |
| L | middle | 1.54 |
| Period | middle | 0.8 |
| I | ring | 0.59 |
| Comma | ring | 0.38 |
| BracketClose | index | 0.24 |

Top pairs within 1s (30.8 per minute over 19026 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1616 | 35.91 |
| 2 | Attack > RightClick | 1480 | 32.89 |
| 3 | CG1 > Attack | 961 | 21.36 |
| 4 | CG6 > ability:0x13702 | 715 | 15.89 |
| 5 | CG1 > RightClick | 698 | 15.51 |
| 6 | CG5 > RightClick | 513 | 11.4 |
| 7 | CG3 > RightClick | 496 | 11.02 |
| 8 | RightClick > CG1 | 464 | 10.31 |
| 9 | Attack > CG5 | 416 | 9.24 |
| 10 | RightClick > RightClick | 413 | 9.18 |
| 11 | RightClick > ability:0x138C2 | 377 | 8.38 |
| 12 | Attack > CG1 | 341 | 7.58 |

Same finger on the next key: **24.4%** of the 4144 pairs where both events map to a key. Of those same pairs, 9.0% are the same key twice (a repeat no layout can move apart) and **15.4% are the same finger on a different key**.

### Vorazun

45 replays, 45 player-games, 615 minutes, 17853 commands: **29.0 commands per minute** (396.7 per game). 20.12 control-group actions and 10.81 camera jumps per minute. 18.1% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 10.41 | 35.85% |
| 2 | Attack | 6.8 | 23.44% |
| 3 | WarpInDarkTemplar | 1.14 | 3.92% |
| 4 | TrainProbe | 1.09 | 3.75% |
| 5 | BuildPylon | 0.93 | 3.2% |
| 6 | WarpInStalker | 0.6 | 2.05% |
| 7 | BuildPhotonCannon | 0.49 | 1.7% |
| 8 | ability:0xED00 | 0.46 | 1.57% |
| 9 | BuildGateway | 0.45 | 1.55% |
| 10 | ability:0x12420 | 0.44 | 1.52% |
| 11 | ability:0xED60 | 0.4 | 1.36% |
| 12 | ability:0xEDA0 | 0.32 | 1.1% |
| 13 | ability:0x12B20 | 0.24 | 0.84% |
| 14 | ability:0x12440 | 0.24 | 0.82% |
| 15 | ability:0xBDE0 | 0.22 | 0.77% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.036 | 0.02 | 0.005 | 0.309 |
| 1 | 0.779 | 0.379 | 0 | 5.94 |
| 2 | 0.745 | 0.013 | 0.002 | 4.732 |
| 3 | 0.215 | 0.015 | 0.002 | 0.837 |
| 4 | 0.094 | 0.01 | 0.007 | 1.39 |
| 5 | 0.164 | 0 | 0 | 1.603 |
| 6 | 0.078 | 0 | 0.007 | 2.285 |
| 7 | 0.026 | 0 | 0 | 0.044 |
| 8 | 0.007 | 0.01 | 0 | 0.101 |
| 9 | 0.013 | 0.021 | 0.013 | 0.218 |
| all | 2.16 | 0.47 | 0.04 | 17.46 |

Busiest TheCore keys (of the 65.3% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 7.51 |
| O | middle | 5.94 |
| I | ring | 4.73 |
| 0 | index | 2.28 |
| Minus | index | 1.84 |
| 9 | middle | 1.6 |
| K | ring | 1.39 |
| H | pinky | 1.2 |
| SemiColon | index | 1.12 |
| L | middle | 0.84 |

Top pairs within 1s (28.3 per minute over 17400 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1006 | 22.36 |
| 2 | CG1 > Attack | 790 | 17.56 |
| 3 | CG1 > CG2 | 692 | 15.38 |
| 4 | Attack > CG2 | 666 | 14.8 |
| 5 | CG2 > CG1 | 655 | 14.56 |
| 6 | CG1 > RightClick | 610 | 13.56 |
| 7 | CG5 > CG6 | 593 | 13.18 |
| 8 | Attack > RightClick | 431 | 9.58 |
| 9 | CG6 > CG5 | 426 | 9.47 |
| 10 | CG2 > RightClick | 405 | 9.0 |
| 11 | RightClick > CG1 | 396 | 8.8 |
| 12 | RightClick > CG2 | 315 | 7.0 |

Same finger on the next key: **16.8%** of the 8075 pairs where both events map to a key. Of those same pairs, 9.8% are the same key twice (a repeat no layout can move apart) and **7.0% are the same finger on a different key**.

### Raynor

26 replays, 26 player-games, 356 minutes, 15922 commands: **44.7 commands per minute** (612.4 per game). 75.88 control-group actions and 11.44 camera jumps per minute. 10.5% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 16.96 | 37.92% |
| 2 | Attack | 6.03 | 13.48% |
| 3 | TrainMarine | 5.93 | 13.27% |
| 4 | UseStimpack | 2.29 | 5.13% |
| 5 | TrainSCV | 1.47 | 3.29% |
| 6 | CalldownMULE | 1.15 | 2.58% |
| 7 | ability:0x13E4 | 0.97 | 2.16% |
| 8 | XelNaga_Caverns_Floating_BridgeNE8 | 0.67 | 1.49% |
| 9 | Stop | 0.49 | 1.11% |
| 10 | ability:0x3340 | 0.43 | 0.96% |
| 11 | XelNaga_Caverns_Floating_BridgeNW8Out | 0.38 | 0.84% |
| 12 | WidowMine | 0.32 | 0.72% |
| 13 | UpgradeToOrbitalCommand | 0.29 | 0.66% |
| 14 | BuildBarracks | 0.28 | 0.63% |
| 15 | ability:0x1409 | 0.27 | 0.61% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.017 | 0 | 0 | 0.11 |
| 1 | 0.216 | 0.222 | 0 | 2.598 |
| 2 | 0.329 | 0.011 | 0.003 | 5.257 |
| 3 | 0.331 | 0.014 | 0 | 26.879 |
| 4 | 0.272 | 0.11 | 0 | 7.771 |
| 5 | 0.264 | 0.008 | 0 | 30.777 |
| 6 | 0.056 | 0.039 | 0 | 0.517 |
| 7 | 0.011 | 0 | 0 | 0.067 |
| 9 | 0.006 | 0 | 0 | 0 |
| all | 1.5 | 0.4 | 0.0 | 73.98 |

Busiest TheCore keys (of the 80.0% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| 9 | middle | 30.78 |
| L | middle | 26.88 |
| P | index | 14.4 |
| K | ring | 7.77 |
| I | ring | 5.26 |
| O | middle | 2.6 |
| J | pinky | 1.83 |
| Minus | index | 1.61 |
| SemiColon | index | 0.86 |
| BracketOpen | index | 0.6 |

Top pairs within 1s (102.0 per minute over 36315 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG3 > CG5 | 8758 | 336.85 |
| 2 | CG5 > CG3 | 6737 | 259.12 |
| 3 | RightClick > TrainMarine | 1465 | 56.35 |
| 4 | CG5 > CG2 | 1313 | 50.5 |
| 5 | CG2 > CG5 | 1267 | 48.73 |
| 6 | CG4 > RightClick | 1035 | 39.81 |
| 7 | TrainMarine > RightClick | 982 | 37.77 |
| 8 | Attack > CG4 | 723 | 27.81 |
| 9 | RightClick > Attack | 680 | 26.15 |
| 10 | CG5 > CG4 | 578 | 22.23 |
| 11 | RightClick > CG3 | 467 | 17.96 |
| 12 | UseStimpack > Attack | 402 | 15.46 |

Same finger on the next key: **65.4%** of the 25843 pairs where both events map to a key. Of those same pairs, 4.0% are the same key twice (a repeat no layout can move apart) and **61.4% are the same finger on a different key**.

## Reproducing

```
# fetch the archive: see replays/README.md
uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
    extract ~/scratch/thecore/coop/replays --coop \
    -o ~/scratch/thecore/coop/events.jsonl.gz
uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
    report ~/scratch/thecore/coop/events.jsonl.gz --coop \
    -o wiki/sc2-coop-sequences.md --summary thecore/coop-summary.json \
    --replay-set ... --parse-note ...   # exact text: replays/README.md
# or rebuild this page from the committed summary alone:
python3 tools/sc2_sequences.py report thecore/coop-summary.json \
    -o wiki/sc2-coop-sequences.md
```

The full aggregates, including the top 200 bigrams and the top 120 abilities per commander, are in `thecore/coop-summary.json`; the replays and the event stream stay out of the repo.
