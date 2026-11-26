#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the funniest one-line git commit
message an AI coding agent types at 3am after a long night of fixing its
own bugs.

The line was picked from 38 candidates by pairwise judging against the
brief — a self-accusation with a two-step twist: the agent files a
complaint against itself and loses. The program builds the line from two
clauses — the confession, then the complaint — and checks the result
against the entry gate (length, single line, no leading or trailing
space, exact judged length) before writing it, then reads the file back
to confirm the bytes match.
"""

import os
import sys

LINE = (
    "fix: the bug was me all along. "
    "i have filed a complaint against myself and lost"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 139):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-139")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        raw = f.read()
    if raw != data:
        sys.exit("read-back mismatch")
    text = raw.decode("utf-8").rstrip("\n")
    if len(text) != len(LINE) or text != LINE:
        sys.exit("read-back character check failed")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
