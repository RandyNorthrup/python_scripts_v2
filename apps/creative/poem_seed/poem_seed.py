#!/usr/bin/env python3
"""Offer a title, image, sound, and final-word constraint for a poem."""

from __future__ import annotations

import argparse
import random

PATTERN = "Title “{title}”; image: {image}; sound: {sound}; end on “{ending}”."
TITLE: tuple[str, ...] = (
    "Instructions for Fog",
    "Small Astronomy",
    "After the Market",
    "Borrowed Weather",
)
IMAGE: tuple[str, ...] = (
    "keys cooling on a windowsill",
    "chalk stars on wet pavement",
    "oranges rolling from a bag",
    "a coat holding rain",
)
SOUND: tuple[str, ...] = (
    "distant train brakes",
    "spoons in a drawer",
    "bees behind a wall",
    "one bicycle bell",
)
ENDING: tuple[str, ...] = ("home", "blue", "again", "open")


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            title=rng.choice(TITLE),
            image=rng.choice(IMAGE),
            sound=rng.choice(SOUND),
            ending=rng.choice(ENDING),
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
