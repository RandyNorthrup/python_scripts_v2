#!/usr/bin/env python3
"""Draft compact fictional logo briefs for design practice."""

from __future__ import annotations

import argparse
import random

PATTERN = "Brand {brand}: {offer}; {personality}; motif {motif}; avoid {avoid}."
BRAND: tuple[str, ...] = (
    "Northloop",
    "Kindling Lab",
    "Pebble & Pine",
    "Second Sunrise",
)
OFFER: tuple[str, ...] = (
    "repair workshops",
    "science kits",
    "outdoor stationery",
    "community breakfast",
)
PERSONALITY: tuple[str, ...] = (
    "clever and calm",
    "warm and experimental",
    "rugged but precise",
    "optimistic and local",
)
MOTIF: tuple[str, ...] = (
    "interlocking path",
    "controlled spark",
    "stacked landscape",
    "rising bowl",
)
AVOID: tuple[str, ...] = (
    "literal tools",
    "generic atoms",
    "mountain clichés",
    "sunburst clichés",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            brand=rng.choice(BRAND),
            offer=rng.choice(OFFER),
            personality=rng.choice(PERSONALITY),
            motif=rng.choice(MOTIF),
            avoid=rng.choice(AVOID),
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
