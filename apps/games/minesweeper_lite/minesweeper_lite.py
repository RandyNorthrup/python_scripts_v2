#!/usr/bin/env python3
"""Reveal one cell on a generated five-by-five minefield."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    mines = set(rng.sample(range(25), 5))
    if interactive:
        row = int(input("Row 1-5: ")) - 1
        column = int(input("Column 1-5: ")) - 1
    else:
        row, column = 2, 2
    index = row * 5 + column
    if row not in range(5) or column not in range(5):
        return "Cell outside board."
    if index in mines:
        return f"Cell {row + 1},{column + 1}: mine!"
    neighbors = sum(
        (near_row * 5 + near_column) in mines
        for near_row in range(max(0, row - 1), min(5, row + 2))
        for near_column in range(max(0, column - 1), min(5, column + 2))
    )
    return f"Cell {row + 1},{column + 1}: {neighbors} neighboring mines."


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
