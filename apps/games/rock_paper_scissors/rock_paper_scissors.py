#!/usr/bin/env python3
"""Play one classic hand-game round against the computer."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    choices = ("rock", "paper", "scissors")
    computer = rng.choice(choices)
    player = (
        input("rock, paper, or scissors? ").strip().casefold()
        if interactive
        else "rock"
    )
    if player not in choices:
        return "Invalid choice."
    wins = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    outcome = (
        "draw"
        if player == computer
        else ("win" if (player, computer) in wins else "lose")
    )
    return f"You: {player}\nComputer: {computer}\nResult: {outcome}"


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
