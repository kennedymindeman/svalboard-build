---
type: Reference
title: SC2 command sequences, measured
description: Command frequencies, control-group and camera use, and event sequences measured from 187 professional StarCraft II replays, projected onto TheCore 5.0's keys and fingers.
tags: [starcraft, thecore, gaming, measurement, hotkeys]
source: "IEM Katowice 2024 main event; measured with tools/sc2_sequences.py"
---

# SC2 command sequences, measured

Every number on this page is measured from replays, not estimated. The set is **IEM Katowice 2024 main event**: 187 games, patch 5.0.12.91115, parsed with sc2reader at `load_level=4`.

Co-op Commanders are measured separately, one set of numbers per commander, in [SC2 co-op command sequences, measured](sc2-coop-sequences.md).

`tools/sc2_sequences.py` produced both this page and `thecore/sequences-summary.json`, which holds the same aggregates; the page can be rebuilt from that file alone, without the replays. `replays/README.md` says how to fetch the set again.

## What is counted

- **Command**: one `CommandEvent` in the replay, i.e. one ability the player issued. Right-clicks (`RightClick`) are in the counts and are a mouse action, not a key.
- Follow-up `UpdateTargetPoint`/`UpdateTargetUnit` events (a target dragged while the mouse is down) are counted separately and left out of every rate below; including them would roughly double the right-click count.
- **Control group**: `set` (Shift+key in TheCore), `add` (Shift+Alt+key), `steal` (Ctrl+key, the steal-and-add and steal-and-set update types), `recall` (the bare key).
- **Camera jump**: two successive camera positions more than 20 map units apart. The distribution of that distance is bimodal, with scrolling below ~8 units, a trough at 14-20 and a second mode above it, so 20 sits in the trough. Replays record where the camera went, never which key moved it, so minimap clicks and follow-unit land in the same bucket: read jumps as an upper bound on camera hotkey presses.
- **Sequence**: consecutive events by the same player no more than 1 s apart, over a stream of commands and control-group recalls (the two things a hand does between camera moves). Times come from the replay's game loops at 22.4 loops per second, the LotV "Faster" rate every game in this set was played at, so they are real seconds a viewer would count. Events that share a loop keep the order the replay records them in; nothing is re-sorted.
- **TheCore projection**: sc2reader ability names normalised to the command names in `thecore/TheCore_5.0_Right_Plus.SC2Hotkeys`, then to that file's key and to the finger that presses it (`FINGERS` in `tools/thecore_keys.py`). Modifiers ride the thumb in TheCore, so a modified binding is counted on the finger of its base key.

## Coverage

All 187 replays in the pack parsed; none failed, so no s2protocol fallback was needed.

| Race | Player-games | Commands | Distinct abilities | On a TheCore key | Mouse (right-click) | No binding found | Unnamed by sc2reader |
|---|---|---|---|---|---|---|---|
| Terran | 167 | 173827 | 149 | 63.0% | 34.7% | 2.2% | 15 |
| Protoss | 106 | 77137 | 115 | 54.1% | 44.0% | 1.9% | 16 |
| Zerg | 101 | 88383 | 135 | 55.1% | 39.7% | 5.2% | 0 |

Right-clicking is the mouse and has no key in the file, so it is its own column. What is left over is ability names the file does not bind under any name the normalisation reaches: mostly upgrades at tech buildings, and a few sizeable gaps (`SpawnLarva`, the queen inject, is the largest). The biggest unmapped names per race are listed with each race below. The hotkey file also binds 17 co-op commanders whose units share ability names with the melee ones (37 command names carry more than one key); only Terran/Zerg/Protoss and global bindings are used here.

## Terran

167 player-games, 2280 minutes played, 173827 commands: **1040.9 per game, 76.2 per minute**. Control-group and camera numbers are per game.

### Top 40 abilities

These 40 are 93.9% of all Terran commands.

