# Discord — distilled notes

Community knowledge pulled out of the Svalboard Discord (server `1053081626898337902`)
and the TheCore hotkey Discord (server `389438169520799744`) so I don't have to keep up
with the channels. Raw exports live in `raw/` (gitignored:
other people's messages don't get committed); the pages here are the distilled result.

How to refresh: scroll the channel in Discord with DevTools open, "Export HAR
(sanitized)", then `tools/har2jsonl.py export.har > discord/raw/<channel>.jsonl`
and re-run the distillation over the new messages (see "Coverage" below for the chunk step).

- Svalboard #general `1124364902811844739`, 43,129 messages captured, 2023-06-30 → 2025-08-10 and 2025-10-17 → 2026-08-22
  (the last 268, 2026-08-15 → 2026-08-22, are not yet distilled).
  Distilled in three passes: the 2025-10-17 → 2026-08-15 window on 2026-08-15 (six ~1,270-message
  chunks plus an earlier 1,309-message pass), and the 2023-09-07 → 2025-08-10 backfill on 2026-08-16
  (25 ~1,287-message chunks, `tools/chunk.py`, distilled in parallel then merged page by page into
  the wiki), and the 2023-06-30 → 2023-09-06 founding months on 2026-08-22 (1,776 messages in four
  chunks, folded into the existing pages rather than distilled to new ones). The result lives in the
  wiki, one page per topic: [../wiki/index.md](../wiki/index.md).
  Message ids cited in the wiki pages are the last 6 digits of the Discord snowflake; a few collide
  across the 43k-message export, so disambiguate by date if a lookup returns two hits.
- Svalboard channel `1172312033199407114`, 8,943 messages, 2025-07-10 → 2026-08-20: captured in `raw/`, not distilled.
- TheCore #general `389438169520799746`, 23,419 messages, 2019-08-24 → 2026-08-27, distilled on 2026-08-29 in
  18 ~1,300-message chunks (`tools/chunk.py` prefix `cchunk`, per-chunk `cdistill-NN.md`, sliced by topic into
  `csect-*.md`, one merge per page) into its own bundle: [../wiki/thecore/index.md](../wiki/thecore/index.md).
  Cross-community notes: [../wiki/svalboard-and-thecore.md](../wiki/svalboard-and-thecore.md).

## Coverage / how to resume scrolling

Svalboard #general has ~48,135 messages (Discord's count, 2026-08-15) and was created 2023-06-30.
Captured so far: 43,129 (90%). One gap remains:

- **2025-08-10 → 2025-10-17** (~2 months, between the two captures). Newest backfill message:
  id `1404016026848595991` (madnificent, 2025-08-10 08:18 UTC) —
  https://discord.com/channels/1053081626898337902/1124364902811844739/1404016026848595991.
  Oldest of the later capture: id `1428728361026584741` (phreaker, 2025-10-17 12:56 UTC) —
  https://discord.com/channels/1053081626898337902/1124364902811844739/1428728361026584741.
  Open either link, DevTools (Preserve log, filter "messages"), scroll toward the other, export HAR.

To fill a gap: run `har2jsonl.py` over the new HAR plus the older HARs still on disk (it dedupes by
message id and splits mixed captures per channel; the founding-months capture is `raw/discord-founding.har`
and must be included or the 2023-06-30 → 2023-09-06 messages vanish from the rebuilt JSONL), then `tools/chunk.py channel.jsonl discord/raw/<prefix> N --after <ts> --before <ts>` for
just the new range, distill each chunk in the `distill-1.md` format, merge into the wiki pages, and
update this section.
