#!/usr/bin/env python3
"""Play a compact tic-tac-toe match against random moves."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    board = [" "] * 9
    wins = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    turn = "X"
    while " " in board and not any(
        board[a] == board[b] == board[c] != " " for a, b, c in wins
    ):
        available = [index for index, value in enumerate(board) if value == " "]
        if interactive and turn == "X":
            move = (
                int(
                    input(
                        f"Cells 1-9, available {[index + 1 for index in available]}: "
                    )
                )
                - 1
            )
            if move not in available:
                return "Invalid move."
        else:
            move = rng.choice(available)
        board[move] = turn
        turn = "O" if turn == "X" else "X"
    rows = [" | ".join(board[index : index + 3]) for index in range(0, 9, 3)]
    winner = next(
        (board[a] for a, b, c in wins if board[a] == board[b] == board[c] != " "),
        "draw",
    )
    return "\n---------\n".join(rows) + f"\nWinner: {winner}"


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
