#!/usr/bin/env python3
"""Suggest song sections using Roman-numeral chord progressions."""

from __future__ import annotations

import argparse
import random

PATTERN = "{section}: {progression} in a {feel} feel at {tempo} tempo."
SECTION: tuple[str, ...] = ("Verse", "Chorus", "Bridge", "Outro")
PROGRESSION: tuple[str, ...] = ("I–V–vi–IV", "ii–V–I–vi", "i–VII–VI–VII", "I–iii–IV–iv")
FEEL: tuple[str, ...] = (
    "bright acoustic",
    "restless synth",
    "slow cinematic",
    "playful funk",
)
TEMPO: tuple[str, ...] = ("72 BPM", "96 BPM", "118 BPM", "140 BPM")


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            section=rng.choice(SECTION),
            progression=rng.choice(PROGRESSION),
            feel=rng.choice(FEEL),
            tempo=rng.choice(TEMPO),
        )
        for _ in range(count)
    ]


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=42, help="Reproducible seed.")
    parser.add_argument("--count", type=int, default=3, help="Number of ideas.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        ideas = generate(int(args.seed), int(args.count))
    except ValueError as error:
        raise SystemExit(str(error)) from error
    print("\n".join(f"{index}. {idea}" for index, idea in enumerate(ideas, 1)))


if __name__ == "__main__":
    main()
