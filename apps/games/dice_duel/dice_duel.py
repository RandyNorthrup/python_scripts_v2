#!/usr/bin/env python3
"""Roll two dice against a computer opponent for three rounds."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    player_score = 0
    computer_score = 0
    lines = []
    for round_number in range(1, 4):
        if interactive:
            input(f"Press Enter to roll round {round_number}.")
        player_roll = rng.randint(1, 6) + rng.randint(1, 6)
        computer_roll = rng.randint(1, 6) + rng.randint(1, 6)
        player_score += player_roll > computer_roll
        computer_score += computer_roll > player_roll
        lines.append(
            f"Round {round_number}: you {player_roll}, computer {computer_roll}"
        )
    winner = (
        "you"
        if player_score > computer_score
        else ("computer" if computer_score > player_score else "draw")
    )
    return "\n".join((*lines, f"Winner: {winner}"))


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
