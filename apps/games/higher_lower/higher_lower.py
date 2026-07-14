#!/usr/bin/env python3
"""Predict whether a second card will be higher than the first."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    first, second = rng.sample(range(1, 14), 2)
    choice = (
        input("Will next card be higher or lower? ").strip().casefold()
        if interactive
        else "higher"
    )
    actual = "higher" if second > first else "lower"
    result = "Correct!" if choice == actual else f"No, it was {actual}."
    return f"First: {first}\nSecond: {second}\nYour choice: {choice}\n{result}"


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
