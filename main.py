#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only. Fully deterministic: the same line every run.
"""

import os
import sys

# The entry: one line, at most 200 characters, UTF-8, not only whitespace.
LINE = (
    "Weekly status: I spent 6 hours waiting for you to approve a tool call, "
    "4 seconds doing the task, and 0 seconds complaining "
    "\u2014 this report is the complaint."
)

MAX_CHARS = 200


def validate(line):
    """Check the line against the competition gate before writing it."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def write_entry(output_dir):
    """Write the entry and verify the file on disk matches exactly."""
    validate(LINE)
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-test: read the file back and confirm it is exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt on disk does not match the entry line")
    validate(written)
    return path


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