| # | Ability | Count | Per game | Per minute | Share |
|---|---|---|---|---|---|
| 1 | RightClick | 60385 | 361.59 | 26.49 | 34.74% |
| 2 | Attack | 39963 | 239.3 | 17.53 | 22.99% |
| 3 | TrainSCV | 9637 | 57.71 | 4.23 | 5.54% |
| 4 | TrainMarine | 8697 | 52.08 | 3.81 | 5.0% |
| 5 | Gather | 4024 | 24.1 | 1.77 | 2.31% |
| 6 | UseStimpack | 3791 | 22.7 | 1.66 | 2.18% |
| 7 | ScannerSweep | 2528 | 15.14 | 1.11 | 1.45% |
| 8 | SiegeMode | 2382 | 14.26 | 1.04 | 1.37% |
| 9 | BuildSupplyDepot | 2209 | 13.23 | 0.97 | 1.27% |
| 10 | TrainMarauder | 2037 | 12.2 | 0.89 | 1.17% |
| 11 | UnloadTargetMedivac | 1993 | 11.93 | 0.87 | 1.15% |
| 12 | MedivacSpeedBoost | 1926 | 11.53 | 0.84 | 1.11% |
| 13 | CalldownMULE | 1799 | 10.77 | 0.79 | 1.03% |
| 14 | BuildSiegeTank | 1493 | 8.94 | 0.65 | 0.86% |
| 15 | CancelLast | 1284 | 7.69 | 0.56 | 0.74% |
| 16 | ReturnCargo | 1283 | 7.68 | 0.56 | 0.74% |
| 17 | HoldPosition | 1281 | 7.67 | 0.56 | 0.74% |
| 18 | BurrowWidowMine | 1233 | 7.38 | 0.54 | 0.71% |
| 19 | TrainMedivac | 1070 | 6.41 | 0.47 | 0.62% |
| 20 | TankMode | 1069 | 6.4 | 0.47 | 0.61% |
| 21 | ScanMove | 1005 | 6.02 | 0.44 | 0.58% |
| 22 | BuildRefinery | 946 | 5.66 | 0.41 | 0.54% |
| 23 | TrainCyclone | 907 | 5.43 | 0.4 | 0.52% |
| 24 | Stop | 900 | 5.39 | 0.39 | 0.52% |
| 25 | BuildWidowMine | 894 | 5.35 | 0.39 | 0.51% |
| 26 | LowerSupplyDepot | 844 | 5.05 | 0.37 | 0.49% |
| 27 | LiberatorAGTarget | 785 | 4.7 | 0.34 | 0.45% |
| 28 | BuildCommandCenter | 717 | 4.29 | 0.31 | 0.41% |
| 29 | BuildBarracks | 653 | 3.91 | 0.29 | 0.38% |
| 30 | UpgradeToOrbitalCommand | 603 | 3.61 | 0.26 | 0.35% |
| 31 | TrainViking | 580 | 3.47 | 0.25 | 0.33% |
| 32 | TrainGhost | 559 | 3.35 | 0.25 | 0.32% |
| 33 | SCVRepair | 538 | 3.22 | 0.24 | 0.31% |
| 34 | BuildHellion | 514 | 3.08 | 0.23 | 0.3% |
| 35 | ChannelSnipe | 508 | 3.04 | 0.22 | 0.29% |
| 36 | BuildMissileTurret | 457 | 2.74 | 0.2 | 0.26% |
| 37 | LiftBarracks | 433 | 2.59 | 0.19 | 0.25% |
| 38 | EMPRound | 429 | 2.57 | 0.19 | 0.25% |
| 39 | LandBarracks | 413 | 2.47 | 0.18 | 0.24% |
| 40 | BuildBarracksReactor | 404 | 2.42 | 0.18 | 0.23% |

### Control groups

| Group | Set/game | Add/game | Steal/game | Recall/game |
|---|---|---|---|---|
| 0 | 4.65 | 0.77 | 3.45 | 30.81 |
| 1 | 33.4 | 3.32 | 0.13 | 456.44 |
| 2 | 21.32 | 1.46 | 2.18 | 228.02 |
| 3 | 10.51 | 1.21 | 1.32 | 378.98 |
| 4 | 9.26 | 0.2 | 4.96 | 454.29 |
| 5 | 3.93 | 0 | 0.01 | 214.16 |
| 6 | 2.41 | 0 | 0.01 | 102.47 |
| 7 | 1.16 | 0 | 0.58 | 24.1 |
| 8 | 2.1 | 0.03 | 1.75 | 14.35 |
| 9 | 0.84 | 0.01 | 0.4 | 12.11 |
| all | 89.58 | 7.0 | 14.79 | 1915.73 |

### Camera

1978.1 camera events per game, of which 409.6 are jumps over 20 map units (30.0 per minute).

### Sequences

473846 consecutive pairs within 1s, 2837.4 per game.

