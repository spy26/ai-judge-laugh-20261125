#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, one line, under 200 characters.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
and prints it. Deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

ENTRY = "HR called it a 'growth opportunity'; my paycheck called it the same job with more meetings."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
