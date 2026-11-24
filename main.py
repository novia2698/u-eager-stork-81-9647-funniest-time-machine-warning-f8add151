#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single one-line warning label for a time machine to
/output/entry.txt, the file the sealed scorer gates on (UTF-8 text,
1 to 120 characters, not only whitespace).

The label: a deadpan safety notice built on the grandfather paradox —
the classic time-travel hazard — with the punchline saved for the last
few words, where the reader least expects it.
"""

import os

LABEL = (
    "WARNING: Do not kill your grandfather. "
    "Doing so voids your warranty, your existence, and your deposit."
)


def main() -> None:
    if "\n" in LABEL or "\r" in LABEL:
        raise ValueError("label must be a single line")
    if not (1 <= len(LABEL) <= 120):
        raise ValueError(f"label is {len(LABEL)} chars, must be 1-120")
    if not LABEL.strip():
        raise ValueError("label must not be only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LABEL)
    print(LABEL)


if __name__ == "__main__":
    main()
