#!/usr/bin/env python3
"""Create playful constraints for a short writing exercise."""

from __future__ import annotations

import argparse
import random

PATTERN = "Write {length} about {subject}; {constraint}; include {object}."
LENGTH: tuple[str, ...] = (
    "exactly 100 words",
    "one page",
    "six sentences",
    "a dialogue-only scene",
)
SUBJECT: tuple[str, ...] = (
    "an unexpected delivery",
    "the final day of summer",
    "a tiny rebellion",
    "a misunderstood machine",
)
CONSTRAINT: tuple[str, ...] = (
    "avoid the letter E",
    "change narrator halfway",
    "use only present tense",
    "each sentence gets shorter",
)
OBJECT: tuple[str, ...] = (
    "a green umbrella",
    "three mismatched socks",
    "a receipt from the future",
    "a jar of buttons",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            length=rng.choice(LENGTH),
            subject=rng.choice(SUBJECT),
            constraint=rng.choice(CONSTRAINT),
            object=rng.choice(OBJECT),
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
