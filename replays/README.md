# Replays

Replay files are not committed (`.gitignore` keeps `replays/` out except this file).
This is the set `wiki/sc2-command-sequences.md` and `thecore/sequences-summary.json`
were measured from, and how to fetch it again.

## The set

- **Pack**: IEM Katowice 2024, main event only (`3 - Main Event/` inside the zip).
- **Source**: [spawningtool's replay packs page](https://lotv.spawningtool.com/replaypacks/),
  entry "2024_01-IEM_Katowice_2024", which links a Google Drive zip
  (file id `1_Mopn1sGftCJpGf8GM6Uaab-BWuIX6-I`).
- **Downloaded**: 2026-08-29.
- **Games**: 187 `.SC2Replay` files, all 1v1, 374 player-games:
  Terran 167, Protoss 106, Zerg 101.
- **Patch**: 5.0.12.91115 (all 187).
- **Parsing**: all 187 parsed with sc2reader 1.9.0 at `load_level=4`; none failed.
- **Clock**: all 187 are LotV on "Faster", i.e. 22.4 game loops per real
  second, which is how event times become seconds. `extract` refuses a replay
  that is not LotV/Faster rather than mis-time it.

## Fetch again

```sh
curl -sSL -o /tmp/kato2024.bin \
  "https://drive.usercontent.google.com/download?id=1_Mopn1sGftCJpGf8GM6Uaab-BWuIX6-I&export=download&confirm=t"
unzip -q -o -j /tmp/kato2024.bin '2024_01-IEM_Katowice_2024/3 - Main Event/*.SC2Replay' \
  -d replays/iem-katowice-2024
ls replays/iem-katowice-2024 | wc -l   # 187
```

`-j` flattens the round subdirectories; the filenames already carry round, players and map.

## Measure again

sc2reader needs Python 3.12 (3.14 is not supported). Either:

```sh
uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
    extract replays/ -o ~/scratch/thecore/events.jsonl.gz
uv run --python 3.12 --with sc2reader python tools/sc2_sequences.py \
    report ~/scratch/thecore/events.jsonl.gz \
    -o wiki/sc2-command-sequences.md --summary thecore/sequences-summary.json \
    --replay-set "IEM Katowice 2024 main event" \
    --parse-note "All 187 replays in the pack parsed; none failed, so no s2protocol fallback was needed."
```

or with a venv outside the repo:

```sh
python3.12 -m venv ~/scratch/thecore/venv-replays
~/scratch/thecore/venv-replays/bin/pip install sc2reader
~/scratch/thecore/venv-replays/bin/python tools/sc2_sequences.py extract ...
```

The event stream is 2,156,868 events (13 MB gzipped) and takes ~40 s to extract; keep it
outside the repo. `report` needs no replays and no sc2reader: it also accepts the
committed `thecore/sequences-summary.json` in place of the event file, which is how the
wiki page is rebuilt.
