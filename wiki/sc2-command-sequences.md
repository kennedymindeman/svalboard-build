---
type: Reference
title: SC2 command sequences, measured
description: Command frequencies, control-group and camera use, and event sequences measured from 187 professional StarCraft II replays, projected onto TheCore 5.0's keys and fingers.
tags: [starcraft, thecore, gaming, measurement, hotkeys]
source: "IEM Katowice 2024 main event; measured with tools/sc2_sequences.py"
---

# SC2 command sequences, measured

Every number on this page is measured from replays, not estimated. The set is **IEM Katowice 2024 main event**: 187 games, patch 5.0.12.91115, parsed with sc2reader at `load_level=4`.

`tools/sc2_sequences.py` produced both this page and `thecore/sequences-summary.json`, which holds the same aggregates; the page can be rebuilt from that file alone, without the replays. `replays/README.md` says how to fetch the set again.

## What is counted

- **Command**: one `CommandEvent` in the replay, i.e. one ability the player issued. Right-clicks (`RightClick`) are in the counts and are a mouse action, not a key.
- Follow-up `UpdateTargetPoint`/`UpdateTargetUnit` events (a target dragged while the mouse is down) are counted separately and left out of every rate below; including them would roughly double the right-click count.
- **Control group**: `set` (Shift+key in TheCore), `add` (Shift+Alt+key), `steal` (Ctrl+key, the steal-and-add and steal-and-set update types), `recall` (the bare key).
- **Camera jump**: two successive camera positions more than 20 map units apart. The distribution of that distance is bimodal, with scrolling below ~8 units, a trough at 14-20 and a second mode above it, so 20 sits in the trough. Replays record where the camera went, never which key moved it, so minimap clicks and follow-unit land in the same bucket: read jumps as an upper bound on camera hotkey presses.
- **Sequence**: consecutive events by the same player no more than 1 s apart, over a stream of commands and control-group recalls (the two things a hand does between camera moves). Game seconds are real seconds here: these are LotV replays on Faster, where sc2reader's speed factor is 1.0.
- **TheCore projection**: sc2reader ability names normalised to the command names in `thecore/TheCore_5.0_Right_Plus.SC2Hotkeys`, then to that file's key and to the finger that presses it (`FINGERS` in `tools/thecore_keys.py`). Modifiers ride the thumb in TheCore, so a modified binding is counted on the finger of its base key.

## Coverage

All 187 replays in the pack parsed; none failed, so no s2protocol fallback was needed.

| Race | Player-games | Commands | Distinct abilities | On a TheCore key | Mouse (right-click) | No binding found | Unnamed by sc2reader |
|---|---|---|---|---|---|---|---|
| Terran | 167 | 173827 | 149 | 63.4% | 34.7% | 1.9% | 15 |
| Protoss | 106 | 77137 | 115 | 54.1% | 44.0% | 1.9% | 16 |
| Zerg | 101 | 88383 | 135 | 55.1% | 39.7% | 5.1% | 0 |

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

1978.1 camera events per game, of which 409.7 are jumps over 20 map units (30.01 per minute).

### Sequences

456808 consecutive pairs within 1s, 2735.4 per game.

