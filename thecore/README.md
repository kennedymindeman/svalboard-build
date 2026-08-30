# TheCore files

Copies of four files from TheCore's public Google Drive folder ("TheCore", linked from the TheCore Discord; fetched 2026-08-29 as `TheCore-20260829T223140Z-1-001.zip`). They are the community's own distribution, kept here so `tools/thecore_keys.py` and the wiki's key-budget analysis are reproducible.

- `TheCore_5.0_Right_Plus.SC2Hotkeys` — `3. Download TheCore/Hotkey Files - TheCore 5.0 Downloads here!/US Qwerty/`, dated 2019-10-06. "Right" names the mouse hand; "Plus" is the variant that expects the Core+ external modifier remap.
- `TheCore6g_right_US_qwerty.SC2Hotkeys` — `3. Download TheCore/TheCore 6.0 Multiplayer Only/`, dated 2020-04-30.
- `finger-chart-5.0.png` — `2. Information and Data Sheets/Finger Chart.PNG`: which finger presses which key in 5.0 Right.
- `homekeys-and-speedzones-5.0.png` — `2. Information and Data Sheets/HomeKeys and SpeedZones.PNG`: home keys and the three distance zones.

The drive also holds 12 other keyboard layouts for each version, the 1.0–4.0 archives, the 5.0 and 6.0 "important keys" spreadsheets, and the handbook and customization documents; those stay outside the repo. The wiki page [thecore-method-on-a-svalboard](../wiki/thecore-method-on-a-svalboard.md) transcribes what it needs from them.

`tools/thecore_keys.py <file> [--commands]` prints per-key binding counts and modifier combinations grouped by the 5.0 Right finger chart.

`tools/thecore_keymap.py` (no arguments) regenerates [`thecore/keymap.html`](keymap.html), a self-contained page showing every binding on the key that presses it, toggled by melee race and co-op commander.

`tools/thecore_svalboard.py` (no arguments) regenerates [`thecore/svalboard-keymap.html`](svalboard-keymap.html), the same bindings drawn on two Svalboard hands under the key mapping derived in [thecore-method-on-a-svalboard](../wiki/thecore-method-on-a-svalboard.md) section 4d.
