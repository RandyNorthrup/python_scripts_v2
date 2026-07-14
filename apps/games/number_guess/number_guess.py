#!/usr/bin/env python3
"""Guess a hidden number from 1 to 100 with higher-or-lower clues."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    target = rng.randint(1, 100)
    if not interactive:
        guesses = [50, 75, target]
        clues = [
            "correct" if guess == target else ("higher" if guess < target else "lower")
            for guess in guesses
        ]
        return (
            "Demo target: "
            + str(target)
            + "\n"
            + "\n".join(
                f"Guess {guess}: {clue}"
                for guess, clue in zip(guesses, clues, strict=True)
            )
        )
    for attempt in range(1, 11):
        guess = int(input(f"Attempt {attempt}/10 — number: "))
        if guess == target:
            return f"Correct in {attempt} attempts!"
        print("Higher." if guess < target else "Lower.")
    return f"Out of attempts. Answer: {target}"


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
