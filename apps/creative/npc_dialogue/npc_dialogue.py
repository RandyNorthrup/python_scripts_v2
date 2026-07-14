#!/usr/bin/env python3
"""Generate tabletop NPC voices, needs, and opening lines."""

from __future__ import annotations

import argparse
import random

PATTERN = "{speaker} ({voice}) needs {need}. Opening: “{line}”"
SPEAKER: tuple[str, ...] = (
    "harbor clerk",
    "wandering herbalist",
    "apprentice ghost",
    "retired dragon",
)
VOICE: tuple[str, ...] = (
    "speaks in lists",
    "never uses names",
    "answers too quickly",
    "pauses for imaginary applause",
)
NEED: tuple[str, ...] = (
    "a harmless secret delivered",
    "help reading a modern map",
    "someone to verify a strange noise",
    "a replacement for a lost teacup",
)
LINE: tuple[str, ...] = (
    "You look like item three on my agenda.",
    "The road remembers you.",
    "No, that sound is definitely new.",
    "Please ignore the smoke; it is sentimental.",
)


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
            speaker=rng.choice(SPEAKER),
            voice=rng.choice(VOICE),
            need=rng.choice(NEED),
            line=rng.choice(LINE),
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