Top 30 bigrams:

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG4 > CG1 | 21432 | 128.34 |
| 2 | CG1 > CG4 | 19905 | 119.19 |
| 3 | CG3 > CG4 | 17898 | 107.17 |
| 4 | RightClick > Attack | 13446 | 80.51 |
| 5 | CG1 > CG3 | 13230 | 79.22 |
| 6 | CG4 > CG3 | 13229 | 79.22 |
| 7 | Attack > RightClick | 10746 | 64.35 |
| 8 | CG3 > CG1 | 10724 | 64.22 |
| 9 | CG1 > RightClick | 9218 | 55.2 |
| 10 | CG1 > Attack | 9217 | 55.19 |
| 11 | CG1 > CG5 | 6851 | 41.02 |
| 12 | CG4 > CG2 | 6699 | 40.11 |
| 13 | CG2 > CG3 | 6666 | 39.92 |
| 14 | CG2 > CG4 | 6519 | 39.04 |
| 15 | Attack > CG4 | 6368 | 38.13 |
| 16 | CG4 > CG5 | 6278 | 37.59 |
| 17 | CG1 > CG2 | 5967 | 35.73 |
| 18 | CG5 > CG1 | 5869 | 35.14 |
| 19 | RightClick > CG1 | 5738 | 34.36 |
| 20 | CG3 > CG5 | 5714 | 34.22 |
| 21 | CG5 > CG6 | 5498 | 32.92 |
| 22 | RightClick > CG3 | 5308 | 31.78 |
| 23 | CG5 > CG3 | 5290 | 31.68 |
| 24 | CG2 > RightClick | 5289 | 31.67 |
| 25 | CG4 > RightClick | 5271 | 31.56 |
| 26 | CG3 > CG2 | 5157 | 30.88 |
| 27 | RightClick > CG4 | 4772 | 28.57 |
| 28 | Attack > CG3 | 4683 | 28.04 |
| 29 | CG2 > CG1 | 4572 | 27.38 |
| 30 | CG5 > CG4 | 4327 | 25.91 |

Top 20 trigrams:

| # | Triple | Count | Per game |
|---|---|---|---|
| 1 | CG1 > CG4 > CG1 | 13091 | 78.39 |
| 2 | CG4 > CG1 > CG4 | 12262 | 73.43 |
| 3 | CG4 > CG3 > CG4 | 10228 | 61.25 |
| 4 | CG3 > CG4 > CG3 | 10080 | 60.36 |
| 5 | CG1 > CG3 > CG1 | 6722 | 40.25 |
| 6 | RightClick > Attack > RightClick | 6602 | 39.53 |
| 7 | Attack > RightClick > Attack | 6488 | 38.85 |
| 8 | CG3 > CG1 > CG3 | 6191 | 37.07 |
| 9 | CG2 > CG4 > CG2 | 4304 | 25.77 |
| 10 | CG4 > CG2 > CG4 | 3906 | 23.39 |
| 11 | CG5 > CG1 > CG5 | 3673 | 21.99 |
| 12 | CG1 > CG5 > CG1 | 3657 | 21.9 |
| 13 | CG3 > CG5 > CG3 | 3246 | 19.44 |
| 14 | CG5 > CG3 > CG5 | 3219 | 19.28 |
| 15 | CG3 > CG2 > CG3 | 3031 | 18.15 |
| 16 | CG2 > CG3 > CG2 | 2828 | 16.93 |
| 17 | CG4 > CG5 > CG4 | 2491 | 14.92 |
| 18 | CG5 > CG4 > CG5 | 2474 | 14.81 |
| 19 | CG3 > CG4 > CG1 | 2238 | 13.4 |
| 20 | CG1 > CG3 > CG4 | 2146 | 12.85 |

### TheCore 5.0 projection

87.1% of the 493755 sequence events (commands plus control-group recalls) map to a key. Share of those events per finger:

| Finger | Share of mapped events | Events |
|---|---|---|
| middle | 42.0% | 180426 |
| ring | 27.9% | 119994 |
| index | 24.9% | 106970 |
| pinky | 5.0% | 21619 |
| other | 0.2% | 1047 |

**Same-finger repetition: 28.0%** of the 350126 within-1s pairs where both events map to a key land on the same finger.

Worst pairs:

| # | Pair (finger) | Count | Per game |
|---|---|---|---|
| 1 | CG1 > CG3 (middle) | 13230 | 79.22 |
| 2 | CG3 > CG1 (middle) | 10724 | 64.22 |
| 3 | CG1 > CG5 (middle) | 6851 | 41.02 |
| 4 | CG4 > CG2 (ring) | 6699 | 40.11 |
| 5 | CG2 > CG4 (ring) | 6519 | 39.04 |
| 6 | CG5 > CG1 (middle) | 5869 | 35.14 |
| 7 | CG3 > CG5 (middle) | 5714 | 34.22 |
| 8 | CG5 > CG3 (middle) | 5290 | 31.68 |
| 9 | CG3 > CG3 (middle) | 4164 | 24.93 |
| 10 | CG4 > CG4 (ring) | 4087 | 24.47 |
| 11 | CG1 > CG1 (middle) | 3193 | 19.12 |
| 12 | UseStimpack > Attack (index) | 1852 | 11.09 |
| 13 | CG6 > TrainSCV (index) | 1712 | 10.25 |
| 14 | CG2 > CG2 (ring) | 1663 | 9.96 |
| 15 | CG5 > CG5 (middle) | 1412 | 8.46 |