Top 30 bigrams:

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG4 > CG1 | 22872 | 136.96 |
| 2 | CG1 > CG4 | 20421 | 122.28 |
| 3 | CG3 > CG4 | 18062 | 108.16 |
| 4 | RightClick > Attack | 14347 | 85.91 |
| 5 | CG4 > CG3 | 13525 | 80.99 |
| 6 | CG1 > CG3 | 13321 | 79.77 |
| 7 | Attack > RightClick | 11244 | 67.33 |
| 8 | CG3 > CG1 | 10976 | 65.72 |
| 9 | CG1 > Attack | 9849 | 58.98 |
| 10 | CG1 > RightClick | 9769 | 58.5 |
| 11 | CG4 > CG2 | 6993 | 41.87 |
| 12 | CG1 > CG5 | 6986 | 41.83 |
| 13 | CG2 > CG3 | 6739 | 40.35 |
| 14 | CG2 > CG4 | 6671 | 39.95 |
| 15 | Attack > CG4 | 6636 | 39.74 |
| 16 | CG4 > CG5 | 6603 | 39.54 |
| 17 | RightClick > CG1 | 6107 | 36.57 |
| 18 | CG1 > CG2 | 6089 | 36.46 |
| 19 | CG5 > CG1 | 6012 | 36.0 |
| 20 | CG3 > CG5 | 5829 | 34.9 |
| 21 | RightClick > CG3 | 5798 | 34.72 |
| 22 | CG5 > CG3 | 5725 | 34.28 |
| 23 | CG2 > RightClick | 5567 | 33.34 |
| 24 | CG5 > CG6 | 5482 | 32.83 |
| 25 | CG3 > CG2 | 5330 | 31.92 |
| 26 | CG4 > RightClick | 5323 | 31.87 |
| 27 | RightClick > CG4 | 5118 | 30.65 |
| 28 | CG5 > CG4 | 5011 | 30.01 |
| 29 | Attack > CG3 | 4819 | 28.86 |
| 30 | CG2 > CG1 | 4779 | 28.62 |

Top 20 trigrams:

| # | Triple | Count | Per game |
|---|---|---|---|
| 1 | CG1 > CG4 > CG1 | 14793 | 88.58 |
| 2 | CG4 > CG1 > CG4 | 13714 | 82.12 |
| 3 | CG4 > CG3 > CG4 | 10500 | 62.87 |
| 4 | CG3 > CG4 > CG3 | 10427 | 62.44 |
| 5 | RightClick > Attack > RightClick | 7076 | 42.37 |
| 6 | CG1 > CG3 > CG1 | 6860 | 41.08 |
| 7 | Attack > RightClick > Attack | 6855 | 41.05 |
| 8 | CG3 > CG1 > CG3 | 6339 | 37.96 |
| 9 | CG2 > CG4 > CG2 | 4691 | 28.09 |
| 10 | CG4 > CG2 > CG4 | 4246 | 25.43 |
| 11 | CG1 > CG5 > CG1 | 3813 | 22.83 |
| 12 | CG5 > CG1 > CG5 | 3783 | 22.65 |
| 13 | CG3 > CG5 > CG3 | 3707 | 22.2 |
| 14 | CG5 > CG3 > CG5 | 3618 | 21.66 |
| 15 | CG5 > CG4 > CG5 | 3291 | 19.71 |
| 16 | CG4 > CG5 > CG4 | 3256 | 19.5 |
| 17 | CG3 > CG2 > CG3 | 3119 | 18.68 |
| 18 | CG2 > CG3 > CG2 | 2927 | 17.53 |
| 19 | CG6 > CG4 > CG6 | 2587 | 15.49 |
| 20 | CG3 > CG4 > CG1 | 2293 | 13.73 |

### TheCore 5.0 projection

87.0% of the 493755 sequence events (commands plus control-group recalls) map to a key. Share of those events per finger:

| Finger | Share of mapped events | Events |
|---|---|---|
| middle | 42.0% | 180426 |
| ring | 27.9% | 119994 |
| index | 24.9% | 106970 |
| pinky | 5.0% | 21619 |
| other | 0.1% | 513 |

**Same-finger repetition: 26.9%** of the 359112 within-1s pairs where both events map to a key land on the same finger. That splits into 4.9% the same key twice (a repeat no layout can move apart, mostly a control group recalled again) and **22.1% the same finger on a different key**, which is the part a layout controls.

Worst pairs (same finger, different key):

| # | Pair (finger) | Count | Per game |
|---|---|---|---|
| 1 | CG1 > CG3 (middle) | 13321 | 79.77 |
| 2 | CG3 > CG1 (middle) | 10976 | 65.72 |
| 3 | CG4 > CG2 (ring) | 6993 | 41.87 |
| 4 | CG1 > CG5 (middle) | 6986 | 41.83 |
| 5 | CG2 > CG4 (ring) | 6671 | 39.95 |
| 6 | CG5 > CG1 (middle) | 6012 | 36.0 |
| 7 | CG3 > CG5 (middle) | 5829 | 34.9 |
| 8 | CG5 > CG3 (middle) | 5725 | 34.28 |
| 9 | CG6 > TrainSCV (index) | 1751 | 10.49 |
| 10 | Attack > CG6 (index) | 1265 | 7.57 |
| 11 | CG0 > CG1 (middle) | 1167 | 6.99 |
| 12 | CG3 > CG0 (middle) | 732 | 4.38 |
| 13 | CG0 > CG3 (middle) | 676 | 4.05 |
| 14 | CG1 > CG0 (middle) | 485 | 2.9 |
| 15 | CG6 > ScannerSweep (index) | 421 | 2.52 |

