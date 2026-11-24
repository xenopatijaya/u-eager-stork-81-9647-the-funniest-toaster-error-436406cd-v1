#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes exactly one line — the error message a kitchen toaster shows its
owner — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The entry (48 characters, one line):
    ERROR: Fork detected. We have talked about this.
"""

import os
import sys

ENTRY = "ERROR: Fork detected. We have talked about this."


def main() -> int:
    # Gate: the entry must be 1-120 UTF-8 characters, a single line, and
    # contain no leading/trailing whitespace.
    if not 1 <= len(ENTRY) <= 120:
        print("entry is %d characters, outside the 1-120 gate" % len(ENTRY),
              file=sys.stderr)
        return 1
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        print("entry is not a single clean line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write (temp file + os.replace) so an interrupted run can
    # never leave a truncated entry behind.
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    # Round-trip check: what was written must be exactly the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != ENTRY:
            print("round-trip mismatch", file=sys.stderr)
            return 1
    print(ENTRY)
    print("(%d characters)" % len(ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
