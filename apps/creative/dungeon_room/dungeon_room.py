#!/usr/bin/env python3
"""Build tabletop dungeon rooms with hazards, clues, and rewards."""

from __future__ import annotations

import argparse
import random

PATTERN = "{room}; hazard: {hazard}; clue: {clue}; reward: {reward}."
ROOM: tuple[str, ...] = (
    "A flooded observatory",
    "A kitchen frozen mid-feast",
    "A hall of whispering portraits",
    "A root-filled chapel",
)
HAZARD: tuple[str, ...] = (
    "rising water",
    "polite mimic furniture",
    "a repeating minute",
    "sleeping glass insects",
)
CLUE: tuple[str, ...] = (
    "star positions scratched into tile",
    "a recipe missing one ingredient",
    "one portrait looks away",
    "roots spell a name",
)
REWARD: tuple[str, ...] = (
    "a compass that points to promises",
    "a restorative silver apple",
    "a key made of warm wax",
    "a map visible only in rain",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            room=rng.choice(ROOM),
            hazard=rng.choice(HAZARD),
            clue=rng.choice(CLUE),
            reward=rng.choice(REWARD),
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