Largest unmapped names: `RightClick` (60385), `UnloadTargetMedivac` (1993), `UpgradeTerranInfantryArmor2` (114), `UpgradeTerranInfantryWeapons2` (108), `CloakGhost` (104), `CancelTerranBuilding` (84), `ResearchInterferenceMatrix` (68), `UpgradeTerranInfantryWeapons3` (65), `DecloakGhost` (61), `UpgradeTerranInfantryArmor3` (60).

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

1616.7 camera events per game, of which 435.7 are jumps over 20 map units (35.54 per minute).

### Sequences

188138 consecutive pairs within 1s, 1774.9 per game.

Top 30 bigrams:

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG1 > RightClick | 5272 | 49.74 |
| 2 | CG3 > CG4 | 5150 | 48.58 |
| 3 | CG1 > CG2 | 5089 | 48.01 |
| 4 | RightClick > CG1 | 4646 | 43.83 |
| 5 | CG2 > CG1 | 4173 | 39.37 |
| 6 | CG1 > Attack | 4077 | 38.46 |
| 7 | RightClick > Attack | 3683 | 34.75 |
| 8 | CG5 > CG1 | 3557 | 33.56 |
| 9 | CG2 > RightClick | 3464 | 32.68 |
| 10 | CG5 > CG6 | 3400 | 32.08 |
| 11 | CG3 > CG5 | 3361 | 31.71 |
| 12 | CG4 > CG5 | 3250 | 30.66 |
| 13 | CG1 > CG5 | 3170 | 29.91 |
| 14 | Attack > RightClick | 2940 | 27.74 |
| 15 | CG4 > CG1 | 2886 | 27.23 |
| 16 | CG5 > CG3 | 2824 | 26.64 |
| 17 | CG1 > CG4 | 2680 | 25.28 |
| 18 | RightClick > CG2 | 2498 | 23.57 |
| 19 | CG1 > CG3 | 2399 | 22.63 |
| 20 | RightClick > CG4 | 2302 | 21.72 |
| 21 | CG5 > CG5 | 2135 | 20.14 |
| 22 | RightClick > CG5 | 2055 | 19.39 |
| 23 | CG2 > CG5 | 1937 | 18.27 |
| 24 | CG4 > CG3 | 1914 | 18.06 |
| 25 | CG5 > CG2 | 1853 | 17.48 |
| 26 | CG3 > CG1 | 1831 | 17.27 |
| 27 | CG2 > CG3 | 1806 | 17.04 |
| 28 | CG2 > CG4 | 1789 | 16.88 |
| 29 | RightClick > RightClick | 1764 | 16.64 |
| 30 | RightClick > CG3 | 1763 | 16.63 |

Top 20 trigrams:

| # | Triple | Count | Per game |
|---|---|---|---|
| 1 | CG2 > CG1 > CG2 | 2575 | 24.29 |
| 2 | CG1 > CG2 > CG1 | 2418 | 22.81 |
| 3 | CG1 > CG5 > CG1 | 1933 | 18.24 |
| 4 | CG5 > CG1 > CG5 | 1839 | 17.35 |
| 5 | CG5 > CG3 > CG5 | 1722 | 16.25 |
| 6 | CG3 > CG5 > CG3 | 1586 | 14.96 |
| 7 | CG1 > CG4 > CG1 | 1489 | 14.05 |
| 8 | CG4 > CG3 > CG4 | 1482 | 13.98 |
| 9 | CG3 > CG4 > CG3 | 1359 | 12.82 |
| 10 | CG4 > CG5 > CG6 | 1299 | 12.25 |
| 11 | CG4 > CG1 > CG4 | 1257 | 11.86 |
| 12 | CG2 > CG5 > CG2 | 1069 | 10.08 |
| 13 | CG3 > CG4 > CG5 | 1039 | 9.8 |
| 14 | RightClick > CG1 > Attack | 1003 | 9.46 |
| 15 | RightClick > Attack > RightClick | 945 | 8.92 |
| 16 | CG1 > RightClick > Attack | 944 | 8.91 |
| 17 | CG1 > CG3 > CG4 | 924 | 8.72 |
| 18 | CG4 > CG5 > CG4 | 883 | 8.33 |
| 19 | CG5 > CG4 > CG5 | 869 | 8.2 |
| 20 | CG5 > CG2 > CG5 | 861 | 8.12 |

