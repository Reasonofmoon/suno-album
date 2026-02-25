#!/usr/bin/env python3
"""
Build ffmetadata chapter file and optional YouTube timestamp text from a track manifest CSV.

Required CSV columns:
  - title
  - duration_sec

Optional:
  - order
  - file
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Track:
    index: int
    title: str
    duration_sec: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build FFmpeg chapter metadata from manifest.csv")
    parser.add_argument("--input", required=True, help="Input manifest CSV path")
    parser.add_argument("--output", required=True, help="Output ffmetadata file path")
    parser.add_argument(
        "--youtube-output",
        default=None,
        help="Optional output text file with YouTube timestamps",
    )
    return parser.parse_args()


def read_manifest(path: Path) -> List[Track]:
    tracks: List[Track] = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        required = {"title", "duration_sec"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required CSV columns: {', '.join(sorted(missing))}")

        for idx, row in enumerate(reader, start=1):
            title = (row.get("title") or "").strip()
            if not title:
                raise ValueError(f"Row {idx}: empty title")

            duration_raw = (row.get("duration_sec") or "").strip()
            if not duration_raw:
                raise ValueError(f"Row {idx}: empty duration_sec")

            try:
                duration_sec = float(duration_raw)
            except ValueError as exc:
                raise ValueError(f"Row {idx}: invalid duration_sec '{duration_raw}'") from exc

            if duration_sec <= 0:
                raise ValueError(f"Row {idx}: duration_sec must be > 0")

            tracks.append(Track(index=idx, title=title, duration_sec=duration_sec))

    if not tracks:
        raise ValueError("Manifest is empty")
    return tracks


def hhmmss(total_seconds: int) -> str:
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def write_ffmetadata(tracks: List[Track], output: Path) -> None:
    cursor_ms = 0
    lines = [";FFMETADATA1", ""]
    for track in tracks:
        start_ms = cursor_ms
        end_ms = start_ms + int(round(track.duration_sec * 1000))
        cursor_ms = end_ms
        lines.extend(
            [
                "[CHAPTER]",
                "TIMEBASE=1/1000",
                f"START={start_ms}",
                f"END={end_ms}",
                f"title={track.index:02d}. {track.title}",
                "",
            ]
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_youtube_timestamps(tracks: List[Track], output: Path) -> None:
    cursor = 0
    lines = []
    for track in tracks:
        lines.append(f"{hhmmss(cursor)} - {track.index:02d}. {track.title}")
        cursor += int(round(track.duration_sec))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()
    yt_output_path = Path(args.youtube_output).resolve() if args.youtube_output else None

    tracks = read_manifest(input_path)
    write_ffmetadata(tracks, output_path)
    if yt_output_path:
        write_youtube_timestamps(tracks, yt_output_path)

    print(f"Built chapter metadata: {output_path}")
    if yt_output_path:
        print(f"Built YouTube timestamps: {yt_output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