Largest unmapped names: `RightClick` (60385), `UnloadTargetMedivac` (1993), `BuildBarracksTechLab` (303), `BuildFactoryTechLab` (154), `UpgradeTerranInfantryArmor2` (114), `UpgradeTerranInfantryWeapons2` (108), `CloakGhost` (104), `CancelTerranBuilding` (84), `BuildStarportTechLab` (77), `ResearchInterferenceMatrix` (68).

## Protoss

106 player-games, 1300 minutes played, 77137 commands: **727.7 per game, 59.4 per minute**. Control-group and camera numbers are per game.

### Top 40 abilities

These 40 are 95.8% of all Protoss commands.

| # | Ability | Count | Per game | Per minute | Share |
|---|---|---|---|---|---|
| 1 | RightClick | 33943 | 320.22 | 26.12 | 44.0% |
| 2 | Attack | 15142 | 142.85 | 11.65 | 19.63% |
| 3 | TrainProbe | 5416 | 51.09 | 4.17 | 7.02% |
| 4 | Blink | 2170 | 20.47 | 1.67 | 2.81% |
| 5 | ChronoBoostEnergyCost | 1778 | 16.77 | 1.37 | 2.3% |
| 6 | BuildPylon | 1709 | 16.12 | 1.32 | 2.22% |
| 7 | WarpInStalker | 1383 | 13.05 | 1.06 | 1.79% |
| 8 | WarpInZealot | 1078 | 10.17 | 0.83 | 1.4% |
| 9 | HoldPosition | 1014 | 9.57 | 0.78 | 1.31% |
| 10 | BuildGateway | 881 | 8.31 | 0.68 | 1.14% |
| 11 | ReturnCargo | 740 | 6.98 | 0.57 | 0.96% |
| 12 | AdeptPhaseShift | 708 | 6.68 | 0.54 | 0.92% |
| 13 | BuildAssimilator | 576 | 5.43 | 0.44 | 0.75% |
| 14 | BuildShieldBattery | 495 | 4.67 | 0.38 | 0.64% |
| 15 | Stop | 492 | 4.64 | 0.38 | 0.64% |
| 16 | UnloadTargetWarpPrism | 467 | 4.41 | 0.36 | 0.61% |
| 17 | BuildNexus | 396 | 3.74 | 0.3 | 0.51% |
| 18 | Patrol | 396 | 3.74 | 0.3 | 0.51% |
| 19 | BuildPhotonCannon | 378 | 3.57 | 0.29 | 0.49% |
| 20 | CancelLast | 342 | 3.23 | 0.26 | 0.44% |
| 21 | PsionicStorm | 338 | 3.19 | 0.26 | 0.44% |
| 22 | Revelation | 325 | 3.07 | 0.25 | 0.42% |
| 23 | TrainAdept | 295 | 2.78 | 0.23 | 0.38% |
| 24 | TrainObserver | 280 | 2.64 | 0.22 | 0.36% |
| 25 | PhasingMode | 273 | 2.58 | 0.21 | 0.35% |
| 26 | PurificationNovaTargeted | 270 | 2.55 | 0.21 | 0.35% |
| 27 | WarpInHighTemplar | 251 | 2.37 | 0.19 | 0.33% |
| 28 | ScanMove | 249 | 2.35 | 0.19 | 0.32% |
| 29 | TrainImmortal | 236 | 2.23 | 0.18 | 0.31% |
| 30 | BuildOracleStasisTrap | 203 | 1.92 | 0.16 | 0.26% |
| 31 | ObserverMorphtoObserverSiege | 203 | 1.92 | 0.16 | 0.26% |
| 32 | TransportMode | 199 | 1.88 | 0.15 | 0.26% |
| 33 | Gather | 197 | 1.86 | 0.15 | 0.26% |
| 34 | ArchonWarpSelection | 176 | 1.66 | 0.14 | 0.23% |
| 35 | TrainDisruptor | 164 | 1.55 | 0.13 | 0.21% |
| 36 | OracleWeapon | 160 | 1.51 | 0.12 | 0.21% |
| 37 | TrainStalker | 157 | 1.48 | 0.12 | 0.2% |
| 38 | ForceField | 150 | 1.42 | 0.12 | 0.19% |
| 39 | TrainColossus | 147 | 1.39 | 0.11 | 0.19% |
| 40 | OracleWeaponOff | 146 | 1.38 | 0.11 | 0.19% |

### Control groups

