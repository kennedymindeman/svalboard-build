---
type: Reference
title: TheCore's method on a Svalboard
description: TheCore's own rules for ranking keys and commands, what its shipped files actually measure, what the Svalboard wiki knows about key ease, a derived recipe that applies the method to a five-key-per-finger cluster board, and a computed assignment for one left hand plus a held layer.
tags: [svalboard, thecore, starcraft, gaming, layout]
source: "TheCore Google Drive: TheCore Handbook - The logic behind the layout.docx, TheCore 5.0 Spreadsheet, TheCore 6.0 Spreadsheet, Customization Ideas - Tweak TheCore to fit you!.docx, F.A.Q_.docx, TheCore_5.0_Right_Plus.SC2Hotkeys, TheCore6g_right_US_qwerty.SC2Hotkeys; Svalboard wiki pages ergonomics-and-fit, faq, firmware-and-config, gaming, open-questions, pointing-devices, suppliers-and-parts"
---

# TheCore's method on a Svalboard

Message ids in parentheses are the last 6 digits of Discord snowflakes; `S:` ids resolve in `discord/raw/channel-1124364902811844739.jsonl` (Svalboard #general), and a few 6-digit suffixes collide in that 43k-message export, so disambiguate by date if a lookup returns two hits. TheCore's drive documents are cited by file name; see [`../thecore/README.md`](../thecore/README.md) for which files are in this repo and where the rest live. The two `.SC2Hotkeys` files are counted with `tools/thecore_keys.py`.

This page is about TheCore's *method*, not its layout. For the layout itself and for what the two Discords say about running TheCore on this hardware, see [Svalboard and TheCore](/svalboard-and-thecore.md).

## 1. What the method is, in TheCore's own words

**Keys are ranked by reach distance, and the ranking was asserted, not measured.** The 5.0 spreadsheet's first tab carries three rows, `Right Keyscore`, `Left Keyscore` and `Key Score`, where Key Score is the formula `Right Keyscore + Left Keyscore` for the mirrored pair in that column. Lower is better: `0.5` on the home column, `12` and `18` at the far columns (5.0 sheet). The two halves are not judged equal, so column G scores `3.0` on the right and `2.0` on the left. Nothing in the sheet says where those numbers came from.

**The only borrowed number in the method is a typing-optimizer figure about home keys.** Handbook, in "Humility in Measurement": *"Zone 1: Home keys / This is something that we can lift directly from the typing optimizers in that home keys are 2-5 times faster to press than a key adjacent to the home keys. / Zone 2: 1 away from home keys / The keys follow this pattern even within the keyscore method (which had distance as one of it's criteria). / Zone 3: 2 away from home keys / There are very few bindings this far out, it's clear that we want to avoid this area when possible."* No study is named.

**The author retired the numeric score and kept the zones.** Handbook: *"Previously TheCore has been built on a key-score system developed by myself and FoxyMayhem for the initial version of TheCore in 2012. This system based on our knowledge is much too specific a claim to make. To say that M is in general easier to press than H is not really a fair claim to try and make. We did it because we had to pick something to choose one over the other."* A "key speed zone" is just a distance band of keys treated as equally cheap. 5.0 ships three zones (`Zone 1: Home Keys`, `Zone 2: One Key Away`, `Zone 3: Two Keys away`); 6.0 ships four and deletes the keyscore rows entirely. Two per-key flags survive alongside the zones: a finger letter (`p`, `i`, `m`, `r`, `t`) on the `Control Groups Cameras` tab, and a Rapid Fire or Precision mark. The rule for the flag, from `Customization Ideas - Tweak TheCore to fit you!.docx`: *"If you want to be able to spam an ability, give it a rapid fire key, and if you need to be precise when casting an ability, give it a precision key."*

**Reaching is the thing being minimised.** Handbook: *"Minimize reaching / Reaching increases learn time / The further away a key is, the longer it takes to develop the ability to press it without looking (full mastery) / Reaching decreases efficiency / The longer the reach, the more time it takes / Milliseconds matter in RTS / Multiplied by 100s of actions per minute, small gains add up"*.

**Commands are ranked twice: by class, then by ordinal slot.** The spreadsheets' own class names are `WORKERS`, `TOGGLE PAIRS`, `STRUCTURE BUILDING`, `UNIT PRODUCTION`, `MORPH / SPAWN UNIT` and `UPGRADES`, each with its grouping rule, for example *"Structures are grouped in categories like anti-air static defenses, gas structure, town hall, etc. When possible they are grouped with unit production like dark shrine and dark templar on the same key."* (5.0 sheet). Above those sit the global slots, named and numbered in priority order: `Command 1`-`Command 13`, `CG 1`-`CG 10` (CG is a control group, a saved selection of units recalled by one key), `Jump to Cam 1`-`8`, `Create Cam`, `Add/Steal CG`, `Top Bar Power 1`-`4`, `Base Camera`, `Idle Worker`, `Special Command 1`, `Auto-Cast`. `Command 1` sits on the pinky home key and the numbering runs outward.

**The ranking is author judgment and says so.** Handbook: *"The differences between most of these keys is quite small. Especially with upgrades and structure building, it seems better to focus on aligning these to make learning as easy as possible. Low time sensitivity and low frequency on average means we can align these at a negligible cost to overall efficiency. Unfortunately we kind of have to make the best guess here since we don't have programs that can calculate the efficiency over a sample of games. Since unit production is the only high frequency category, the priority goes to unit production first."* There is no frequency column, no APM count and no replay sample anywhere in the two spreadsheets.

**The combining rule has two halves.** Handbook: *"Principles for applying TheCore to Starcraft 2 / Efficiency > Intuition / When selecting the key zone for the binding. / Intuition > Efficiency / When moving bindings within key zones."* So the zone is picked by cost against frequency and time sensitivity, and the key inside the zone is picked by whatever is easiest to remember. Restated for 5.0: *"In TheCore 5.0 we are changing the priority of intuition to be over efficiency within 3 zones of keys."*

**Finger roles come from the sequence a command sits in, not from the command alone.** Handbook: *"Other Global Keys / Select All Army / Should be followed by attack or CG / Attack is index / CGs are ring middle / Select All Army should be on the pinky"*, and *"Idle Worker / Should be followed by right click or build menu (terran) / Build menus are index, pinky, thumb / Idle worker should be on the ring or middle finger"*, and *"Larva Injects / Camera keys on Index, Middle, and Ring finger, inject on Pinky finger / Optimal lack of finger repetition"*.

**The thumb holds one modifier combination through a whole sequence.** That is the rule the modifier assignment exists to serve, stated in `F.A.Q_.docx`: *"Jumping to a rally camera is usually followed by adding units into a control group. By recalling this camera with control, we take 1-2 actions out of the sequence for adding units into control groups: / Ctrl+camera jumps to location / Ctrl+click selects unit type / Ctrl+cg add/steals to cg / If these modifiers were not lined up, the thumb would have to move back and forth pressing different modifier combinations for each action. ... This is a technique we call modifier synergy. It is the primary reason for changing which modifiers are used for cameras and control groups."* The FAQ also gives the anatomical reason the thumb has the job: *"TheCore has the advantage of utilizing the naturally occurring large gap between the thumb and first finger (when compared to gaps between the non-thumb fingers). By placing the thumb on shift, the number comfortable combinations (Shift+Key) are much higher than when the pinky is on shift"*.

**Same-finger repetition is the central prohibition.** Handbook: *"Utilize alternation / Using the same finger twice in a row decreases speed and comfort over time / Optimize for frequent and time sensitive action sequences / Ensure alternating fingers to achieve optimization"*, backed by *"Utilize all five fingers"*. An alternate is a second key bound to the same command, and alternates exist mainly to break repetition: *"By default, unload is on the index finger, but if the spell you want to cast is also on your index finger, that would mean that you would have to perform two tasks in a row with the same finger. Having an alternate hotkey for unload on the pinky finger will reduce the finger repetition in these scenarios."* (`Customization Ideas`). Alternates must earn their place: *"Alternates increase complexity, we want to be sure they're paying rent."* (Handbook).

**Two more prohibitions.** Auto-cast collides with the Alt camera layer, Handbook: *"Auto-cast / Must be on ability 4 or higher / Alt+abilities 1-3 recall a camera / If an auto ability was on ability 1, 2, or 3 the camera would move every time auto-cast was toggled"*. And commands judged harmful are banished, meaning bound deliberately out of reach rather than unbound, `F.A.Q_.docx`: *"Banished functions are set to Ctrl+Shift+Alt+key, this is to avoid conflicts with other functions. Functions are banished when they are considered to form bad habits by default or if they're considered unimportant/useless"*. They stay bound because of the Handbook's *"Can't leave unbound without causing issues for AltGr keyboards"*.

**Context beats raw key cost.** Handbook: *"If we assume that town hall control group is on 3/0 then the follow up key must be measured from that location and not the home keys. This makes 2 and Q much better keys in context since the hand has already moved part of the way to the key. Making exceptions for action sequences is very important."*

**The mouse carries almost nothing, and all of it optional.** The only mouse suggestions in the corpus are *"Change 'select all warp gates' to back mouse button"* (Handbook), Shift+Alt+Right Mouse Click as an alternate for Smart Command (`Customization Ideas`), and left click in the ability-target alternate list. There is no mouse-button budget.

**6.0 changed the mechanism without documenting why.** The keyscore rows are gone, there is a fourth zone, the modifier set is re-cut into seven columns (`No-modifer` (sic) `/ Ctrl / Shift / Alt / Ctrl+Shift / Alt+Shift / Ctrl+Alt`), and a per-structure priority rank appears as annotations like `1 k;` and `3 pk`. The Handbook has a dated section for the 5.0 rework and none for 6.0, and no document defines the rank notation.

**What the documents never cover:** split, ortholinear, columnar or finger-cluster keyboards, and any per-key timing, error-rate or force measurement. The only physical variables the corpus recognises are keyboard region, laptop versus desktop, mouse hand, and which modifier keys sit next to Ctrl.

## 2. What the shipped files measure

Measured with `tools/thecore_keys.py`. `TheCore_5.0_Right_Plus.SC2Hotkeys` holds 1,434 bindings on 53 keys; `TheCore6g_right_US_qwerty.SC2Hotkeys` holds 1,314 on 57. Per finger, 5.0 Right Plus uses 10 index keys, 4 middle, 4 ring, 9 pinky and 0 thumb (the modifiers are never bound bare), with the remaining 26 keys outside the finger chart. 6.0 Right uses 11 index, 4 middle, 4 ring and 9 pinky.

The counts split the fingers into two jobs. Index and pinky keys carry hundreds of plain bindings each, because each one is a `Command n` slot that every unit's command card reuses: `J` 300 bindings (297 plain), `;` 257, `-` 188, `[` 107, `P` 102, `M` 85, `H` 75, `N` 68. Middle and ring keys carry 5 to 10 bindings each, roughly one per modifier combination, because they are control-group and camera slots: `O`, `L` and `9` (middle) and `I` (ring) each carry 7, one for plain, Shift, Ctrl, Ctrl+Shift, Alt+Shift, Alt and Alt+Ctrl; `K` carries 10, four of them plain; `8`, `,` and `.` carry 5.

Modifier meanings in 5.0 Right Plus: plain selects, Shift creates a control group, Ctrl adds or steals to one, Alt jumps to a camera view, Alt+Ctrl saves a camera (the Handbook's *"Control+Alt+Cam key to set camera"*), and Ctrl+Shift+Alt is where banished commands are parked. Every finger group has exactly one Alt+Ctrl+Shift binding on several keys, which is the banishment mechanism showing up in the count.

The 5.0 spreadsheet's important-keys table, condensed by finger (the sheet's own finger letters and its right-hand keys):

| Finger | Right keys | Plain | Shift | Ctrl | Ctrl-Shift | Alt / Ctrl-Alt (Plus) |
|---|---|---|---|---|---|---|
| p (pinky) | J, H, M, N, G, B | Command 1, 6, 8, 9, 12, 13 | same Command (shift-queue) | Jump to Cam 1 on J, Base Camera on H | Add/Steal CG 5 on J | Create Cam 1 on J (Plus) |
| i (index) | P, ;, -, [, ', =, ] | Command 2, 3, 4, 5, 7, 10, 11 | same Command | Create Cam 1, Top Bar Power 1-4 | Jump to Cam 2 and 5, Auto-Cast | Create Cam 2, 5 |
| m (middle) | O, L, 9, 0, . | CG 1, 3, 4, 5, 10 | Create CG n | Add/Steal CG n | Jump to Cam 3, 6, 8 (Plus: Create/Steal CG n) | Jump to Cam n / Create Cam n |
| r (ring) | I, K, 8, U, `,`, 7 | CG 2, 6, 7, 8, 9, Idle Worker | Create CG n | Add/Steal CG n | Jump to Cam 4, 7 (Plus: Create/Steal CG n) | Jump to Cam n / Create Cam n |
| t (thumb) | / | Special Command 1 (Plus: Thumb Command) | | | | |

The Finger Chart image (`thecore/finger-chart-5.0.png`) colours the keys in four groups but carries no legend. The spreadsheet's finger letters name them: `J`, `H`, `M` and the rest of the red group are the pinky, `I` and `K` the ring, `O` and `L` the middle, and `P`, `;` and the green group the index. That is what a left hand gets on the right side of a keyboard with its thumb on the right-hand Shift, Alt and Ctrl: the pinky sits nearest the middle of the board. `tools/thecore_keys.py` uses the same letters. The one disagreement is `U` and `7`, which the sheet gives to the ring finger and the chart colours with the pinky group.

What changed in the shipped 6.0 file: `K` goes from 10 bindings (4 plain) to 82 plain bindings and `Period` from 5 to 15 plain, so two keys that were pure control-group slots in 5.0 became command-card keys; `BackSlash` appears as a new index key with 5 bindings, so the index group grows from 10 keys to 11; and the pinky keys gain full modifier sets, with `J` carrying all seven combinations rather than four.

## 3. What the Svalboard wiki says about key ease

The one global ordering, [Ergonomics and fit](/ergonomics-and-fit.md): key difficulty runs "down > south > inward = north > outward" (S:660969), read easiest first, so centre, then south, then inward and north tied, then outward. That is claussen's order. The two other orderings the wiki cites beside it disagree about north: "down, south, inward, outward, north" (S:456597) puts it last, and "Middle > South > North > Inwards > Outwards" (S:159072) puts it above inward. All three agree that centre is first, south second and outward in the bottom two; the inward = north tie that section 4a uses is claussen's alone. When porting a flat layout, put the inner diagonal reaches on inward middle and ring (S:177041). Laterals split: inward keys are light and quick to learn, outward awkward and worst on the ring (S:224460). River's decomposition narrows the novelty: inward is about as easy as down, so only outward is a genuinely new movement (S:183424), and outward ring is the one that "probably needs the most practice" (S:310331).

Two named worst positions. Pinky north is the worst key on the board and the advice is to fix it in the layout rather than train it, with a Repeat key or a letter swap (S:283944, S:041266); pinkies that feel useless on north usually need cluster rotation to match finger splay (S:447489). Ring outward is the exception everyone hates, fixed with outward roll, a stiffer or more spacious key, or by not mapping it at all (S:619275, S:013317). North in general is the universal complaint, and the shipped fix is a thicker and lighter north key, mainline 2024-05-21, which stopped fingers flying out of the socket on north combos (S:301843, S:004830, S:368122, S:638662). Mechanically north is extension and a flick upward, not an outward reach (S:372621).

Centre and south are the resting positions, [Ergonomics and fit](/ergonomics-and-fit.md) and [FAQ](/faq.md): you are meant to rest on the keys, "S can take a huge amount of force… that's the purpose of the fitment mechanism", and the home row here is a centre or south key, not a row (S:475099, S:032203); resting on south "a *bit* is fine, touching N tends to be more error-prone as extension is less controlled" (S:010497); cramping means you are hovering instead of resting on centre or south (S:815232, S:076309, S:361595). That is also why [Firmware and config](/firmware-and-config.md) puts modifiers on the bottom row rather than the home row, "because south is so good on sval" (S:349754, S:645618). Stock force follows the same story: side keys ship at a 0.7 mm magnet offset, roughly 20 g (S:465775), and tipping centres at 0.9 mm, which is lighter (S:581929, S:393361); the thumb knuckle ships heavier at 0.4 mm because it "is stronger than it realizes and tends to get false actuations if it's too light" (S:029736, S:744094).

The thumb cluster has five keys, Pad, Nail, Knuckle, Down and Up (also called Mode), plus a second stage under Down that cannot be bound separately. The ranking: nail over knuckle unanimously, with Pad the favourite (S:083694, S:395392, S:155753); knuckle is the worst thumb key and "belongs to a modifier", not a letter (S:564050). Down is treated separately and has the sharpest learning curve on the board: its half-press is "the single hardest adjustment", the key can travel about 75% without actuating, and the fix is moving the cluster south with the thumb as deep in as is comfortable (S:729728, S:761184); [Open questions](/open-questions.md) records it as the loudest complaint of 2024-05 (S:890763), at what claussen called "a 1-2% report rate" (S:945814), and "long boi" thumb keys with the magnets offset 0.8 mm are one user's workaround (S:675539). Chords: the only rated ones are Down + Pad as easiest, then Down + Pad + Knuckle, "but it's a bit of a contortion" (S:496731, S:225903). Modifiers on thumbs with no home-row mods is called "a viable 20-year answer" (S:928060), and claussen holds control+shift+tab with one thumb (S:683620). Thumb Up is the layer key by default and the escape hatch, left thumb up bound to layer 0 only (S:015400, S:801298, S:111792). Mouse clicks go on whichever cluster the modifiers are not on; the default click keys were the souths (S:057237) and are now the centres, "so you can click with the opposite hand" (S:056916), with claussen's reason for not clicking with the same-hand thumb being that it encourages finger and wrist movement (S:638009).

Same-finger sequence evidence is thin, and what exists is a warning, not data. [Gaming](/gaming.md): collapsing WASD onto one finger's cluster "just becomes cursor diamond and is a recipe for RSI" (S:369527, S:797555). Adjacent and indirect: north combos are iffy and south combos are great across one cluster (S:930405, S:652019), cross-petal diagonals are physically hard because once a key breaks away the force drops steeply (S:740670), and repeats of the same key rather than rolls are what people complain about, with the switches deliberately not optimised for rapid repeats (S:958616). The one throughput number is whole-board: 6.7 clicks per second on a Svalboard against 6.9 on a Wooting (S:609447, S:244127).

Gaming-layer conventions, [Gaming](/gaming.md): make the layer locking rather than held, `TG` being the mechanism (S:437698); strip home-row mods (S:316392) and one-shot mods (S:018053) because games assume WASD and hold-or-tap behaviours misfire (S:283391); switch to the mouse layer, press the automouse toggle, turn off autoshift (S:612489, S:139654). Held movement keys go on centres and souths, never north: "putting that on the north is really bad" (S:130017, S:754446). One firmware gotcha: you cannot toggle into a layer you are already momentarily in, so a lock needs a duplicated destination layer (S:136074).

What the wiki does not measure: there is no timing or words-per-minute figure per position, no per-finger ranking of the five directions (only the one global order and the two named outliers), no per-position force table beyond the stock offsets above, and no chord data beyond the two thumb chords. The only ease note on thumb Up is in the raw export rather than on any wiki page, claussen: "Forming the thumb up is a bit harder than N keys, since it's not as coherent in layer structure" (S:126898).

## 4. The recipe, applied

Derived below, not said by either community. Nobody in either Discord has run TheCore's method on a DataHand-style board, and the wiki has no per-position numbers to score against. What follows is TheCore's procedure with the Svalboard's evidence substituted for TheCore's keyscore.

### 4a. Key speed zones for a Svalboard hand

Zone membership below is the only part the wiki supports. Ordering inside a zone is judgment, exactly as it is in TheCore, where the Handbook makes intuition the tie-break within a zone.

| Finger | Direction | Zone | Evidence |
|---|---|---|---|
| index, middle, ring, pinky | centre (down) | 1 | easiest in the global order (S:660969); the resting key (S:475099) |
| index, middle, ring, pinky | south | 1 | second in the order, rests fine, takes force (S:660969, S:032203) |
| index, middle, ring | inward | 2 | light and quick to learn, tied with north on claussen's order only, see section 3 (S:660969, S:224460, S:183424) |
| index, middle, ring | north | 2 | tied with inward in the order, universal complaint (S:660969, S:301843) |
| pinky | inward | 2 | no pinky-specific exception is recorded for inward (S:224460) |
| index, middle | outward | 3 | outward is last and the one genuinely new motion (S:660969, S:183424) |
| pinky | outward | 3 | outward last (S:660969) |
| ring | outward | 3 | "the exception everyone hates", stiffen or leave unmapped (S:619275) |
| pinky | north | 3 | "the worst key", demoted from the north tier (S:283944) |

That is 8 zone-1 keys, 7 zone-2 keys and 5 zone-3 keys per hand, against TheCore's 2 zone-1 columns on a full keyboard. Derived thumb ranking, from the same evidence: Pad (S:155753), then Nail (S:083694), then Down with the half-press caveat (S:729728), then Up (no wiki rank, one raw note that it is harder than north, S:126898), then Knuckle last (S:564050).

### 4b. Modifiers on the thumb

TheCore needs the thumb to hold one modifier combination through a whole sequence (`F.A.Q_.docx`, modifier synergy), and it needs Ctrl in most of the combinations, since Ctrl is the add-or-steal modifier that the camera jump is aligned to. Derived proposal, one modifier per thumb key:

- **Ctrl on Pad.** Pad is the favourite thumb key (S:155753) and Ctrl appears in more combinations than any other modifier in the 5.0 Plus sheet.
- **Shift on thumb Down.** Down + Pad is the only chord the wiki rates as easiest (S:496731), so the two modifiers that get pressed together, Ctrl and Shift for the camera jump, go on that pair. Cost: the half-press is the hardest adjustment on the board (S:729728), so this assignment depends on a good fit, the cluster moved south, or a long-boi key with the magnet offset 0.8 mm (S:675539).
- **Alt on Knuckle.** The wiki says knuckle "belongs to a modifier, not a letter" (S:564050), and Alt is the least frequently held of the three in the sheet. A useful side effect: Ctrl+Shift+Alt then becomes Pad + Down + Knuckle, which the wiki calls "a bit of a contortion" (S:225903), and that is exactly TheCore's banished combination, which is meant to be hard.
- **Nail as the overflow layer key.** Nail ranks above knuckle (S:083694), and TheCore's own answer to a small board is an Fn layer ([Svalboard and TheCore](/svalboard-and-thecore.md), C:917360).
- **Up as the gaming-layer lock.** Thumb Up is the default layer key and escape hatch (S:015400, S:801298), and gaming layers should lock rather than be held (S:437698), remembering the duplicated-layer gotcha (S:136074).

### 4c. Command classes onto finger zones, and the budget

TheCore's roles carry over unchanged: index and pinky take the plain `Command n` slots, because those keys carry hundreds of command-card bindings; middle and ring take the control-group and camera slots, one binding per modifier; and no two steps of a common sequence sit on the same finger (Handbook, Select All Army and Larva Injects passages).

The budget does not fit. TheCore 5.0 Right uses 10 index + 4 middle + 4 ring + 9 pinky = 27 finger keys. A Svalboard hand has 20 finger keys, of which 8 are zone 1. The middle and ring load fits easily, 8 slots into 10 keys. The index and pinky load does not: 19 slots into 10 keys, an overflow of 9.

Three ways out:

- **The other hand.** On a Svalboard the pointing device sits under a thumb, so no hand is holding a mouse. That is a real break from TheCore's premise, which assumes one hand on the keyboard and one on the mouse, and it doubles the key budget to 40 finger keys and 16 zone-1 keys. The cost is that mouse clicks then need keys of their own, and the wiki puts them on the cluster the modifiers are not on, on the centres by current default (S:056916).
- **A layer.** TheCore's own answer on small boards, `F` and `Fn+F` in place of `Alt+F` ([Svalboard and TheCore](/svalboard-and-thecore.md), C:917360).
- **Dropping the tail.** Commands 10 to 13 and CG 9 to 10 are the lowest-priority slots by TheCore's own numbering.

Recommended: **the layer**, held under the thumb Nail, on one hand. This is the user's decision about their own setup, not a finding from either Discord: they play with the left hand on the Svalboard and the right hand on an ordinary mouse, not on the board's trackball. That settles the choice before the ergonomics do. The other hand is simply not available, so the board offers 20 finger keys plus the thumb cluster, and the only extra room is a held layer, which is TheCore's own answer on small boards ([Svalboard and TheCore](/svalboard-and-thecore.md), C:917360). Two consequences worth stating: mouse clicks cost no keys at all, which is what breaks in the two-hand version (S:056916); and a held layer is not the locking gaming layer of 4b, so it costs no mode change under time pressure, only a thumb that is already down. Dropping the tail is not needed: 40 slots hold everything the two shipped files bind except the modifier keys themselves, the mouse buttons, the banished commands, and two or three camera and idle-worker keys that overflow the middle and ring fingers (see 4d).

### 4d. The computed assignment

The table below is generated, not hand-written: `tools/thecore_svalboard.py` prints it with `--markdown`, so it and
[`thecore/svalboard-keymap.html`](../thecore/svalboard-keymap.html) can never drift apart. Re-run the tool after any
change to a hotkey file or to the rules above.

Three inputs, all cited elsewhere on this page or in the repo:

1. The shipped files, parsed as in section 2. The unit of assignment is one TheCore physical key with every modifier
   variant it carries, because TheCore keeps them together: `E` is Command 2 plain, Command 2 queued on Shift, and its
   Ctrl and Alt bindings, all on one key well.
2. Replay evidence for the ordering: events per minute per TheCore key, summed over Terran, Zerg and Protoss across
   187 IEM Katowice 2024 games, from [`../thecore/sequences-summary.json`](../thecore/sequences-summary.json) as
   described in [SC2 command sequences](/sc2-command-sequences.md). The summary ships a key map for 5.0 only, so both
   files are scored the same way instead: each summary ability row is matched to the key that file binds it to, and
   each control-group set, add, steal, delete and recall is counted on that file's own recall key. Right clicks are
   dropped, because they are on the mouse. **The co-op blend was adopted in issue #27**: the tool is run with
   `--coop-blend 0.5 --coop-normalize`, so each key's load is 0.5 x its 1v1 rate + 0.5 x its co-op rate, the
   equal-commander mean over the 18 commanders of [`../thecore/coop-summary.json`](../thecore/coop-summary.json)
   (per-minute rates averaged, raw counts never pooled), with the co-op side first scaled so its total load and
   total bigram rate equal the 1v1 totals; without that scaling co-op per-key rates total ~5x below 1v1 (bigram
   totals ~10x below) and co-op gets well under half the influence. Bigram rates blend the same way. What equal influence costs 1v1 play is measured in
   [`../thecore/coop-blend-report.md`](../thecore/coop-blend-report.md): about 1.7%.
3. The zones of 4a and the finger roles of 4c.

Slots: 20 base keys and 20 with the Nail layer held. A slot's difficulty is `(zone - 1) + 1 if the layer is held` plus
a per-finger weight of index 0.0, middle 0.0, ring 0.2, pinky 0.5, which treats a held layer as costing about one zone
step and a pinky key as costing half of one. That *derives* the ordering base zone 1, base zone 2, layer zone 1, base
zone 3, layer zone 2, layer zone 3, with index and middle ahead of ring and pinky inside each band. Inside a zone the
order is 4a's: centre, south, inward, north, outward, with pinky north forced last as "the worst key" (S:283944).

Two rules were added after the first pass, and one of them is not evidence. **The per-finger weights are an
assumption**: the Svalboard wiki of section 3 ranks positions within one finger and never ranks the fingers against
each other, so the four numbers above are a judgement call, picked so that the highest-load keys prefer index and
middle over ring and pinky. Without them every finger cost the same and Attack landed on the pinky. **The
control-group floor** is the second rule: the ten keys carrying `ControlGroupRecall0` to `9` each get a base-plane
middle or ring slot. Middle and ring have exactly ten base slots, so the ten groups own them outright, no group sits
anywhere else and nothing else sits there. Where 6.0 stacks a group onto a command-card key (`J`, `M`, `N`, `H`, `G`)
this beats the index/pinky rule for `Command n`. Everything else, camera keys included, competes for the other 30
slots under the rules already stated.

Assignment, deterministic and printed by the tool:

1. Order TheCore's keys by how tight their role is first, then by replay load, most first; ties broken by binding
   count, then by name. Tightness runs control-group recall (ten fixed slots), then the camera and idle-worker group
   (middle and ring only), then command-card keys (index and pinky only), then unconstrained keys. Ordering on load
   alone lets an unconstrained key take the last slot a constrained key is allowed to use, which is what pushed Idle
   Worker and Town Camera off the hand before issue #33. TheCore's own slot numbers are not in the hotkey files, so
   binding count stands in for them.
2. Greedy: each key takes the easiest free slot its role allows.
3. Then a hill climb: repeatedly make the one swap of two placed keys that lowers the cost most, as long as each key's
   role still allows its new finger and the control-group floor still holds. Cost, in events per minute, is the rate of same-finger different-key transitions
   over the summary's bigrams (a transition that crosses into the layer counts half, since the layer hand is already
   loaded differently) plus each key's load times its slot difficulty. Same-key repeats such as `CG3 > CG3` are not a
   cost; the summary counts them separately.

For 5.0 Right Plus that is 98.73 after the greedy pass and 83.67 after 5 swaps; for 6.0 Right, 98.22 and then 82.60
after 6 swaps. These are blended-unit costs (the normalized 50/50 mix above), so they are not comparable with the 1v1-only
106.46/99.11 and 106.11/98.20, nor with the 69.29 and 41.13 of the pass before the finger weights and the
control-group floor.

Some same-finger work is forced rather than a failure of the search. The control-group floor puts all ten groups on
middle and ring, and five of them carry most of the replay load, so heavy pairs such as `CG1 > CG3` share a finger
whichever way they are arranged; the tool spends the half-price cross-plane transition on the heaviest of them. Camera
and idle-worker keys score zero, because a replay records where the camera went and never which key moved it, so they
sort to the tail of the load ordering. That is a limit of the evidence, not a judgement that they are unused, and it
is why the ordering puts role tightness ahead of load: Town Camera and Idle Worker may only take a middle or ring
slot, and on load alone the zero-scoring unconstrained keys took those slots first and pushed both off the hand.
Seating them costs almost nothing, because the keys they displace also score zero. 5.0 finishes at the same 83.67 and
drops `X` (Merc Hellion on the Factory, Set Bunker Rally Point) and `B` (Stop Planetary Fortress); 6.0 finishes at
82.60 against 82.58 and drops `R` (Vespene Drone on the Command Center and the Planetary Fortress) and `Space`
(Stalker Hallucination on the Sentry).

Banished commands stay banished: this board can only make Ctrl+Shift+Alt as Pad + Down + Knuckle, and the keys whose
every binding is that chord get no slot of their own. There is a way out that this pass does not take: SC2 accepts
`F13`, `F14` and up as hotkeys and no ordinary board can send them, which is why TheCore's own community used them as
a dumping ground and macroed Fn+key to an unused F-key for a one-press inject
([hotkey file editing](/thecore/hotkey-file-editing.md), 191702, 384532; [keyboards and
hardware](/thecore/keyboards-and-hardware.md), H:256033, H:157574, H:130369). Firmware could emit F13-F24 from layer
slots and free a banished command from the contortion.

TheCore 5.0 Right Plus, generated; the 6.0 Right table is on
[`thecore/svalboard-keymap.html`](../thecore/svalboard-keymap.html), which draws both files with every binding on the
key that would press it. "Load /min" is the replay evidence of input 2, and "Vial keycode" is what the firmware must
emit for that well (section 4e).

| Svalboard key | Zone | TheCore key | Vial keycode | Carries | Load /min |
| --- | --- | --- | --- | --- | --- |
| **Base** | | | | | |
| index centre | 1 | P | `KC_P` | Cam 0/3, Attack, Larva | 32.9 |
| index south | 1 | - | `KC_MINS` | Larva, command card (187) | 5.9 |
| index inward | 2 | [ | `KC_LBRC` | Burrow Down, command card (106) | 1.5 |
| index north | 2 | ] | `KC_RBRC` | Move Hold Position, command card (11) | 1.0 |
| index outward | 3 | N | `KC_N` | Land, Lift, Larva | 0.4 |
| middle centre | 1 | O | `KC_O` | CG 1, Cam 1 | 36.1 |
| middle south | 1 | L | `KC_L` | CG 3, Cam 5 | 21.1 |
| middle inward | 2 | I | `KC_I` | CG 2, Cam 2 | 20.6 |
| middle north | 2 | 0 | `KC_0` | CG 6 | 5.5 |
| middle outward | 3 | U | `KC_U` | CG 8 | 1.3 |
| ring centre | 1 | K | `KC_K` | CG 4, Cam 6 | 24.8 |
| ring south | 1 | 9 | `KC_9` | CG 5, Cam 7 | 20.6 |
| ring inward | 2 | . | `KC_DOT` | CG 0 | 4.6 |
| ring north | 2 | , | `KC_COMM` | CG 9 | 1.6 |
| ring outward | 3 | 8 | `KC_8` | CG 7 | 1.1 |
| pinky centre | 1 | ; | `KC_SCLN` | Cam 4, command card (254) | 3.3 |
| pinky south | 1 | J | `KC_J` | Cam 3, Larva, command card (297) | 3.1 |
| pinky inward | 2 | G | `KC_G` | Stop, command card (13) | 0.7 |
| pinky north | 3 | W | `KC_W` | command card (5) | 0.0 |
| pinky outward | 3 | D | `KC_D` | Rally Egg, command card (6) | 0.0 |
| **Nail layer held** | | | | | |
| index centre | 1 | ' | `KC_QUOT` | Larva, command card (52) | 1.0 |
| index south | 1 | H | `KC_H` | Larva, Burrow Up, command card (74) | 0.9 |
| index inward | 2 | Y | `KC_Y` | Move Patrol, Larva, Army Select | 0.2 |
| index north | 2 | = | `KC_EQL` | Larva, command card (30) | 0.0 |
| index outward | 3 | Backspace | `KC_BSPC` | Camera Turn Left, Camera Turn Right | 0.0 |
| middle centre | 1 | F | `KC_F` | Rally SCV | 0.1 |
| middle south | 1 | Z | `KC_Z` | Rally | 0.0 |
| middle inward | 2 | 7 | `KC_7` | Idle Worker | 0.0 |
| middle north | 2 | Enter | `KC_ENT` | Chat Default, Chat Allies | 0.0 |
| middle outward | 3 | Escape | `KC_ESC` | Menu Game | 0.0 |
| ring centre | 1 | 6 | `KC_6` | Town Camera | 0.0 |
| ring south | 1 | A | `KC_A` | Move | 0.0 |
| ring inward | 2 | E | `KC_E` | misc | 0.0 |
| ring north | 2 | Q | `KC_Q` | misc | 0.0 |
| ring outward | 3 | F10 | `KC_F10` | Menu Game | 0.0 |
| pinky centre | 1 | / | `KC_SLSH` | Cancel, command card (12) | 0.5 |
| pinky south | 1 | M | `KC_M` | Stop Generate Creep, Larva, command card (84) | 0.5 |
| pinky inward | 2 | C | `KC_C` | Select Builder, command card (5) | 0.0 |
| pinky north | 3 | Tab | `KC_TAB` | misc | 0.0 |
| pinky outward | 3 | R | `KC_R` | misc | 0.0 |

### 4e. Vial versus the hotkey file

Do all modifier work in the firmware and all per-command work in the text file. The reasons, the mouse-button tokens, the alternate tricks and the one case that must be firmware rather than file are set out in [Svalboard and TheCore](/svalboard-and-thecore.md); the thumb assignment in 4b and the layer key in 4c are Vial changes, and so is the table in 4d: every slot in it emits an ordinary TheCore keycode, so the `.SC2Hotkeys` file ships unedited once the thumb emits real Ctrl, Shift and Alt.

## 5. Open questions

- **The per-position timing gap.** TheCore's only speed number is a borrowed "2-5 times faster" for home keys (Handbook), and the Svalboard wiki has no timing per direction at all. So zone 1 versus zone 2 on this board is an ordering with no magnitude, and nothing says whether a Svalboard centre key beats a south key by 5% or by 100%.
- **Can one cluster take TheCore's press rate?** `J` carries 297 plain bindings in 5.0 Right Plus and is the busiest key in the file, and the wiki both warns against collapsing a movement cluster onto one finger (S:369527) and says the switches are not optimised for rapid repeats (S:958616). Nobody has measured a cluster under RTS load.
- **Where do next and previous subgroup go?** They are not in the 5.0 important-keys table at all. With the right hand on a mouse they are natural mouse-button binds, which is what 4d assumes by leaving the mouse tokens off the board.
- **What does a held layer really cost?** 4d prices it at one zone step, which is a guess with nothing behind it: the wiki has no timing for holding the Nail while a finger moves, and TheCore's community never measured its own Fn layer either. Change that number and the layer half of the table reshuffles.
- **Should the camera keys be scored some other way?** Replays never say which key moved the camera, so every camera and idle-worker key scores zero in 4d and sorts to the tail behind keys that are genuinely idle. Camera jumps per minute are in the summary as a total; splitting them across camera slots would need something replays do not record.
- **Is thumb Up spare?** It carries the gaming-layer lock in 4b, but it has no ease rank anywhere on the wiki, and the only note on it, that forming it is harder than a north key, is in the raw export rather than in the distilled pages (S:126898).
