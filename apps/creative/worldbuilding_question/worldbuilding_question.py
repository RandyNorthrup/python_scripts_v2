#!/usr/bin/env python3
"""Ask focused questions that expose consequences in fictional worlds."""

from __future__ import annotations

import argparse
import random

PATTERN = "If {premise}, how does it change {system}, especially for {group}?"
PREMISE: tuple[str, ...] = (
    "memories can be traded",
    "night lasts a month",
    "roads choose destinations",
    "music controls weather",
)
SYSTEM: tuple[str, ...] = (
    "inheritance law",
    "food storage",
    "postal service",
    "public education",
)
GROUP: tuple[str, ...] = (
    "children",
    "traveling workers",
    "rural communities",
    "people without money",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            premise=rng.choice(PREMISE),
            system=rng.choice(SYSTEM),
            group=rng.choice(GROUP),
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
