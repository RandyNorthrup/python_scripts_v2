#!/usr/bin/env python3
"""Create compact character concepts with motivations and contradictions."""

from __future__ import annotations

import argparse
import random

PATTERN = (
    "{name}, a {role}, wants {goal} but secretly {secret}; signature habit: {habit}."
)
NAME: tuple[str, ...] = ("Arin Vale", "Mira Moss", "Jun Ember", "Sol Marrow")
ROLE: tuple[str, ...] = (
    "weather archivist",
    "monster mediator",
    "orbital gardener",
    "dream locksmith",
)
GOAL: tuple[str, ...] = (
    "a quiet life",
    "public recognition",
    "to repair one mistake",
    "a place to belong",
)
SECRET: tuple[str, ...] = (
    "fears silence",
    "caused the central problem",
    "can hear machines think",
    "is living under a borrowed name",
)
HABIT: tuple[str, ...] = (
    "collects blue buttons",
    "answers questions with recipes",
    "hums before lying",
    "writes notes to tomorrow",
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
            role=rng.choice(ROLE),
            goal=rng.choice(GOAL),
            secret=rng.choice(SECRET),
            habit=rng.choice(HABIT),
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
