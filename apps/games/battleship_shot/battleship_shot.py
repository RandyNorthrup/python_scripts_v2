#!/usr/bin/env python3
"""Fire one shot at a hidden ship on a five-by-five grid."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    horizontal = rng.choice((True, False))
    start_row = rng.randrange(5 if horizontal else 3)
    start_column = rng.randrange(3 if horizontal else 5)
    ship = {
        (
            start_row + (0 if horizontal else offset),
            start_column + (offset if horizontal else 0),
        )
        for offset in range(3)
    }
    if interactive:
        shot = (int(input("Row 1-5: ")) - 1, int(input("Column 1-5: ")) - 1)
    else:
        shot = (2, 2)
    result = "hit" if shot in ship else "miss"
    visible_ship = sorted((row + 1, column + 1) for row, column in ship)
    return (
        f"Shot {shot[0] + 1},{shot[1] + 1}: {result}.\nDemo ship cells: {visible_ship}"
    )


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
