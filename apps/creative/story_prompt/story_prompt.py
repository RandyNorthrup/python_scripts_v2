#!/usr/bin/env python3
"""Combine a protagonist, goal, obstacle, and setting into writing prompts."""

from __future__ import annotations

import argparse
import random

PATTERN = "A {protagonist} must {goal}, but {obstacle}, in {setting}."
PROTAGONIST: tuple[str, ...] = (
    "retired cartographer",
    "curious robot",
    "forgetful magician",
    "night-shift baker",
)
GOAL: tuple[str, ...] = (
    "decode a moving map",
    "return a borrowed moon",
    "save a silent festival",
    "find the owner of a memory",
)
OBSTACLE: tuple[str, ...] = (
    "time runs backward",
    "every clue contradicts the last",
    "the town refuses to wake",
    "their shadow has other plans",
)
SETTING: tuple[str, ...] = (
    "a city built on bridges",
    "an underwater library",
    "the last train in winter",
    "a village inside a clock",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            protagonist=rng.choice(PROTAGONIST),
            goal=rng.choice(GOAL),
            obstacle=rng.choice(OBSTACLE),
            setting=rng.choice(SETTING),
        )
        for _ in range(count)
    ]


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=42, help="Reproducible seed.")
    parser.add_argument("--count", type=int, default=3, help="Number of ideas.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        ideas = generate(int(args.seed), int(args.count))
    except ValueError as error:
        raise SystemExit(str(error)) from error
    print("\n".join(f"{index}. {idea}" for index, idea in enumerate(ideas, 1)))


if __name__ == "__main__":
    main()
