#!/usr/bin/env python3
"""Change one letter at a time to transform one word into another."""

from __future__ import annotations

import argparse
import itertools
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    ladders = (
        ("cold", "cord", "card", "ward", "warm"),
        ("head", "heal", "teal", "tell", "tall", "tail"),
    )
    ladder = rng.choice(ladders)
    if not interactive:
        return f"Puzzle: {ladder[0]} -> {ladder[-1]}\nOne answer: {' -> '.join(ladder)}"
    response = (
        input(f"Enter comma-separated ladder from {ladder[0]} to {ladder[-1]}: ")
        .casefold()
        .split(",")
    )
    words = [word.strip() for word in response]
    valid = (
        words[0] == ladder[0]
        and words[-1] == ladder[-1]
        and all(
            sum(a != b for a, b in zip(left, right, strict=True)) == 1
            for left, right in itertools.pairwise(words)
        )
    )
    return "Valid ladder!" if valid else f"Example: {' -> '.join(ladder)}"


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--play", action="store_true", help="Enable interactive play.")
    parser.add_argument("--seed", type=int, default=42, help="Reproducible game seed.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    print(run_game(int(args.seed), interactive=bool(args.play)))


if __name__ == "__main__":
    main()
