#!/usr/bin/env python3
"""Render a JSONL message range as N distillation chunks.

Usage: tools/chunk.py channel.jsonl OUTPREFIX NCHUNKS [--before TS] [--after TS]
Writes OUTPREFIX-01.txt .. OUTPREFIX-NN.txt, chronological. Line format:
[last6 id] YYYY-MM-DDTHH:MM author (re last6): content / lines <N attachment(s)> <embed url>
"""
import json, sys

args = sys.argv[1:]
src, prefix, n = args[0], args[1], int(args[2])
before = args[args.index("--before") + 1] if "--before" in args else None
after = args[args.index("--after") + 1] if "--after" in args else None
msgs = [json.loads(l) for l in open(src)]
msgs = [m for m in msgs if (not before or m["ts"] < before) and (not after or m["ts"] > after)]
msgs.sort(key=lambda m: m["ts"])

def line(m):
    s = f"[{m['id'][-6:]}] {m['ts'][:16]} {m['author']}"
    if m["reply_to"]:
        s += f" (re {m['reply_to'][-6:]})"
    s += ": " + m["content"].replace("\n", " / ")
    if m["attachments"]:
        s += f" <{len(m['attachments'])} attachment(s)>"
    for e in m["embeds"]:
        if e.get("url"):
            s += f" <embed {e['url']}>"
    return s

size = -(-len(msgs) // n)
for i in range(n):
    part = msgs[i * size:(i + 1) * size]
    if not part:
        break
    with open(f"{prefix}-{i+1:02d}.txt", "w") as f:
        f.write("\n".join(line(m) for m in part) + "\n")
    print(f"{prefix}-{i+1:02d}.txt {len(part)} {part[0]['ts'][:10]}..{part[-1]['ts'][:10]}", file=sys.stderr)
