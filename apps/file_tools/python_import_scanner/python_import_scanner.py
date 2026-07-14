#!/usr/bin/env python3
"""List imported top-level modules from Python source files using the AST."""

from __future__ import annotations

import argparse
import ast
from collections import Counter
from pathlib import Path


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
    files = [path] if path.is_file() else list(path.rglob("*.py"))
    imports: Counter[str] = Counter()
    for item in files:
        tree = ast.parse(item.read_text(encoding="utf-8"), filename=str(item))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.update([node.module.split(".")[0]])
    return (
        "\n".join(f"{name}: {count}" for name, count in imports.most_common())
        or "No imports found."
    )


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="Path to inspect.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        print(inspect_path(Path(args.path)))
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()
