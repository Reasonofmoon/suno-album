#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

DEFAULT_BUDGETS = {
    "Intro": 250,
    "Verse 1": 1200,
    "Hook": 600,
    "Verse 2": 1500,
    "Bridge": 600,
    "Final Hook": 600,
    "Outro": 250,
}

TOTAL_MIN = 4000
TOTAL_MAX = 5000
DEFAULT_TOL = 0.10

HEADER_RE = re.compile(r"^\[(.+?)\]\s*$")


def count_chars(text: str, include_newlines: bool) -> int:
    if include_newlines:
        return len(text)
    return len(text.replace("\n", ""))


def parse_sections(text: str, known_names: set[str]) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    sections = {name: [] for name in known_names}
    extras: dict[str, list[str]] = {}
    current: list[str] | None = None

    for line in text.splitlines():
        match = HEADER_RE.match(line)
        if match:
            name = match.group(1).strip()
            if "|" in name:
                if current is None:
                    extras.setdefault("_preamble", []).append(line)
                else:
                    current.append(line)
                continue
            if name in known_names:
                current = sections[name]
                continue
            current = extras.setdefault(name, [])
            continue

        if current is None:
            if line.strip():
                extras.setdefault("_preamble", []).append(line)
            continue
        current.append(line)

    return sections, extras


def status_for(count: int, target: int, tol: float) -> tuple[str, int, int, int]:
    low = int(round(target * (1 - tol)))
    high = int(round(target * (1 + tol)))
    if count < low:
        status = "LOW"
    elif count > high:
        status = "HIGH"
    else:
        status = "OK"
    delta = target - count
    return status, delta, low, high


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count lyric characters by section (spaces included; newlines optional)."
    )
    parser.add_argument("path", help="Path to the lyrics text file.")
    parser.add_argument(
        "--include-newlines",
        action="store_true",
        help="Count newline characters as part of the total.",
    )
    parser.add_argument("--tol", type=float, default=DEFAULT_TOL, help="Tolerance ratio (default: 0.10).")
    parser.add_argument("--total-min", type=int, default=TOTAL_MIN, help="Hard minimum total characters.")
    parser.add_argument("--total-max", type=int, default=TOTAL_MAX, help="Hard maximum total characters.")
    args = parser.parse_args()

    text = Path(args.path).read_text(encoding="utf-8")
    sections, extras = parse_sections(text, set(DEFAULT_BUDGETS.keys()))

    order = list(DEFAULT_BUDGETS.keys())
    extra_names = list(extras.keys())
    width = max([len(name) for name in order + extra_names + ["TOTAL"]] or [5])

    total = 0
    target_total = 0

    print("Section counts (spaces included; newlines excluded by default):")
    for name in order:
        target = DEFAULT_BUDGETS[name]
        target_total += target
        content = "\n".join(sections.get(name, []))
        count = count_chars(content, args.include_newlines)
        total += count
        status, delta, low, high = status_for(count, target, args.tol)
        print(f"{name:<{width}} {count:5d} / {target:5d} {status} ({delta:+d}, {low}-{high})")

    if extras:
        for name in extra_names:
            content = "\n".join(extras[name])
            count = count_chars(content, args.include_newlines)
            total += count
            print(f"{('EXTRA:' + name):<{width}} {count:5d} / {'-':>5}  N/A")

    if total < args.total_min:
        total_status = "LOW"
    elif total > args.total_max:
        total_status = "HIGH"
    else:
        total_status = "OK"

    print(
        f"{'TOTAL':<{width}} {total:5d} / {target_total:5d} {total_status} "
        f"(hard {args.total_min}-{args.total_max})"
    )


if __name__ == "__main__":
    main()
