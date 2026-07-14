#!/usr/bin/env python3
"""Apply one move to a tiny 2×2 sliding-tile puzzle."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    board = [1, 2, 3, 0]
    for _ in range(10):
        zero = board.index(0)
        row, column = divmod(zero, 2)
        neighbors = [
            candidate
            for candidate in range(4)
            if abs(divmod(candidate, 2)[0] - row)
            + abs(divmod(candidate, 2)[1] - column)
            == 1
        ]
        swap = rng.choice(neighbors)
        board[zero], board[swap] = board[swap], board[zero]
    before = board.copy()
    if interactive:
        tile = int(input(f"Board {before}; tile to slide: "))
    else:
        zero = board.index(0)
        tile = board[
            next(
                candidate
                for candidate in range(4)
                if board[candidate]
                and abs(divmod(candidate, 2)[0] - divmod(zero, 2)[0])
                + abs(divmod(candidate, 2)[1] - divmod(zero, 2)[1])
                == 1
            )
        ]
    tile_index, zero_index = board.index(tile), board.index(0)
    adjacent = (
        abs(divmod(tile_index, 2)[0] - divmod(zero_index, 2)[0])
        + abs(divmod(tile_index, 2)[1] - divmod(zero_index, 2)[1])
        == 1
    )
    if adjacent:
        board[tile_index], board[zero_index] = board[zero_index], board[tile_index]
    return f"Before: {before}\nAfter:  {board}\nMove valid: {adjacent}"


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
