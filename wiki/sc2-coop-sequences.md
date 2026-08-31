---
type: Reference
title: SC2 co-op command sequences, measured
description: Command frequencies, control-group use and event sequences measured from 975 StarCraft II Co-op speedrun replays, one set of numbers per commander.
tags: [starcraft, thecore, gaming, measurement, hotkeys, coop]
source: "starcraft2coop.com co-op speedrun archive; measured with tools/sc2_sequences.py"
---

# SC2 co-op command sequences, measured

The companion to [SC2 command sequences, measured](sc2-command-sequences.md), which measures 1v1 pro play. This page measures **Co-op Commanders** instead: 975 replays, 1121 player-games, 18 commanders, 14,291 minutes played. Co-op is where a hotkey layout is stressed differently: every commander has its own calldowns and top-bar abilities on top of the melee kit.

## Where the replays come from

The set is the community **co-op speedrun archive**: the replays behind the clear-time leaderboards on [starcraft2coop.com](https://starcraft2coop.com/), kept in the public Google Drive folder [0B0kAPEv3WqAeZlhmbzN5NWlDc1E](https://drive.google.com/drive/folders/0B0kAPEv3WqAeZlhmbzN5NWlDc1E), one directory per commander (`Dehaka Solo`, `Alarak-Co-Op`, ...). These are record attempts, not average games, so read every rate as the fast end of what a player does, not the median.

The archive is old and wide: 58 distinct game builds, 3.13.0.52910 to 5.0.15.95841. `replays/README.md` says how to fetch it and where it lives locally.

## What is counted

Definitions (command, control-group action, camera jump, sequence pair, the TheCore projection) are the ones on the [1v1 page](sc2-command-sequences.md#what-is-counted), with three co-op-specific points:

- **Who is a player.** A co-op replay has two player slots and a pile of Amon computer players. Human players are the ones with a commander; `replay.cooperative` is not used, because it is 0 on plenty of these replays. In a two-human run each player is counted under their own commander, so one replay can feed two commanders' numbers.
- **Hex-id tokens.** sc2reader has no name for many commander-specific abilities, so about 30.0% of commands here arrive as a numeric ability id, written `ability:0x....`. They are kept verbatim rather than dropped: the id is stable inside a build, so it counts and sequences correctly, and only the label is missing. Because the archive spans 58 builds, the same id can mean different abilities in different years — treat a hex token as a within-commander shape, not a name.
- **Camera hotkeys are invisible.** A replay records where the camera went, never which key sent it there, and co-op players lean on camera hotkeys and the minimap hard. The camera-jump counts below are an upper bound on camera hotkey presses, and no camera key appears in the sequences at all, so the real same-finger load is higher than the numbers here.

## Commanders

All 975 replays in the archive parsed with sc2reader 1.9.0 at load_level=4; none failed.

| Commander | Replays | Player-games | Minutes | Commands | Commands/min | CG actions/min | Camera jumps/min | Distinct abilities | Hex-id share | On a TheCore key |
|---|---|---|---|---|---|---|---|---|---|---|
| Dehaka | 158 | 158 | 1738 | 69665 | 40.1 | 21.74 | 10.28 | 506 | 41.3% | 17.7% |
| Abathur | 89 | 89 | 838 | 22258 | 26.6 | 29.39 | 10.9 | 171 | 20.8% | 35.4% |
| Artanis | 77 | 77 | 1162 | 36269 | 31.2 | 13.39 | 9.85 | 131 | 14.2% | 47.5% |
| Zagara | 72 | 72 | 1003 | 31891 | 31.8 | 22.89 | 8.85 | 196 | 24.3% | 38.2% |
| Alarak | 68 | 68 | 869 | 36486 | 42.0 | 25.11 | 8.59 | 138 | 29.5% | 35.6% |
| Nova | 63 | 63 | 860 | 31146 | 36.2 | 17.86 | 7.83 | 259 | 42.0% | 19.4% |
| Tychus | 58 | 58 | 813 | 29626 | 36.4 | 15.67 | 9.46 | 216 | 31.7% | 34.2% |
| Swann | 57 | 57 | 816 | 37812 | 46.3 | 25.09 | 11.69 | 192 | 18.2% | 37.2% |
| Han & Horner | 55 | 55 | 731 | 23673 | 32.4 | 12.96 | 9.01 | 249 | 40.7% | 29.6% |
| Zeratul | 54 | 54 | 551 | 22943 | 41.6 | 17.51 | 9.61 | 196 | 34.9% | 16.0% |
| Fenix | 53 | 53 | 637 | 26734 | 41.9 | 21.63 | 9.52 | 190 | 18.5% | 45.2% |
| Stetmann | 52 | 52 | 696 | 31211 | 44.9 | 23.07 | 6.82 | 204 | 44.4% | 18.8% |
| Kerrigan | 51 | 51 | 629 | 24314 | 38.6 | 25.72 | 10.65 | 166 | 32.3% | 28.6% |
| Mengsk | 49 | 49 | 598 | 26071 | 43.6 | 22.41 | 6.33 | 226 | 39.3% | 21.4% |
| Vorazun | 48 | 48 | 679 | 20184 | 29.7 | 19.17 | 10.44 | 151 | 17.9% | 44.1% |
| Karax | 45 | 45 | 691 | 25172 | 36.4 | 14.48 | 8.55 | 119 | 26.3% | 41.7% |
| Stukov | 45 | 45 | 618 | 20926 | 33.9 | 18.68 | 8.08 | 164 | 33.5% | 23.6% |
| Raynor | 27 | 27 | 364 | 15926 | 43.8 | 74.28 | 11.24 | 199 | 10.1% | 47.0% |

Control-group load is the number that varies most, and not with command rate: Raynor runs 74.28 control-group actions a minute (mostly recalls, on 364 minutes of play) against Han & Horner's 12.96. A layout tuned for one commander is not tuned for another.

"On a TheCore key" uses only the bindings the hotkey file gives that commander (its own units, its race's melee units, and the global commands), so it is a fair per-commander coverage figure. The hex-id commands can never map, which is most of what the gap is.

### Dehaka

158 replays, 158 player-games, 1738 minutes, 69665 commands: **40.1 commands per minute** (440.9 per game). 21.74 control-group actions and 10.28 camera jumps per minute. 41.3% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 14.46 | 36.07% |
| 2 | Attack | 6.09 | 15.2% |
| 3 | ability:0x11400 | 2.02 | 5.04% |
| 4 | ability:0x11300 | 1.48 | 3.7% |
| 5 | ability:0x113A0 | 1.14 | 2.84% |
| 6 | ability:0x11220 | 1.13 | 2.82% |
| 7 | ability:0x112A0 | 0.7 | 1.75% |
| 8 | ability:0x111C0 | 0.7 | 1.75% |
| 9 | ability:0x160A0 | 0.6 | 1.5% |
| 10 | HoldPosition | 0.58 | 1.46% |
| 11 | ability:0x11120 | 0.46 | 1.15% |
| 12 | ability:0x16420 | 0.43 | 1.08% |
| 13 | Stop | 0.34 | 0.84% |
| 14 | ability:0x11200 | 0.33 | 0.81% |
| 15 | ability:0x112C0 | 0.31 | 0.77% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.056 | 0 | 0 | 0.695 |
| 1 | 0.149 | 0.005 | 0.002 | 8.469 |
| 2 | 0.183 | 0.024 | 0.001 | 1.664 |
| 3 | 0.121 | 0.083 | 0.002 | 2.46 |
| 4 | 0.12 | 0.022 | 0 | 4.229 |
| 5 | 0.131 | 0.018 | 0.001 | 2.057 |
| 6 | 0.026 | 0.003 | 0 | 0.082 |
| 7 | 0.001 | 0 | 0 | 0 |
| 8 | 0.035 | 0 | 0.001 | 0.306 |
| 9 | 0.045 | 0.004 | 0 | 0.743 |
| all | 0.87 | 0.16 | 0.01 | 20.7 |

Busiest TheCore keys (of the 45.7% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| O | middle | 8.47 |
| P | index | 6.1 |
| K | ring | 4.23 |
| L | middle | 2.46 |
| 9 | middle | 2.06 |
| I | ring | 1.66 |
| Comma | ring | 0.74 |
| Period | middle | 0.69 |
| BracketClose | index | 0.58 |
| G | pinky | 0.34 |

Top pairs within 1s (42.8 per minute over 74437 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG1 > RightClick | 4313 | 27.3 |
| 2 | RightClick > Attack | 2488 | 15.75 |
| 3 | Attack > RightClick | 1996 | 12.63 |
| 4 | ability:0x11400 > RightClick | 1464 | 9.27 |
| 5 | RightClick > CG1 | 1464 | 9.27 |
| 6 | Attack > CG1 | 1280 | 8.1 |
| 7 | CG1 > CG5 | 1280 | 8.1 |
| 8 | CG1 > Attack | 1250 | 7.91 |
| 9 | CG1 > CG4 | 1182 | 7.48 |
| 10 | ability:0x11300 > RightClick | 1167 | 7.39 |
| 11 | CG4 > CG1 | 1160 | 7.34 |
| 12 | ability:0x11220 > RightClick | 1034 | 6.54 |

Same finger on the next key: **23.7%** of the 19264 pairs where both events map to a key. Of those same pairs, 8.1% are the same key twice (a repeat no layout can move apart) and **15.6% are the same finger on a different key**.

### Abathur

89 replays, 89 player-games, 838 minutes, 22258 commands: **26.6 commands per minute** (250.1 per game). 29.39 control-group actions and 10.9 camera jumps per minute. 20.8% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 11.36 | 42.76% |
| 2 | Attack | 5.46 | 20.56% |
| 3 | MorphDrone | 0.85 | 3.22% |
| 4 | ability:0x12060 | 0.76 | 2.86% |
| 5 | MorphMutalisk | 0.7 | 2.64% |
| 6 | HoldPosition | 0.57 | 2.14% |
| 7 | ability:0x11E00 | 0.5 | 1.87% |
| 8 | MorphOverlord | 0.48 | 1.81% |
| 9 | ability:0x11F20 | 0.33 | 1.24% |
| 10 | ability:0x143A0 | 0.31 | 1.16% |
| 11 | ability:0x14740 | 0.29 | 1.1% |
| 12 | ability:0x11C60 | 0.28 | 1.04% |
| 13 | ability:0x11D00 | 0.19 | 0.73% |
| 14 | ability:0x14720 | 0.19 | 0.72% |
| 15 | ability:0x14540 | 0.19 | 0.71% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.068 | 0.002 | 0 | 0.718 |
| 1 | 0.413 | 0.211 | 0.084 | 3.012 |
| 2 | 0.351 | 0.074 | 0.06 | 7.059 |
| 3 | 0.321 | 0.029 | 0.013 | 5.522 |
| 4 | 0.045 | 0.007 | 0.006 | 1.902 |
| 5 | 0.06 | 0 | 0.005 | 7.707 |
| 6 | 0.004 | 0 | 0.011 | 0.269 |
| 7 | 0.001 | 0.001 | 0 | 0.039 |
| 8 | 0.012 | 0.017 | 0.027 | 0.26 |
| 9 | 0.013 | 0.026 | 0.049 | 0.931 |
| all | 1.29 | 0.37 | 0.26 | 27.42 |

Busiest TheCore keys (of the 68.2% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| 9 | middle | 7.71 |
| I | ring | 7.06 |
| P | index | 5.58 |
| L | middle | 5.52 |
| O | middle | 3.01 |
| K | ring | 1.9 |
| Minus | index | 0.93 |
| Comma | ring | 0.93 |
| SemiColon | index | 0.76 |
| Period | middle | 0.72 |

Top pairs within 1s (36.8 per minute over 30817 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG3 > CG5 | 3210 | 36.07 |
| 2 | CG5 > CG2 | 2728 | 30.65 |
| 3 | CG2 > CG5 | 2503 | 28.12 |
| 4 | CG5 > CG3 | 2070 | 23.26 |
| 5 | RightClick > Attack | 1560 | 17.53 |
| 6 | Attack > RightClick | 989 | 11.11 |
| 7 | CG2 > RightClick | 928 | 10.43 |
| 8 | RightClick > RightClick | 704 | 7.91 |
| 9 | CG1 > RightClick | 517 | 5.81 |
| 10 | RightClick > CG2 | 474 | 5.33 |
| 11 | CG3 > RightClick | 398 | 4.47 |
| 12 | RightClick > CG1 | 395 | 4.44 |

Same finger on the next key: **35.8%** of the 17883 pairs where both events map to a key. Of those same pairs, 2.4% are the same key twice (a repeat no layout can move apart) and **33.4% are the same finger on a different key**.

### Artanis

77 replays, 77 player-games, 1162 minutes, 36269 commands: **31.2 commands per minute** (471.0 per game). 13.39 control-group actions and 9.85 camera jumps per minute. 14.2% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 11.71 | 37.52% |
| 2 | Attack | 8.99 | 28.8% |
| 3 | WarpInStalker | 1.5 | 4.81% |
| 4 | TrainProbe | 1.5 | 4.79% |
| 5 | WarpInZealot | 0.79 | 2.53% |
| 6 | ability:0xDDE0 | 0.72 | 2.31% |
| 7 | ability:0xF3A0 | 0.39 | 1.26% |
| 8 | ability:0xF3C0 | 0.39 | 1.24% |
| 9 | Stop | 0.33 | 1.07% |
| 10 | HoldPosition | 0.3 | 0.95% |
| 11 | BuildPhotonCannon | 0.28 | 0.9% |
| 12 | BuildAssimilator | 0.23 | 0.75% |
| 13 | BuildPylon | 0.21 | 0.68% |
| 14 | ability:0x155D | 0.21 | 0.68% |
| 15 | ability:0xD229 | 0.2 | 0.63% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.009 | 0.043 | 0 | 0.336 |
| 1 | 0.698 | 0.375 | 0.003 | 3.555 |
| 2 | 0.382 | 0.035 | 0.001 | 1.936 |
| 3 | 0.082 | 0.014 | 0.022 | 0.603 |
| 4 | 0.145 | 0.019 | 0.001 | 2.324 |
| 5 | 0.067 | 0.005 | 0 | 0.84 |
| 6 | 0.09 | 0.004 | 0 | 1.347 |
| 7 | 0 | 0.002 | 0 | 0 |
| 8 | 0.003 | 0.021 | 0 | 0.04 |
| 9 | 0.011 | 0.053 | 0 | 0.325 |
| all | 1.49 | 0.57 | 0.03 | 11.31 |

Busiest TheCore keys (of the 61.4% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 10.15 |
| O | middle | 3.55 |
| Minus | index | 3.15 |
| K | ring | 2.32 |
| I | ring | 1.94 |
| 0 | index | 1.35 |
| 9 | middle | 0.84 |
| L | middle | 0.6 |
| Period | middle | 0.34 |
| G | pinky | 0.33 |

Top pairs within 1s (25.6 per minute over 29764 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 5319 | 69.08 |
| 2 | Attack > RightClick | 3357 | 43.6 |
| 3 | CG1 > Attack | 1125 | 14.61 |
| 4 | CG4 > WarpInStalker | 1030 | 13.38 |
| 5 | CG1 > RightClick | 642 | 8.34 |
| 6 | Attack > CG1 | 595 | 7.73 |
| 7 | RightClick > CG1 | 527 | 6.84 |
| 8 | CG2 > RightClick | 496 | 6.44 |
| 9 | ability:0xDDE0 > CG4 | 494 | 6.42 |
| 10 | Attack > CG4 | 443 | 5.75 |
| 11 | Attack > CG2 | 419 | 5.44 |
| 12 | CG5 > CG6 | 408 | 5.3 |

Same finger on the next key: **20.2%** of the 10441 pairs where both events map to a key. Of those same pairs, 11.4% are the same key twice (a repeat no layout can move apart) and **8.8% are the same finger on a different key**.

### Zagara

72 replays, 72 player-games, 1003 minutes, 31891 commands: **31.8 commands per minute** (442.9 per game). 22.89 control-group actions and 8.85 camera jumps per minute. 24.3% of commands are hex ids.

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

### Nova

63 replays, 63 player-games, 860 minutes, 31146 commands: **36.2 commands per minute** (494.4 per game). 17.86 control-group actions and 7.83 camera jumps per minute. 42.0% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 12.62 | 34.84% |
| 2 | Attack | 4.77 | 13.19% |
| 3 | ability:0x10660 | 1.65 | 4.56% |
| 4 | ability:0x142E0 | 1.49 | 4.12% |
| 5 | TrainSCV | 1.08 | 2.99% |
| 6 | ability:0x14660 | 0.82 | 2.26% |
| 7 | ability:0x14EE0 | 0.76 | 2.11% |
| 8 | ability:0x14F00 | 0.65 | 1.8% |
| 9 | ability:0x10600 | 0.62 | 1.72% |
| 10 | ability:0x14520 | 0.6 | 1.67% |
| 11 | ability:0x106A0 | 0.51 | 1.42% |
| 12 | ability:0x146C0 | 0.44 | 1.22% |
| 13 | ability:0x15080 | 0.43 | 1.18% |
| 14 | ability:0x14780 | 0.42 | 1.16% |
| 15 | ability:0x148A0 | 0.35 | 0.98% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.019 | 0.042 | 0 | 0.277 |
| 1 | 0.173 | 0.16 | 0 | 6.585 |
| 2 | 0.279 | 0.016 | 0 | 3.632 |
| 3 | 0.157 | 0.014 | 0 | 2.25 |
| 4 | 0.086 | 0.013 | 0 | 1.399 |
| 5 | 0.159 | 0.001 | 0 | 1.156 |
| 6 | 0.113 | 0.001 | 0 | 1.03 |
| 7 | 0.023 | 0.005 | 0 | 0.109 |
| 8 | 0.001 | 0.017 | 0 | 0.006 |
| 9 | 0.012 | 0.045 | 0 | 0.084 |
| all | 1.02 | 0.31 | 0 | 16.53 |

Busiest TheCore keys (of the 44.6% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| O | middle | 6.58 |
| P | index | 4.94 |
| I | ring | 3.63 |
| L | middle | 2.25 |
| K | ring | 1.4 |
| Minus | index | 1.21 |
| 9 | middle | 1.16 |
| 0 | index | 1.03 |
| Period | middle | 0.28 |
| N | pinky | 0.23 |

Top pairs within 1s (35.6 per minute over 30646 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1374 | 21.81 |
| 2 | ability:0x142E0 > RightClick | 1176 | 18.67 |
| 3 | CG1 > RightClick | 1169 | 18.56 |
| 4 | Attack > RightClick | 678 | 10.76 |
| 5 | RightClick > ability:0x10660 | 659 | 10.46 |
| 6 | Attack > CG1 | 650 | 10.32 |
| 7 | CG1 > CG2 | 610 | 9.68 |
| 8 | RightClick > CG1 | 607 | 9.63 |
| 9 | ability:0x10660 > RightClick | 604 | 9.59 |
| 10 | CG1 > Attack | 533 | 8.46 |
| 11 | CG2 > RightClick | 516 | 8.19 |
| 12 | CG2 > CG1 | 513 | 8.14 |

Same finger on the next key: **24.4%** of the 7032 pairs where both events map to a key. Of those same pairs, 9.6% are the same key twice (a repeat no layout can move apart) and **14.8% are the same finger on a different key**.

### Tychus

58 replays, 58 player-games, 813 minutes, 29626 commands: **36.4 commands per minute** (510.8 per game). 15.67 control-group actions and 9.46 camera jumps per minute. 31.7% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 11.88 | 32.61% |
| 2 | Attack | 11.58 | 31.77% |
| 3 | ability:0x17F40 | 1.26 | 3.45% |
| 4 | ability:0x18480 | 1.04 | 2.86% |
| 5 | ability:0x18180 | 0.85 | 2.33% |
| 6 | ability:0x18360 | 0.69 | 1.9% |
| 7 | ability:0x18380 | 0.66 | 1.81% |
| 8 | ability:0x18460 | 0.57 | 1.57% |
| 9 | Stop | 0.53 | 1.44% |
| 10 | ability:0x17C60 | 0.53 | 1.44% |
| 11 | ability:0x184A0 | 0.51 | 1.4% |
| 12 | ability:0x17C40 | 0.5 | 1.37% |
| 13 | ability:0x18160 | 0.49 | 1.34% |
| 14 | ability:0x181A0 | 0.45 | 1.23% |
| 15 | ability:0x17C80 | 0.24 | 0.66% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.044 | 0.009 | 0 | 0.165 |
| 1 | 0.048 | 0.004 | 0.091 | 4.831 |
| 2 | 0.093 | 0.004 | 0.006 | 2.961 |
| 3 | 0.151 | 0.004 | 0.004 | 2.48 |
| 4 | 0.144 | 0.038 | 0.004 | 2.499 |
| 5 | 0.089 | 0.011 | 0.01 | 1.335 |
| 6 | 0.012 | 0.063 | 0.002 | 0.405 |
| 7 | 0.005 | 0.005 | 0.004 | 0.027 |
| 8 | 0.01 | 0.018 | 0.001 | 0.025 |
| 9 | 0.043 | 0.004 | 0 | 0.014 |
| all | 0.64 | 0.16 | 0.12 | 14.74 |

Busiest TheCore keys (of the 53.2% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 11.6 |
| O | middle | 4.83 |
| I | ring | 2.96 |
| K | ring | 2.5 |
| L | middle | 2.48 |
| 9 | middle | 1.34 |
| G | pinky | 0.53 |
| 0 | index | 0.4 |
| Period | middle | 0.16 |
| BracketClose | index | 0.11 |

Top pairs within 1s (33.7 per minute over 27435 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 3534 | 60.93 |
| 2 | Attack > RightClick | 1907 | 32.88 |
| 3 | CG1 > Attack | 876 | 15.1 |
| 4 | Attack > CG1 | 778 | 13.41 |
| 5 | CG2 > RightClick | 683 | 11.78 |
| 6 | Attack > CG2 | 641 | 11.05 |
| 7 | RightClick > CG1 | 452 | 7.79 |
| 8 | CG1 > CG3 | 441 | 7.6 |
| 9 | CG1 > RightClick | 431 | 7.43 |
| 10 | CG3 > CG1 | 413 | 7.12 |
| 11 | Attack > CG3 | 386 | 6.66 |
| 12 | ability:0x18360 > Attack | 381 | 6.57 |

Same finger on the next key: **23.2%** of the 7508 pairs where both events map to a key. Of those same pairs, 5.6% are the same key twice (a repeat no layout can move apart) and **17.6% are the same finger on a different key**.

### Swann

57 replays, 57 player-games, 816 minutes, 37812 commands: **46.3 commands per minute** (663.4 per game). 25.09 control-group actions and 11.69 camera jumps per minute. 18.2% of commands are hex ids.

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

### Han & Horner

55 replays, 55 player-games, 731 minutes, 23673 commands: **32.4 commands per minute** (430.4 per game). 12.96 control-group actions and 9.01 camera jumps per minute. 40.7% of commands are hex ids.

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

54 replays, 54 player-games, 551 minutes, 22943 commands: **41.6 commands per minute** (424.9 per game). 17.51 control-group actions and 9.61 camera jumps per minute. 34.9% of commands are hex ids.

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

53 replays, 53 player-games, 637 minutes, 26734 commands: **41.9 commands per minute** (504.4 per game). 21.63 control-group actions and 9.52 camera jumps per minute. 18.5% of commands are hex ids.

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

### Stetmann

52 replays, 52 player-games, 696 minutes, 31211 commands: **44.9 commands per minute** (600.2 per game). 23.07 control-group actions and 6.82 camera jumps per minute. 44.4% of commands are hex ids.

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

51 replays, 51 player-games, 629 minutes, 24314 commands: **38.6 commands per minute** (476.7 per game). 25.72 control-group actions and 10.65 camera jumps per minute. 32.3% of commands are hex ids.

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

49 replays, 49 player-games, 598 minutes, 26071 commands: **43.6 commands per minute** (532.1 per game). 22.41 control-group actions and 6.33 camera jumps per minute. 39.3% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 16.56 | 37.96% |
| 2 | Attack | 8.99 | 20.61% |
| 3 | ability:0x1A421 | 2.76 | 6.33% |
| 4 | ability:0x1A221 | 1.91 | 4.37% |
| 5 | ability:0x1A400 | 0.84 | 1.93% |
| 6 | ability:0x19FC0 | 0.66 | 1.51% |
| 7 | ability:0x19DC0 | 0.63 | 1.44% |
| 8 | ability:0x1A260 | 0.55 | 1.26% |
| 9 | ability:0x1A041 | 0.53 | 1.21% |
| 10 | ability:0x1A820 | 0.47 | 1.08% |
| 11 | ability:0x19DA0 | 0.43 | 0.99% |
| 12 | ability:0x19FA0 | 0.41 | 0.94% |
| 13 | ability:0x1A200 | 0.4 | 0.91% |
| 14 | ability:0x1A840 | 0.34 | 0.78% |
| 15 | ability:0x19DC2 | 0.32 | 0.74% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.05 | 0.08 | 0.007 | 1.253 |
| 1 | 0.179 | 2.507 | 0.003 | 6.702 |
| 2 | 0.146 | 0.134 | 0 | 1.862 |
| 3 | 0.214 | 0.032 | 0 | 1.422 |
| 4 | 0.156 | 0.069 | 0 | 5.346 |
| 5 | 0.074 | 0 | 0 | 0.651 |
| 6 | 0.062 | 0 | 0 | 0.229 |
| 7 | 0 | 0.005 | 0 | 0.002 |
| 8 | 0 | 0.114 | 0 | 0.162 |
| 9 | 0.04 | 0.089 | 0.002 | 0.81 |
| all | 0.92 | 3.03 | 0.01 | 18.44 |

Busiest TheCore keys (of the 44.8% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 8.99 |
| O | middle | 6.7 |
| K | ring | 5.35 |
| I | ring | 1.86 |
| L | middle | 1.42 |
| Period | middle | 1.25 |
| Comma | ring | 0.81 |
| 9 | middle | 0.65 |
| 0 | index | 0.23 |
| U | pinky | 0.16 |

Top pairs within 1s (43.6 per minute over 26067 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1909 | 38.96 |
| 2 | CG1 > Attack | 1641 | 33.49 |
| 3 | CG4 > RightClick | 1078 | 22.0 |
| 4 | Attack > RightClick | 986 | 20.12 |
| 5 | RightClick > ability:0x1A421 | 967 | 19.73 |
| 6 | Attack > CG1 | 780 | 15.92 |
| 7 | RightClick > ability:0x1A221 | 776 | 15.84 |
| 8 | Attack > CG4 | 765 | 15.61 |
| 9 | ability:0x1A221 > RightClick | 690 | 14.08 |
| 10 | CG1 > CG1 | 594 | 12.12 |
| 11 | ability:0x1A421 > RightClick | 470 | 9.59 |
| 12 | RightClick > CG4 | 440 | 8.98 |

Same finger on the next key: **18.7%** of the 6360 pairs where both events map to a key. Of those same pairs, 13.1% are the same key twice (a repeat no layout can move apart) and **5.6% are the same finger on a different key**.

### Vorazun

48 replays, 48 player-games, 679 minutes, 20184 commands: **29.7 commands per minute** (420.5 per game). 19.17 control-group actions and 10.44 camera jumps per minute. 17.9% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 10.74 | 36.11% |
| 2 | Attack | 6.89 | 23.18% |
| 3 | WarpInDarkTemplar | 1.17 | 3.94% |
| 4 | TrainProbe | 1.08 | 3.64% |
| 5 | BuildPylon | 0.96 | 3.24% |
| 6 | WarpInStalker | 0.64 | 2.15% |
| 7 | BuildPhotonCannon | 0.59 | 1.99% |
| 8 | ability:0xED60 | 0.56 | 1.88% |
| 9 | BuildGateway | 0.44 | 1.49% |
| 10 | ability:0xED00 | 0.41 | 1.39% |
| 11 | ability:0x12420 | 0.39 | 1.31% |
| 12 | ability:0x12B20 | 0.37 | 1.23% |
| 13 | ability:0xEDA0 | 0.29 | 0.98% |
| 14 | ability:0x12440 | 0.21 | 0.7% |
| 15 | ability:0xBDE0 | 0.2 | 0.68% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.032 | 0.028 | 0.004 | 0.361 |
| 1 | 0.747 | 0.343 | 0 | 5.495 |
| 2 | 0.797 | 0.012 | 0.001 | 4.496 |
| 3 | 0.186 | 0.013 | 0.001 | 0.75 |
| 4 | 0.121 | 0.009 | 0.006 | 1.668 |
| 5 | 0.15 | 0 | 0 | 1.406 |
| 6 | 0.084 | 0 | 0.006 | 1.936 |
| 7 | 0.037 | 0 | 0 | 0.063 |
| 8 | 0.006 | 0.015 | 0 | 0.096 |
| 9 | 0.012 | 0.031 | 0.012 | 0.246 |
| all | 2.17 | 0.45 | 0.03 | 16.52 |

Busiest TheCore keys (of the 64.1% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| P | index | 7.68 |
| O | middle | 5.5 |
| I | ring | 4.5 |
| 0 | index | 1.94 |
| Minus | index | 1.87 |
| K | ring | 1.67 |
| 9 | middle | 1.41 |
| H | pinky | 1.23 |
| SemiColon | index | 1.15 |
| L | middle | 0.75 |

Top pairs within 1s (27.9 per minute over 18939 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | RightClick > Attack | 1260 | 26.25 |
| 2 | CG1 > Attack | 791 | 16.48 |
| 3 | Attack > CG2 | 719 | 14.98 |
| 4 | CG1 > CG2 | 696 | 14.5 |
| 5 | CG2 > CG1 | 667 | 13.9 |
| 6 | CG1 > RightClick | 626 | 13.04 |
| 7 | CG5 > CG6 | 541 | 11.27 |
| 8 | Attack > RightClick | 502 | 10.46 |
| 9 | CG2 > RightClick | 431 | 8.98 |
| 10 | RightClick > CG1 | 401 | 8.35 |
| 11 | CG6 > CG5 | 397 | 8.27 |
| 12 | RightClick > CG2 | 329 | 6.85 |

Same finger on the next key: **16.5%** of the 8466 pairs where both events map to a key. Of those same pairs, 9.8% are the same key twice (a repeat no layout can move apart) and **6.7% are the same finger on a different key**.

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

45 replays, 45 player-games, 618 minutes, 20926 commands: **33.9 commands per minute** (465.0 per game). 18.68 control-group actions and 8.08 camera jumps per minute. 33.5% of commands are hex ids.

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

### Raynor

27 replays, 27 player-games, 364 minutes, 15926 commands: **43.8 commands per minute** (589.9 per game). 74.28 control-group actions and 11.24 camera jumps per minute. 10.1% of commands are hex ids.

Top abilities, per minute:

| # | Ability | Per minute | Share of commands |
|---|---|---|---|
| 1 | RightClick | 16.6 | 37.93% |
| 2 | Attack | 5.9 | 13.47% |
| 3 | TrainMarine | 5.81 | 13.27% |
| 4 | UseStimpack | 2.25 | 5.13% |
| 5 | TrainSCV | 1.44 | 3.29% |
| 6 | CalldownMULE | 1.13 | 2.58% |
| 7 | ability:0x13E4 | 0.95 | 2.16% |
| 8 | XelNaga_Caverns_Floating_BridgeNE8 | 0.65 | 1.49% |
| 9 | Stop | 0.48 | 1.11% |
| 10 | ability:0x3340 | 0.42 | 0.96% |
| 11 | XelNaga_Caverns_Floating_BridgeNW8Out | 0.37 | 0.84% |
| 12 | WidowMine | 0.31 | 0.72% |
| 13 | UpgradeToOrbitalCommand | 0.29 | 0.66% |
| 14 | BuildBarracks | 0.28 | 0.63% |
| 15 | ability:0x1409 | 0.27 | 0.61% |

Control groups, actions per minute:

| Group | Set/min | Add/min | Steal/min | Recall/min |
|---|---|---|---|---|
| 0 | 0.016 | 0 | 0 | 0.107 |
| 1 | 0.212 | 0.217 | 0 | 2.543 |
| 2 | 0.322 | 0.011 | 0.003 | 5.146 |
| 3 | 0.324 | 0.014 | 0 | 26.311 |
| 4 | 0.267 | 0.107 | 0 | 7.607 |
| 5 | 0.258 | 0.008 | 0 | 30.126 |
| 6 | 0.055 | 0.038 | 0 | 0.506 |
| 7 | 0.011 | 0 | 0 | 0.066 |
| 9 | 0.005 | 0 | 0 | 0 |
| all | 1.47 | 0.4 | 0.0 | 72.41 |

Busiest TheCore keys (of the 80.0% of sequence events that map to one):

| Key | Finger | Events/min |
|---|---|---|
| 9 | middle | 30.13 |
| L | middle | 26.31 |
| P | index | 14.09 |
| K | ring | 7.61 |
| I | ring | 5.15 |
| O | middle | 2.54 |
| J | pinky | 1.8 |
| Minus | index | 1.57 |
| SemiColon | index | 0.84 |
| BracketOpen | index | 0.59 |

Top pairs within 1s (99.8 per minute over 36316 pairs):

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG3 > CG5 | 8758 | 324.37 |
| 2 | CG5 > CG3 | 6737 | 249.52 |
| 3 | RightClick > TrainMarine | 1465 | 54.26 |
| 4 | CG5 > CG2 | 1313 | 48.63 |
| 5 | CG2 > CG5 | 1267 | 46.93 |
| 6 | CG4 > RightClick | 1035 | 38.33 |
| 7 | TrainMarine > RightClick | 982 | 36.37 |
| 8 | Attack > CG4 | 723 | 26.78 |
| 9 | RightClick > Attack | 680 | 25.19 |
| 10 | CG5 > CG4 | 578 | 21.41 |
| 11 | RightClick > CG3 | 467 | 17.3 |
| 12 | UseStimpack > Attack | 402 | 14.89 |

Same finger on the next key: **65.4%** of the 25844 pairs where both events map to a key. Of those same pairs, 4.0% are the same key twice (a repeat no layout can move apart) and **61.4% are the same finger on a different key**.

## Reproducing

```
# fetch the archive: see replays/README.md
uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
    extract ~/scratch/thecore/coop/replays --coop \
    -o ~/scratch/thecore/coop/events.jsonl.gz
uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
    report ~/scratch/thecore/coop/events.jsonl.gz --coop \
    -o wiki/sc2-coop-sequences.md --summary thecore/coop-summary.json
# or rebuild this page from the committed summary alone:
python3 tools/sc2_sequences.py report thecore/coop-summary.json \
    -o wiki/sc2-coop-sequences.md
```

The full aggregates, including the top 200 bigrams and the top 120 abilities per commander, are in `thecore/coop-summary.json`; the replays and the event stream stay out of the repo.
