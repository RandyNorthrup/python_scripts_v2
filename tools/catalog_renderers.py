"""Render typed catalog specifications into standalone Python programs."""

from __future__ import annotations

import textwrap

from tools.catalog_models import (
    AppSpec,
    FileApp,
    FormulaApp,
    GameApp,
    GeneratorApp,
    QuizApp,
    TextApp,
)

HEADER = "#!/usr/bin/env python3\n"


def _module_imports(imports: tuple[str, ...]) -> str:
    """Render sorted import statements."""
    return "\n".join(
        sorted(
            imports, key=lambda statement: (statement.startswith("from "), statement)
        )
    )


def _indent_body(body: str) -> str:
    """Normalize and indent a function body."""
    return textwrap.indent(textwrap.dedent(body).strip(), "    ")


def render_formula(app: FormulaApp) -> str:
    """Render numeric calculator or planner."""
    signature = ", ".join(f"{item.name}: float" for item in app.parameters)
    validation_lines = "\n".join(
        f"    if {condition}:\n"
        f"        error_message = {message!r}\n"
        "        raise ValueError(error_message)"
        for condition, message in app.validations
    )
    validation_block = f"{validation_lines}\n" if validation_lines else ""
    result_lines = ",\n".join(
        f"        {label!r}: float({expression})" for label, expression in app.outputs
    )
    arguments = "\n".join(
        (
            f"    parser.add_argument('--{item.name.replace('_', '-')}', "
            f"type=float, default={item.default!r}, help={item.help_text!r})"
        )
        for item in app.parameters
    )
    call_args = ",\n".join(
        f"            {item.name}=float(args.{item.name})" for item in app.parameters
    )
    source = f'''\
"""{app.summary}"""

from __future__ import annotations

import argparse


def calculate({signature}) -> dict[str, float]:
    """Calculate and return named results."""
{validation_block}\
    return {{
{result_lines},
    }}


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
{arguments}
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    try:
        results = calculate(
{call_args},
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    for label, value in results.items():
        print(f"{{label}}: {{value:,.2f}}")


if __name__ == "__main__":
    main()
'''
    return HEADER + source


def render_text(app: TextApp) -> str:
    """Render text transformer or analyzer."""
    imports = _module_imports(("import argparse", *app.imports))
    body = _indent_body(app.body)
    source = f'''\
"""{app.summary}"""

from __future__ import annotations

{imports}


DEFAULT_TEXT = {app.default_text!r}


def transform(text: str) -> str:
    """Transform or analyze input text."""
{body}


def build_parser() -> argparse.ArgumentParser:
    """Build command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "text",
        nargs="?",
        default=DEFAULT_TEXT,
        help="Text to process.",
    )
    return parser


def main() -> None:
    """Run command-line interface."""
    args = build_parser().parse_args()
    print(transform(str(args.text)))


if __name__ == "__main__":
    main()
'''
    return HEADER + source


def render_generator(app: GeneratorApp) -> str:
    """Render deterministic creative generator."""
    bank_lines = "\n".join(
        f"{name.upper()}: tuple[str, ...] = {values!r}" for name, values in app.banks
    )
    format_args = ",\n".join(
        f"            {name}=rng.choice({name.upper()})" for name, _ in app.banks
    )
    source = f'''\
"""{app.summary}"""

from __future__ import annotations

import argparse
import random


PATTERN = {app.pattern!r}
{bank_lines}


def generate(seed: int, count: int) -> list[str]:
    """Generate reproducible ideas."""
    if count < 1:
        error_message = "count must be at least 1"
        raise ValueError(error_message)
    rng = random.Random(seed)
    return [
        PATTERN.format(
{format_args},
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
    print("\\n".join(f"{{index}}. {{idea}}" for index, idea in enumerate(ideas, 1)))


if __name__ == "__main__":
    main()
'''
    return HEADER + source


def render_quiz(app: QuizApp) -> str:
    """Render quiz with optional interactive play."""
    source = f'''\
"""{app.summary}"""

from __future__ import annotations

import argparse
import random


CARDS: tuple[tuple[str, str, str], ...] = {app.cards!r}


def normalize(value: str) -> str:
    """Normalize an answer for comparison."""
    return " ".join(value.casefold().strip().split())


def study_cards() -> str:
    """Return all cards as a compact study guide."""
    return "\\n".join(
        f"Q: {{question}}\\nA: {{answer}} — {{note}}"
        for question, answer, note in CARDS
    )


def play(seed: int) -> int:
    """Run an interactive quiz and return score."""
    cards = list(CARDS)
    random.Random(seed).shuffle(cards)
    score = 0
    for question, answer, note in cards:
        response = input(f"{{question}} ")
        if normalize(response) == normalize(answer):
            score += 1
            print("Correct.")
        else:
            print(f"Answer: {{answer}}")
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
        print(f"Score: {{score}}/{{len(CARDS)}}")
    else:
        print(study_cards())


if __name__ == "__main__":
    main()
'''
    return HEADER + source


def render_file(app: FileApp) -> str:
    """Render read-only filesystem tool."""
    imports = _module_imports(
        ("import argparse", "from pathlib import Path", *app.imports)
    )
    body = _indent_body(app.body)
    source = f'''\
"""{app.summary}"""

from __future__ import annotations

{imports}


def inspect_path(path: Path) -> str:
    """Inspect path without modifying it."""
{body}


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
'''
    return HEADER + source


def render_game(app: GameApp) -> str:
    """Render small terminal game."""
    imports = _module_imports(("import argparse", "import random", *app.imports))
    body = _indent_body(app.body)
    source = f'''\
"""{app.summary}"""

from __future__ import annotations

{imports}


def run_game(seed: int, *, interactive: bool) -> str:
    """Run game in interactive or automatic demo mode."""
{body}


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
'''
    return HEADER + source


def render_app(app: AppSpec) -> str:
    """Render one app according to specification type."""
    if isinstance(app, FormulaApp):
        return render_formula(app)
    if isinstance(app, TextApp):
        return render_text(app)
    if isinstance(app, GeneratorApp):
        return render_generator(app)
    if isinstance(app, QuizApp):
        return render_quiz(app)
    if isinstance(app, FileApp):
        return render_file(app)
    if isinstance(app, GameApp):
        return render_game(app)
    raise TypeError(type(app).__name__)
