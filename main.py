#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, one line, under 200 characters.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
and prints it. Deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

ENTRY = "HR called it a 'growth opportunity'; my paycheck called it the same job with more meetings."


def main() -> None:
    if not ENTRY or not ENTRY.strip():
        raise SystemExit("error: entry must not be empty or whitespace-only")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("error: entry must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("error: entry must be between 1 and 200 characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
