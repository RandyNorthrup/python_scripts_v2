#!/usr/bin/env python3
"""Convert bytes into binary storage units."""

from __future__ import annotations

import argparse


def calculate(byte_count: float) -> dict[str, float]:
    """Calculate and return named results."""
    if byte_count < 0:
        error_message = "byte count cannot be negative"
        raise ValueError(error_message)
    return {
        "KiB": float(byte_count / 1024),
        "MiB": float(byte_count / 1024**2),
        "GiB": float(byte_count / 1024**3),
    }


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--byte-count", type=float, default=1048576.0, help="Number of bytes."
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
            byte_count=float(args.byte_count),
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{label}: {value:,.2f}")


if __name__ == "__main__":
    main()