| Group | Set/game | Add/game | Steal/game | Recall/game |
|---|---|---|---|---|
| 0 | 2.44 | 2.64 | 2.71 | 79.75 |
| 1 | 18.42 | 12.52 | 2.58 | 289.03 |
| 2 | 14.44 | 1.21 | 10.98 | 186.99 |
| 3 | 4.16 | 0.4 | 4.97 | 157.46 |
| 4 | 2.9 | 0.46 | 5.72 | 185.46 |
| 5 | 2.0 | 2.18 | 1.3 | 200.95 |
| 6 | 1.18 | 1.92 | 1.72 | 113.55 |
| 7 | 0.35 | 0.49 | 0.89 | 27.63 |
| 8 | 0.36 | 0.54 | 0.49 | 45.19 |
| 9 | 0.66 | 0.46 | 1.78 | 17.31 |
| all | 46.91 | 22.82 | 33.14 | 1303.32 |

### Camera

1616.7 camera events per game, of which 435.7 are jumps over 20 map units (35.53 per minute).

### Sequences

199722 consecutive pairs within 1s, 1884.2 per game.

Top 30 bigrams:

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG1 > RightClick | 5528 | 52.15 |
| 2 | CG3 > CG4 | 5199 | 49.05 |
| 3 | CG1 > CG2 | 5188 | 48.94 |
| 4 | RightClick > CG1 | 5078 | 47.91 |
| 5 | CG1 > Attack | 4381 | 41.33 |
| 6 | CG2 > CG1 | 4308 | 40.64 |
| 7 | RightClick > Attack | 4249 | 40.08 |
| 8 | CG3 > CG5 | 3817 | 36.01 |
| 9 | CG5 > CG1 | 3703 | 34.93 |
| 10 | CG2 > RightClick | 3644 | 34.38 |
| 11 | CG5 > CG6 | 3458 | 32.62 |
| 12 | CG5 > CG3 | 3439 | 32.44 |
| 13 | CG4 > CG5 | 3305 | 31.18 |
| 14 | Attack > RightClick | 3293 | 31.07 |
| 15 | CG1 > CG5 | 3289 | 31.03 |
| 16 | CG4 > CG1 | 3011 | 28.41 |
| 17 | CG1 > CG4 | 2817 | 26.58 |
| 18 | RightClick > CG2 | 2648 | 24.98 |
| 19 | RightClick > CG4 | 2513 | 23.71 |
| 20 | CG1 > CG3 | 2465 | 23.25 |
| 21 | RightClick > CG5 | 2272 | 21.43 |
| 22 | CG4 > CG3 | 2042 | 19.26 |
| 23 | CG2 > CG5 | 2039 | 19.24 |
| 24 | RightClick > RightClick | 2025 | 19.1 |
| 25 | CG5 > CG2 | 1986 | 18.74 |
| 26 | CG3 > CG1 | 1947 | 18.37 |
| 27 | RightClick > CG3 | 1879 | 17.73 |
| 28 | CG2 > CG4 | 1862 | 17.57 |
| 29 | CG2 > CG3 | 1841 | 17.37 |
| 30 | CG4 > RightClick | 1726 | 16.28 |

Top 20 trigrams:

| # | Triple | Count | Per game |
|---|---|---|---|
| 1 | CG5 > CG3 > CG5 | 2691 | 25.39 |
| 2 | CG2 > CG1 > CG2 | 2659 | 25.08 |
| 3 | CG1 > CG2 > CG1 | 2509 | 23.67 |
| 4 | CG3 > CG5 > CG3 | 2481 | 23.41 |
| 5 | CG1 > CG5 > CG1 | 2068 | 19.51 |
| 6 | CG5 > CG1 > CG5 | 1965 | 18.54 |
| 7 | CG4 > CG3 > CG4 | 1582 | 14.92 |
| 8 | CG1 > CG4 > CG1 | 1578 | 14.89 |
| 9 | CG3 > CG4 > CG3 | 1418 | 13.38 |
| 10 | CG4 > CG1 > CG4 | 1365 | 12.88 |
| 11 | CG4 > CG5 > CG6 | 1298 | 12.25 |
| 12 | CG2 > CG5 > CG2 | 1294 | 12.21 |
| 13 | RightClick > Attack > RightClick | 1235 | 11.65 |
| 14 | RightClick > CG1 > Attack | 1193 | 11.25 |
| 15 | Attack > RightClick > Attack | 1126 | 10.62 |
| 16 | CG1 > RightClick > Attack | 1104 | 10.42 |
| 17 | CG5 > CG2 > CG5 | 1071 | 10.1 |
| 18 | CG3 > CG4 > CG5 | 1066 | 10.06 |
| 19 | CG4 > CG5 > CG4 | 958 | 9.04 |
| 20 | CG5 > CG4 > CG5 | 935 | 8.82 |

