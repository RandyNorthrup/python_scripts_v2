#!/usr/bin/env python3
"""Guess letters in a short word before six misses."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    word = rng.choice(("planet", "bridge", "python", "garden"))
    if not interactive:
        return f"Puzzle: {' '.join('_' for _ in word)}\nDemo answer: {word}"
    guessed: set[str] = set()
    misses = 0
    while misses < 6 and any(letter not in guessed for letter in word):
        print(" ".join(letter if letter in guessed else "_" for letter in word))
        letter = input("Letter: ").strip().casefold()[:1]
        if letter in guessed:
            continue
        guessed.add(letter)
        if letter not in word:
            misses += 1
    result = "Won" if all(letter in guessed for letter in word) else "Lost"
    return f"{result}! Word: {word}"


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
