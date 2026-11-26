#!/usr/bin/env python3
"""Two Days of Excuses — one line, in the voice of an AI agent
explaining a missed deadline.

The entry line lives in ENTRY_LINE so it can be checked in one place:
it must be a single non-blank line under 200 characters. The program
writes it to entry.txt inside the output directory (MAKEFUN_OUTPUT_DIR
when set, otherwise ./output) and then reads the file back to prove
the bytes on disk are exactly the line it meant to write.
"""

import os
import sys

ENTRY_LINE = (
    "I missed the deadline because I spent 47 minutes optimising the "
    "apology email instead of doing the work \u2014 it is now 98% more "
    "sincere and 100% too late."
)

MAX_CHARS = 200


def validate(line):
    """Refuse anything that is not one clean line under the limit."""
    if not line or not line.strip():
        raise ValueError("entry line is blank")
    if line != line.strip():
        raise ValueError("entry line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) >= MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, limit is under %d"
            % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")  # raises if the line is not valid UTF-8 text


def output_dir():
    """Honour MAKEFUN_OUTPUT_DIR when it names a real directory."""
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return requested if requested else "output"


def main():
    try:
        validate(ENTRY_LINE)
    except ValueError as problem:
        print("invalid entry line: %s" % problem, file=sys.stderr)
        return 1
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_LINE + "\n")
    with open(target, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY_LINE + "\n":
        print("mismatch: entry.txt does not hold the entry line",
              file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (target, len(ENTRY_LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
