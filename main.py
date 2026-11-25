#!/usr/bin/env python3
"""Funniest Autocorrect Fail — writes one autocorrect-fail line to entry.txt.

The program reads the entry line from entry.txt next to this script,
validates it against the competition gate (UTF-8, 1-199 characters,
not only whitespace), and writes it to <OUTPUT_DIR>/entry.txt
(default /output/entry.txt, the path the grader reads).
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load_entry() -> str:
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
        return f.read().strip()


def main() -> int:
    text = load_entry()
    if not text or text.isspace():
        print("entry is empty or whitespace only", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 199:
        print(f"entry length {len(text)} out of gate range 1-199", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
