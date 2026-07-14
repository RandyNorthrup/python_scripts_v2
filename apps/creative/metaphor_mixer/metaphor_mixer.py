#!/usr/bin/env python3
"""Mix sensory images into surprising metaphor starters."""

from __future__ import annotations

import argparse
import random

PATTERN = "{concept} is {image} {action}."
CONCEPT: tuple[str, ...] = ("Patience", "Jealousy", "Memory", "Hope")
IMAGE: tuple[str, ...] = (
    "a paper lantern",
    "an untuned radio",
    "a winter orchard",
    "a pocket compass",
)
ACTION: tuple[str, ...] = (
    "waiting beneath the floorboards",
    "searching for one clear station",
    "holding fruit no one can see",
    "pointing through a storm",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            concept=rng.choice(CONCEPT),
            image=rng.choice(IMAGE),
            action=rng.choice(ACTION),
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
