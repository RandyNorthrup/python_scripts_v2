#!/usr/bin/env python3
"""Create unusual heroes with powers, limits, and civic problems."""

from __future__ import annotations

import argparse
import random

PATTERN = "{alias} can {power}, but {limit}; today they must {problem}."
ALIAS: tuple[str, ...] = ("The Margin", "Static Bloom", "Second Hand", "Mothlight")
POWER: tuple[str, ...] = (
    "step into written footnotes",
    "grow tools from seeds",
    "borrow ten seconds from tomorrow",
    "speak with streetlights",
)
LIMIT: tuple[str, ...] = (
    "only near a library",
    "every tool wilts by sunset",
    "tomorrow becomes shorter",
    "the lights exaggerate",
)
PROBLEM: tuple[str, ...] = (
    "mediate a parade route",
    "find a missing bus",
    "repair a community garden",
    "stop a rumor becoming real",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            alias=rng.choice(ALIAS),
            power=rng.choice(POWER),
            limit=rng.choice(LIMIT),
            problem=rng.choice(PROBLEM),
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