### TheCore 5.0 projection

83.5% of the 215289 sequence events (commands plus control-group recalls) map to a key. Share of those events per finger:

| Finger | Share of mapped events | Events |
|---|---|---|
| middle | 42.9% | 77082 |
| index | 24.7% | 44352 |
| ring | 24.6% | 44244 |
| pinky | 7.8% | 13963 |
| other | 0.1% | 219 |

**Same-finger repetition: 28.8%** of the 132617 within-1s pairs where both events map to a key land on the same finger.

Worst pairs:

| # | Pair (finger) | Count | Per game |
|---|---|---|---|
| 1 | CG5 > CG1 (middle) | 3557 | 33.56 |
| 2 | CG3 > CG5 (middle) | 3361 | 31.71 |
| 3 | CG1 > CG5 (middle) | 3170 | 29.91 |
| 4 | CG5 > CG3 (middle) | 2824 | 26.64 |
| 5 | CG1 > CG3 (middle) | 2399 | 22.63 |
| 6 | CG5 > CG5 (middle) | 2135 | 20.14 |
| 7 | CG3 > CG1 (middle) | 1831 | 17.27 |
| 8 | CG2 > CG4 (ring) | 1789 | 16.88 |
| 9 | CG0 > CG1 (middle) | 1367 | 12.9 |
| 10 | CG1 > CG1 (middle) | 1349 | 12.73 |
| 11 | CG4 > CG2 (ring) | 1219 | 11.5 |
| 12 | CG6 > CG6 (index) | 999 | 9.42 |
| 13 | CG0 > CG0 (middle) | 980 | 9.25 |
| 14 | Attack > CG6 (index) | 787 | 7.42 |
| 15 | CG3 > CG3 (middle) | 760 | 7.17 |

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

2363.2 camera events per game, of which 600.9 are jumps over 20 map units (43.22 per minute).

### Sequences

299726 consecutive pairs within 1s, 2967.6 per game.

Top 30 bigrams:

| # | Pair | Count | Per game |
|---|---|---|---|
| 1 | CG5 > CG1 | 14609 | 144.64 |
| 2 | CG1 > CG5 | 13524 | 133.9 |
| 3 | CG1 > CG2 | 11796 | 116.79 |
| 4 | CG1 > CG3 | 8390 | 83.07 |
| 5 | CG2 > CG1 | 7998 | 79.19 |
| 6 | CG5 > CG2 | 7983 | 79.04 |
| 7 | CG2 > CG5 | 7221 | 71.5 |
| 8 | CG3 > CG1 | 6783 | 67.16 |
| 9 | CG3 > CG4 | 6650 | 65.84 |
| 10 | CG1 > RightClick | 6400 | 63.37 |
| 11 | CG2 > CG3 | 6225 | 61.63 |
| 12 | CG2 > RightClick | 5764 | 57.07 |
| 13 | RightClick > CG1 | 5467 | 54.13 |
| 14 | CG2 > CG4 | 4977 | 49.28 |
| 15 | CG4 > CG5 | 4907 | 48.58 |
| 16 | CG3 > CG5 | 4902 | 48.53 |
| 17 | CG4 > CG1 | 4205 | 41.63 |
| 18 | RightClick > CG5 | 3955 | 39.16 |
| 19 | CG4 > CG3 | 3878 | 38.4 |
| 20 | CG5 > CG3 | 3841 | 38.03 |
| 21 | CG5 > CG5 | 3739 | 37.02 |
| 22 | CG1 > CG4 | 3582 | 35.47 |
| 23 | CG1 > Attack | 3444 | 34.1 |
| 24 | CG3 > CG2 | 3438 | 34.04 |
| 25 | CG4 > CG2 | 3203 | 31.71 |
| 26 | CG4 > RightClick | 3167 | 31.36 |
| 27 | RightClick > CG2 | 3080 | 30.5 |
| 28 | RightClick > Attack | 3066 | 30.36 |
| 29 | CG5 > CG0 | 3037 | 30.07 |
| 30 | RightClick > CG4 | 2924 | 28.95 |

