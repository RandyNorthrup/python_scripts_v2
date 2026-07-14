#!/usr/bin/env python3
"""Create scale-degree motifs for melody practice."""

from __future__ import annotations

import argparse
import random

PATTERN = "Degrees {degrees}; rhythm {rhythm}; shape {shape}."
DEGREES: tuple[str, ...] = ("1-3-5-2", "5-4-2-1", "1-2-4-6", "3-2-1-7")
RHYTHM: tuple[str, ...] = (
    "long-short-short-long",
    "four even eighths",
    "syncopated eighths",
    "dotted-quarter and three eighths",
)
SHAPE: tuple[str, ...] = (
    "rise then resolve",
    "fall by steps",
    "leap and echo",
    "circle one anchor note",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            degrees=rng.choice(DEGREES),
            rhythm=rng.choice(RHYTHM),
            shape=rng.choice(SHAPE),
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
