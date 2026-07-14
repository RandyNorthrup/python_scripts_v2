# Password Strength Coach

Score password variety and length without storing the input.

## What it does

This standalone Python 3 command-line app runs with a useful built-in demo when no arguments are supplied. It uses clear text output, no color-only meaning, and keyboard-only controls where interaction is available.

## How to use it

```bash
python3 password_strength.py
python3 password_strength.py "your input here"
```

Run `python3 password_strength.py --help` for every option. Interactive quizzes and games only prompt when `--play` is supplied.

## How to modify it

Edit `transform()` to change the text rule; keep it pure so it remains easy to test. The file is self-contained, so you can copy this directory anywhere with Python 3.11 or newer.

After an edit, run repository checks from the project root:

```bash
make verify
```

## Requirements

- Python 3.11 or newer
- No third-party runtime packages

`requirements.txt` is intentionally empty except for a comment because this app uses only the Python standard library.
