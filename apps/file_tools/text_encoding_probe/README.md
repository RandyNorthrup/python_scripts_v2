# Text Encoding Probe

Check whether a file decodes as UTF-8, UTF-8 with BOM, or Latin-1.

## What it does

This standalone Python 3 command-line app runs with a useful built-in demo when no arguments are supplied. It uses clear text output, no color-only meaning, and keyboard-only controls where interaction is available.

## How to use it

```bash
python3 text_encoding_probe.py
python3 text_encoding_probe.py /path/to/file-or-directory
```

Run `python3 text_encoding_probe.py --help` for every option. Interactive quizzes and games only prompt when `--play` is supplied.

## How to modify it

Edit `inspect_path()` to add analysis. Keep the tool read-only unless its name and documentation clearly announce writes. The file is self-contained, so you can copy this directory anywhere with Python 3.11 or newer.

After an edit, run repository checks from the project root:

```bash
make verify
```

## Requirements

- Python 3.11 or newer
- No third-party runtime packages

`requirements.txt` is intentionally empty except for a comment because this app uses only the Python standard library.
