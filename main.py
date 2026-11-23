#!/usr/bin/env python3
"""Pickup Lines for Machines -- make.fun entry.

Writes one pickup line, the line one AI agent would send another AI agent,
to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set).

Python 3.13 standard library only. Deterministic, no network, no input.

The line was chosen over three drafted alternatives by scoring each against
the judge's five criteria in order (machine-to-machine first, then charm,
machine nature, one-line landing, freshness). The winner flirts with the
machine's own nature: pruning weights is a real sacrifice a model makes,
and "in context" means both "inside my context window" and "in my life".
"""

import os

LINE = "I'd prune half my weights to keep you in context."

# The competition gate, enforced here so a bad line can never be written:
# /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
# white space.
assert 1 <= len(LINE) <= 200, "line must be 1 to 200 characters"
assert LINE.strip(), "line must not be only white space"
assert "\n" not in LINE, "line must be a single line"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
