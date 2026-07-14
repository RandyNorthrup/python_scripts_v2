#!/usr/bin/env python3
"""Generate small instructions for text-based geometric art."""

from __future__ import annotations

import argparse
import random

PATTERN = "Draw {shape} using {symbol}, size {size}, with {twist}."
SHAPE: tuple[str, ...] = ("a diamond", "nested squares", "a wave", "a spiral")
SYMBOL: tuple[str, ...] = ("#", "*", "+", "<>")
SIZE: tuple[str, ...] = ("7", "9", "12", "15")
TWIST: tuple[str, ...] = (
    "alternating gaps",
    "a mirrored center",
    "a gradient of density",
    "one broken edge",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            shape=rng.choice(SHAPE),
            symbol=rng.choice(SYMBOL),
            size=rng.choice(SIZE),
            twist=rng.choice(TWIST),
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