Top 20 trigrams:

| # | Triple | Count | Per game |
|---|---|---|---|
| 1 | CG5 > CG1 > CG5 | 10877 | 107.69 |
| 2 | CG1 > CG5 > CG1 | 8327 | 82.45 |
| 3 | CG2 > CG5 > CG2 | 5152 | 51.01 |
| 4 | CG2 > CG1 > CG2 | 4878 | 48.3 |
| 5 | CG5 > CG2 > CG5 | 4783 | 47.36 |
| 6 | CG1 > CG2 > CG1 | 4659 | 46.13 |
| 7 | CG3 > CG1 > CG3 | 4502 | 44.57 |
| 8 | CG1 > CG3 > CG1 | 3997 | 39.57 |
| 9 | CG4 > CG3 > CG4 | 2655 | 26.29 |
| 10 | CG5 > CG3 > CG5 | 2629 | 26.03 |
| 11 | CG3 > CG5 > CG3 | 2475 | 24.5 |
| 12 | CG3 > CG4 > CG3 | 2351 | 23.28 |
| 13 | CG3 > CG2 > CG3 | 2290 | 22.67 |
| 14 | CG2 > CG3 > CG2 | 2270 | 22.48 |
| 15 | CG1 > CG2 > CG3 | 2032 | 20.12 |
| 16 | CG1 > CG2 > CG4 | 1968 | 19.49 |
| 17 | CG1 > CG4 > CG1 | 1877 | 18.58 |
| 18 | CG1 > CG3 > CG4 | 1846 | 18.28 |
| 19 | CG4 > CG1 > CG4 | 1738 | 17.21 |
| 20 | CG0 > CG1 > CG2 | 1672 | 16.55 |

### TheCore 5.0 projection

87.8% of the 323765 sequence events (commands plus control-group recalls) map to a key. Share of those events per finger:

| Finger | Share of mapped events | Events |
|---|---|---|
| middle | 53.5% | 152083 |
| ring | 27.4% | 77754 |
| index | 16.2% | 46110 |
| pinky | 2.8% | 7823 |
| other | 0.1% | 351 |

**Same-finger repetition: 37.3%** of the 232478 within-1s pairs where both events map to a key land on the same finger.

Worst pairs:

| # | Pair (finger) | Count | Per game |
|---|---|---|---|
| 1 | CG5 > CG1 (middle) | 14609 | 144.64 |
| 2 | CG1 > CG5 (middle) | 13524 | 133.9 |
| 3 | CG1 > CG3 (middle) | 8390 | 83.07 |
| 4 | CG3 > CG1 (middle) | 6783 | 67.16 |
| 5 | CG2 > CG4 (ring) | 4977 | 49.28 |
| 6 | CG3 > CG5 (middle) | 4902 | 48.53 |
| 7 | CG5 > CG3 (middle) | 3841 | 38.03 |
| 8 | CG5 > CG5 (middle) | 3739 | 37.02 |
| 9 | CG4 > CG2 (ring) | 3203 | 31.71 |
| 10 | CG5 > CG0 (middle) | 3037 | 30.07 |
| 11 | CG0 > CG1 (middle) | 2770 | 27.43 |
| 12 | CG0 > CG5 (middle) | 2399 | 23.75 |
| 13 | CG4 > CG4 (ring) | 2389 | 23.65 |
| 14 | CG1 > CG1 (middle) | 2148 | 21.27 |
| 15 | CG2 > CG2 (ring) | 2045 | 20.25 |

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
