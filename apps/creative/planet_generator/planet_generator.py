#!/usr/bin/env python3
"""Invent science-fiction worlds with environments and mysteries."""

from __future__ import annotations

import argparse
import random

PATTERN = "{name}: {environment}; inhabited by {inhabitants}; mystery: {mystery}."
NAME: tuple[str, ...] = ("Oris-7", "Pelagos", "Vanta Minor", "Ilyra")
ENVIRONMENT: tuple[str, ...] = (
    "floating salt continents",
    "forests beneath clear ice",
    "permanent copper twilight",
    "mountains that migrate",
)
INHABITANTS: tuple[str, ...] = (
    "tidal engineers",
    "archival drones",
    "nomadic cloud farmers",
    "echo-based life",
)
MYSTERY: tuple[str, ...] = (
    "a signal older than its star",
    "one missing season",
    "ruins that appear in dreams",
    "gravity pauses every century",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            name=rng.choice(NAME),
            environment=rng.choice(ENVIRONMENT),
            inhabitants=rng.choice(INHABITANTS),
            mystery=rng.choice(MYSTERY),
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