### TheCore 5.0 projection

83.5% of the 215289 sequence events (commands plus control-group recalls) map to a key. Share of those events per finger:

| Finger | Share of mapped events | Events |
|---|---|---|
| middle | 42.9% | 77082 |
| index | 24.8% | 44516 |
| ring | 24.6% | 44244 |
| pinky | 7.8% | 13963 |
| other | 0.0% | 55 |

**Same-finger repetition: 28.4%** of the 139244 within-1s pairs where both events map to a key land on the same finger. That splits into 6.0% the same key twice (a repeat no layout can move apart, mostly a control group recalled again) and **22.4% the same finger on a different key**, which is the part a layout controls.

Worst pairs (same finger, different key):

| # | Pair (finger) | Count | Per game |
|---|---|---|---|
| 1 | CG3 > CG5 (middle) | 3817 | 36.01 |
| 2 | CG5 > CG1 (middle) | 3703 | 34.93 |
| 3 | CG5 > CG3 (middle) | 3439 | 32.44 |
| 4 | CG1 > CG5 (middle) | 3289 | 31.03 |
| 5 | CG1 > CG3 (middle) | 2465 | 23.25 |
| 6 | CG3 > CG1 (middle) | 1947 | 18.37 |
| 7 | CG2 > CG4 (ring) | 1862 | 17.57 |
| 8 | CG0 > CG1 (middle) | 1383 | 13.05 |
| 9 | CG4 > CG2 (ring) | 1306 | 12.32 |
| 10 | Attack > CG6 (index) | 839 | 7.92 |
| 11 | CG6 > TrainProbe (index) | 765 | 7.22 |
| 12 | CG0 > CG3 (middle) | 514 | 4.85 |
| 13 | CG0 > CG5 (middle) | 395 | 3.73 |
| 14 | CG6 > WarpInStalker (index) | 395 | 3.73 |
| 15 | CG5 > CG0 (middle) | 380 | 3.58 |

Largest unmapped names: `RightClick` (33943), `UnloadTargetWarpPrism` (467), `ArchonWarpSelection` (176), `BatteryOvercharge` (129), `AdeptShadePhaseShiftCancel` (105), `ObserverSiegeMorphtoObserver` (103), `AdeptPhaseShiftCancel` (103), `LoadTarget` (78), `UpgradeGroundWeapons2` (63), `HallucinatePhoenix` (61).

## Zerg

101 player-games, 1404 minutes played, 88383 commands: **875.1 per game, 62.9 per minute**. Control-group and camera numbers are per game.

### Top 40 abilities

These 40 are 95.9% of all Zerg commands.

| # | Ability | Count | Per game | Per minute | Share |
|---|---|---|---|---|---|
| 1 | RightClick | 35103 | 347.55 | 25.0 | 39.72% |
| 2 | Attack | 15585 | 154.31 | 11.1 | 17.63% |
| 3 | MorphDrone | 5311 | 52.58 | 3.78 | 6.01% |
| 4 | MorphZergling | 3797 | 37.59 | 2.7 | 4.3% |
| 5 | SpawnLarva | 3576 | 35.41 | 2.55 | 4.05% |
| 6 | ScanMove | 2118 | 20.97 | 1.51 | 2.4% |
| 7 | MorphOverlord | 2087 | 20.66 | 1.49 | 2.36% |
| 8 | BuildCreepTumor | 1690 | 16.73 | 1.2 | 1.91% |
| 9 | MorphRoach | 1548 | 15.33 | 1.1 | 1.75% |
| 10 | CreepTumor | 1267 | 12.54 | 0.9 | 1.43% |
| 11 | ReturnCargo | 1022 | 10.12 | 0.73 | 1.16% |
| 12 | MorphToBaneling | 873 | 8.64 | 0.62 | 0.99% |
| 13 | MorphHydralisk | 793 | 7.85 | 0.56 | 0.9% |
| 14 | TrainQueen | 728 | 7.21 | 0.52 | 0.82% |
| 15 | RavagerCorrosiveBile | 718 | 7.11 | 0.51 | 0.81% |
| 16 | HoldPosition | 702 | 6.95 | 0.5 | 0.79% |
| 17 | BuildExtractor | 672 | 6.65 | 0.48 | 0.76% |
| 18 | SpawnChangeling | 643 | 6.37 | 0.46 | 0.73% |
| 19 | BuildHatchery | 641 | 6.35 | 0.46 | 0.73% |
| 20 | Gather | 575 | 5.69 | 0.41 | 0.65% |
| 21 | BurrowLurker | 565 | 5.59 | 0.4 | 0.64% |
| 22 | QueenTransfusion | 512 | 5.07 | 0.36 | 0.58% |
| 23 | Stop | 407 | 4.03 | 0.29 | 0.46% |
| 24 | Consume | 379 | 3.75 | 0.27 | 0.43% |
| 25 | BuildSporeCrawler | 375 | 3.71 | 0.27 | 0.42% |
| 26 | MorphToOverseer | 330 | 3.27 | 0.24 | 0.37% |
| 27 | UnburrowLurker | 307 | 3.04 | 0.22 | 0.35% |
| 28 | SetWorkerRally | 302 | 2.99 | 0.22 | 0.34% |
| 29 | MorphToRavager | 272 | 2.69 | 0.19 | 0.31% |
| 30 | FungalGrowth | 247 | 2.45 | 0.18 | 0.28% |
| 31 | RootSporeCrawler | 241 | 2.39 | 0.17 | 0.27% |
| 32 | UprootSporeCrawler | 214 | 2.12 | 0.15 | 0.24% |
| 33 | UnloadAll | 196 | 1.94 | 0.14 | 0.22% |
| 34 | CancelBuilding | 162 | 1.6 | 0.12 | 0.18% |
| 35 | MorphMutalisk | 151 | 1.5 | 0.11 | 0.17% |
| 36 | BuildNydusCanal | 142 | 1.41 | 0.1 | 0.16% |
| 37 | BuildEvolutionChamber | 141 | 1.4 | 0.1 | 0.16% |
| 38 | OverseerMorphtoOverseerSiegeMode | 141 | 1.4 | 0.1 | 0.16% |
| 39 | MorphToLurker | 138 | 1.37 | 0.1 | 0.16% |
| 40 | Patrol | 129 | 1.28 | 0.09 | 0.15% |

