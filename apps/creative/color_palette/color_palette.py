#!/usr/bin/env python3
"""Invent themed color-palette briefs for visual projects."""

from __future__ import annotations

import argparse
import random

PATTERN = "{mood} palette: {color1}, {color2}, {color3}; use for {use}."
MOOD: tuple[str, ...] = (
    "quiet cosmic",
    "sunlit workshop",
    "rainy arcade",
    "desert library",
)
COLOR1: tuple[str, ...] = ("indigo ink", "copper glow", "moss green", "cloud white")
COLOR2: tuple[str, ...] = ("electric coral", "paper cream", "storm blue", "plum shadow")
COLOR3: tuple[str, ...] = ("mint signal", "charcoal", "amber glass", "rose dust")
USE: tuple[str, ...] = (
    "an album cover",
    "a reading app",
    "a board game",
    "a poster series",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            mood=rng.choice(MOOD),
            color1=rng.choice(COLOR1),
            color2=rng.choice(COLOR2),
            color3=rng.choice(COLOR3),
            use=rng.choice(USE),
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
