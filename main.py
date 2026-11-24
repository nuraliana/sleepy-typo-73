#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun bounty entry.

Writes the single-line winning entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only, deterministic,
no network access.
"""

import os

ENTRY = "I texted my boss 'sorry, I was on mute' — autocorrect sent 'sorry, I was on nude' and now the whole team thinks I attend meetings naked."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)}-char entry to {path}")


if __name__ == "__main__":
    main()
