# Svalboard Discord — distilled notes

Community knowledge pulled out of the Svalboard Discord (server `1053081626898337902`)
so I don't have to keep up with the channel. Raw exports live in `raw/` (gitignored:
other people's messages don't get committed); the pages here are the distilled result.

How to refresh: scroll the channel in Discord with DevTools open, "Export HAR
(sanitized)", then `tools/har2jsonl.py export.har > discord/raw/<channel>.jsonl`
and re-run the distillation over the new messages. Message ids cited in the wiki pages are
the last 6 digits of the Discord snowflake, unique within the export.

- Channel `1124364902811844739`, 8,921 messages, 2025-10-17 → 2026-08-15 (distilled
  2026-08-15 from six ~1,270-message chunks plus an earlier 1,309-message pass, then
  merged). The result lives in the wiki, one page per topic: [../wiki/index.md](../wiki/index.md).

## Coverage / how to resume scrolling

The channel has ~48,135 messages (Discord's count, 2026-08-15) and was created 2023-06-30.
Captured so far: everything from 2025-10-17 onward (18.5%). Oldest captured message:
id `1428728361026584741` (phreaker, 2025-10-17 12:56 UTC) —
https://discord.com/channels/1053081626898337902/1124364902811844739/1428728361026584741

To extend backwards: open that link, start DevTools (Preserve log, filter "messages"),
scroll up, export HAR. Run `har2jsonl.py` over the new HAR (plus any older HARs still on
disk; it dedupes by message id), then distill only messages older than the previous oldest
`ts`, and update this section.