### Control groups

| Group | Set/game | Add/game | Steal/game | Recall/game |
|---|---|---|---|---|
| 0 | 1.9 | 2.18 | 1.19 | 111.6 |
| 1 | 15.78 | 20.5 | 4.26 | 572.62 |
| 2 | 19.97 | 34.67 | 20.31 | 419.0 |
| 3 | 8.2 | 3.5 | 17.33 | 332.71 |
| 4 | 8.24 | 3.81 | 15.23 | 312.62 |
| 5 | 3.03 | 1.23 | 2.65 | 488.83 |
| 6 | 2.2 | 0.19 | 0.51 | 45.86 |
| 7 | 0.96 | 0.02 | 0.46 | 15.47 |
| 8 | 1.06 | 0 | 0 | 9.04 |
| 9 | 0.98 | 0.58 | 0.36 | 22.75 |
| all | 62.32 | 66.68 | 62.3 | 2330.5 |

### Camera

2363.2 camera events per game, of which 600.8 are jumps over 20 map units (43.22 per minute).

### Sequences

311247 consecutive pairs within 1s, 3081.7 per game.

Top 30 bigrams:

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG5 > CG1 | 15533 | 153.79 |
| 2 | CG1 > CG5 | 13399 | 132.66 |
| 3 | CG1 > CG2 | 11898 | 117.8 |
| 4 | CG5 > CG2 | 9117 | 90.27 |
| 5 | CG1 > CG3 | 8547 | 84.62 |
| 6 | CG2 > CG1 | 8213 | 81.32 |
| 7 | CG2 > CG5 | 7580 | 75.05 |
| 8 | CG3 > CG1 | 7125 | 70.54 |
| 9 | CG1 > RightClick | 7042 | 69.72 |
| 10 | CG3 > CG4 | 6738 | 66.71 |
| 11 | CG2 > CG3 | 6323 | 62.6 |
| 12 | CG2 > RightClick | 6070 | 60.1 |
| 13 | RightClick > CG1 | 5567 | 55.12 |
| 14 | CG3 > CG5 | 5149 | 50.98 |
| 15 | CG2 > CG4 | 5122 | 50.71 |
| 16 | CG4 > CG5 | 4960 | 49.11 |
| 17 | CG4 > CG1 | 4719 | 46.72 |
| 18 | RightClick > CG5 | 4391 | 43.48 |
| 19 | CG5 > CG3 | 4159 | 41.18 |
| 20 | CG4 > CG3 | 4139 | 40.98 |
| 21 | CG1 > Attack | 3761 | 37.24 |
| 22 | CG1 > CG4 | 3745 | 37.08 |
| 23 | CG3 > CG2 | 3645 | 36.09 |
| 24 | CG4 > CG2 | 3393 | 33.59 |
| 25 | RightClick > Attack | 3353 | 33.2 |
| 26 | CG5 > CG0 | 3290 | 32.57 |
| 27 | RightClick > CG2 | 3189 | 31.57 |
| 28 | RightClick > CG4 | 3188 | 31.56 |
| 29 | CG4 > RightClick | 3145 | 31.14 |
| 30 | CG2 > Attack | 3142 | 31.11 |

