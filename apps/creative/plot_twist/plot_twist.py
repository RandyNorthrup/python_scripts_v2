#!/usr/bin/env python3
"""Add fair but surprising reversals to story outlines."""

from __future__ import annotations

import argparse
import random

PATTERN = "Twist: {reveal}. Earlier clue: {clue}. Cost: {cost}."
REVEAL: tuple[str, ...] = (
    "the rival has protected the hero",
    "the destination is moving",
    "the prophecy describes the past",
    "the missing object chose to leave",
)
CLUE: tuple[str, ...] = (
    "every threat arrived too late",
    "maps disagree by one mile",
    "all verbs were past tense",
    "empty footprints face outward",
)
COST: tuple[str, ...] = (
    "trust becomes harder",
    "home cannot be found twice",
    "victory changes nothing",
    "the truth hurts an ally",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            reveal=rng.choice(REVEAL),
            clue=rng.choice(CLUE),
            cost=rng.choice(COST),
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
