# Svalboard Discord — distilled notes

Community knowledge pulled out of the Svalboard Discord (server `1053081626898337902`)
so I don't have to keep up with the channel. Raw exports live in `raw/` (gitignored:
other people's messages don't get committed); the pages here are the distilled result.

How to refresh: scroll the channel in Discord with DevTools open, "Export HAR
(sanitized)", then `tools/har2jsonl.py export.har > discord/raw/<channel>.jsonl`
and re-run the distillation over the new messages. Message ids cited below are the
last 6 digits of the Discord snowflake, unique within the export.

- [general-channel.md](general-channel.md) — channel `1124364902811844739`,
  1,309 messages, 2026-06-21 → 2026-08-15 (distilled 2026-08-15).