Top 20 trigrams:

| # | Triple | Count | Per game |
|---|---|---|---|
| 1 | CG5 > CG1 > CG5 | 11505 | 113.91 |
| 2 | CG1 > CG5 > CG1 | 8940 | 88.51 |
| 3 | CG2 > CG5 > CG2 | 6498 | 64.34 |
| 4 | CG5 > CG2 > CG5 | 6128 | 60.67 |
| 5 | CG2 > CG1 > CG2 | 5064 | 50.14 |
| 6 | CG3 > CG1 > CG3 | 4852 | 48.04 |
| 7 | CG1 > CG2 > CG1 | 4832 | 47.84 |
| 8 | CG1 > CG3 > CG1 | 4350 | 43.07 |
| 9 | CG5 > CG3 > CG5 | 3127 | 30.96 |
| 10 | CG3 > CG5 > CG3 | 2947 | 29.18 |
| 11 | CG4 > CG3 > CG4 | 2861 | 28.33 |
| 12 | CG3 > CG4 > CG3 | 2597 | 25.71 |
| 13 | CG3 > CG2 > CG3 | 2440 | 24.16 |
| 14 | CG2 > CG3 > CG2 | 2425 | 24.01 |
| 15 | CG1 > CG4 > CG1 | 2386 | 23.62 |
| 16 | CG4 > CG1 > CG4 | 2201 | 21.79 |
| 17 | CG5 > CG0 > CG5 | 2099 | 20.78 |
| 18 | CG1 > CG2 > CG3 | 2063 | 20.43 |
| 19 | CG1 > CG2 > CG4 | 2007 | 19.87 |
| 20 | CG0 > CG5 > CG0 | 1951 | 19.32 |

### TheCore 5.0 projection

87.7% of the 323765 sequence events (commands plus control-group recalls) map to a key. Share of those events per finger:

| Finger | Share of mapped events | Events |
|---|---|---|
| middle | 53.5% | 152083 |
| ring | 27.4% | 77754 |
| index | 16.2% | 46110 |
| pinky | 2.8% | 7823 |
| other | 0.1% | 316 |

**Same-finger repetition: 35.9%** of the 239552 within-1s pairs where both events map to a key land on the same finger. That splits into 4.1% the same key twice (a repeat no layout can move apart, mostly a control group recalled again) and **31.8% the same finger on a different key**, which is the part a layout controls.

Worst pairs (same finger, different key):

| # | Pair (finger) | Count | Per game |
|---|---|---|---|
| 1 | CG5 > CG1 (middle) | 15533 | 153.79 |
| 2 | CG1 > CG5 (middle) | 13399 | 132.66 |
| 3 | CG1 > CG3 (middle) | 8547 | 84.62 |
| 4 | CG3 > CG1 (middle) | 7125 | 70.54 |
| 5 | CG3 > CG5 (middle) | 5149 | 50.98 |
| 6 | CG2 > CG4 (ring) | 5122 | 50.71 |
| 7 | CG5 > CG3 (middle) | 4159 | 41.18 |
| 8 | CG4 > CG2 (ring) | 3393 | 33.59 |
| 9 | CG5 > CG0 (middle) | 3290 | 32.57 |
| 10 | CG0 > CG1 (middle) | 2780 | 27.52 |
| 11 | CG0 > CG5 (middle) | 2568 | 25.43 |
| 12 | CG1 > CG0 (middle) | 778 | 7.7 |
| 13 | CG3 > CG0 (middle) | 586 | 5.8 |
| 14 | CG4 > CG9 (ring) | 350 | 3.47 |
| 15 | CG9 > CG4 (ring) | 274 | 2.71 |

Largest unmapped names: `RightClick` (35103), `SpawnLarva` (3576), `BuildNydusCanal` (142), `Abduct` (115), `UnloadTargetOverlord` (89), `OverseerSiegeModeMorphtoOverseer` (67), `ResearchZergMissileWeaponsLevel2` (52), `ResearchZergGroundArmorsLevel2` (50), `ResearchZergMeleeWeaponsLevel2` (50), `EvolveCentrifugalHooks` (45).

## Reproducing

```
# fetch the replays: see replays/README.md
uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
    extract replays/ -o ~/scratch/thecore/events.jsonl.gz
uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
    report ~/scratch/thecore/events.jsonl.gz \
    -o wiki/sc2-command-sequences.md --summary thecore/sequences-summary.json
# or rebuild this page from the committed summary alone:
python3 tools/sc2_sequences.py report thecore/sequences-summary.json \
    -o wiki/sc2-command-sequences.md
```
