#!/usr/bin/env python3
"""Combine ingredients, techniques, and flavor directions for cooking experiments."""

from __future__ import annotations

import argparse
import random

PATTERN = "Try {ingredient} with {partner}, {technique}, finished with {finish}."
INGREDIENT: tuple[str, ...] = ("chickpeas", "sweet potato", "mushrooms", "pears")
PARTNER: tuple[str, ...] = ("smoked paprika", "miso", "rosemary", "toasted sesame")
TECHNIQUE: tuple[str, ...] = (
    "roasted until crisp",
    "folded into flatbread",
    "simmered into a thick stew",
    "grilled on skewers",
)
FINISH: tuple[str, ...] = ("lemon yogurt", "chili oil", "fresh herbs", "crushed nuts")


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            ingredient=rng.choice(INGREDIENT),
            partner=rng.choice(PARTNER),
            technique=rng.choice(TECHNIQUE),
            finish=rng.choice(FINISH),
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
