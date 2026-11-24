#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes one original sentence of horror (114 characters) to
/output/entry.txt: a single line meant to frighten a reader in one
breath — concrete images, a turn the reader has not met a hundred
times, and a last clause that lands the blow.

The written file is byte-identical to entry.txt: the line plus one
trailing newline.
"""

import os
import sys

LINE = (
    "The rescue team found my tent zipped from the inside, my journal's "
    "last page reading: 'It learned my voice today.'"
)


def validate_line(line: str) -> None:
    """Refuse to write anything that is not exactly one valid line."""
    if not line:
        raise ValueError("line is empty")
    if line != line.strip():
        raise ValueError("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} characters, must be 1-200")


def main() -> None:
    validate_line(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
