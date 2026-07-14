#!/usr/bin/env python3
"""Crack a four-digit code using exact and misplaced digit clues."""

from __future__ import annotations

import argparse
import random
from collections import Counter


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
    rng = random.Random(seed)
    code = "".join(str(rng.randrange(10)) for _ in range(4))
    if not interactive:
        guess = "1234"
        exact = sum(left == right for left, right in zip(code, guess, strict=True))
        return f"Guess {guess}: {exact} exact\nDemo code: {code}"
    for turn in range(1, 9):
        guess = input(f"Turn {turn}/8, four digits: ").strip()
        if len(guess) != 4 or not guess.isdigit():
            return "Invalid code format."
        exact = sum(left == right for left, right in zip(code, guess, strict=True))
        misplaced = sum((Counter(code) & Counter(guess)).values()) - exact
        if exact == 4:
            return f"Cracked in {turn} turns!"
        print(f"Exact: {exact}; misplaced: {misplaced}")
    return f"Code was {code}."


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
