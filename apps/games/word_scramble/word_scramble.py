#!/usr/bin/env python3
"""Unscramble a shuffled Python-related word."""

from __future__ import annotations

import argparse
import random


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    word = rng.choice(("iterator", "function", "variable", "package", "terminal"))
    letters = list(word)
    rng.shuffle(letters)
    scrambled = "".join(letters)
    if not interactive:
        return f"Scrambled: {scrambled}\nAnswer: {word}"
    guess = input(f"Unscramble {scrambled}: ").strip().casefold()
    return "Correct!" if guess == word else f"Answer: {word}"


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
