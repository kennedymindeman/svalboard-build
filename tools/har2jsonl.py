#!/usr/bin/env python3
"""Extract Discord messages from a DevTools HAR export into JSONL.

Usage: tools/har2jsonl.py export.har [more.har ...] > discord/raw/<channel>.jsonl

Capture: open the channel in Discord (desktop app or web), DevTools > Network,
filter "messages", tick Preserve log, scroll up as far as you want, then use the
Network toolbar's download icon: "Export HAR (sanitized)". Sanitized keeps the
response bodies and strips cookies/Authorization. "Copy all as HAR" from the
right-click menu drops the bodies and is useless here.
"""
import json, re, sys

msgs = {}
for path in sys.argv[1:]:
    har = json.load(open(path))
    for e in har["log"]["entries"]:
        if not re.search(r"/channels/\d+/messages(\?|$)", e["request"]["url"]):
            continue
        text = e["response"]["content"].get("text")
        if not text:
            continue
        for m in json.loads(text):
            msgs[m["id"]] = {
                "id": m["id"], "channel_id": m["channel_id"], "ts": m["timestamp"],
                "author": m["author"].get("global_name") or m["author"]["username"],
                "author_id": m["author"]["id"], "content": m["content"],
                "attachments": [a["url"] for a in m.get("attachments", [])],
                "embeds": [{"title": x.get("title"), "url": x.get("url"),
                            "desc": x.get("description")} for x in m.get("embeds", [])],
                "reply_to": (m.get("referenced_message") or {}).get("id"),
                "reactions": [(r["emoji"].get("name"), r["count"]) for r in m.get("reactions", [])],
            }
for r in sorted(msgs.values(), key=lambda r: r["ts"]):
    print(json.dumps(r, ensure_ascii=False))
print(f"{len(msgs)} unique messages", file=sys.stderr)
