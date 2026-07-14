#!/usr/bin/env python3
"""Navigate a small generated obstacle grid toward a goal."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    size = 7
    blocked = set(rng.sample(list(range(1, size * size - 1)), 10))
    blocked -= {1, size}
    position = 0
    moves = (
        input("Moves using UDLR: ").strip().upper() if interactive else "RRDDRRDDRRDD"
    )
    for move in moves:
        row, column = divmod(position, size)
        candidate = {
            "U": (row - 1, column),
            "D": (row + 1, column),
            "L": (row, column - 1),
            "R": (row, column + 1),
        }.get(move, (row, column))
        next_row, next_column = candidate
        next_position = next_row * size + next_column
        if (
            0 <= next_row < size
            and 0 <= next_column < size
            and next_position not in blocked
        ):
            position = next_position
    grid = [
        "#"
        if index in blocked
        else ("P" if index == position else ("G" if index == size * size - 1 else "."))
        for index in range(size * size)
    ]
    return "\n".join(
        "".join(grid[row * size : (row + 1) * size]) for row in range(size)
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
