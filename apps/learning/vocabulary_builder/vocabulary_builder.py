#!/usr/bin/env python3
"""Learn precise English vocabulary through short definitions."""

from __future__ import annotations

import argparse
import random

CARDS: tuple[tuple[str, str, str], ...] = (
    (
        "Word meaning brief and clear?",
        "concise",
        "Concise expression uses no unnecessary words.",
    ),
    (
        "Word meaning able to recover quickly?",
        "resilient",
        "Resilience is recovery after difficulty.",
    ),
    (
        "Word meaning occurring at irregular intervals?",
        "sporadic",
        "Sporadic events are scattered or occasional.",
    ),
    (
        "Word meaning careful and exact?",
        "meticulous",
        "Meticulous work pays close attention to detail.",
    ),
)


def normalize(value: str) -> str:
    """Normalize an answer for comparison."""
    return " ".join(value.casefold().strip().split())


def study_cards() -> str:
    """Return all cards as a compact study guide."""
    return "\n".join(
        f"Q: {question}\nA: {answer} — {note}" for question, answer, note in CARDS
    )


def play(seed: int) -> int:
    """Run an interactive quiz and return score."""
    cards = list(CARDS)
    random.Random(seed).shuffle(cards)
    score = 0
    for question, answer, note in cards:
        response = input(f"{question} ")
        if normalize(response) == normalize(answer):
            score += 1
            print("Correct.")
        else:
            print(f"Answer: {answer}")
        print(note)
    return score


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--play", action="store_true", help="Start interactive quiz.")
    parser.add_argument("--seed", type=int, default=42, help="Question order seed.")
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    if bool(args.play):
        score = play(int(args.seed))
        print(f"Score: {score}/{len(CARDS)}")
    else:
        print(study_cards())


if __name__ == "__main__":
    main()
