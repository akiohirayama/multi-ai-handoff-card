"""Command line: handoff-card path/to/card.json (or - for stdin)."""

import json
import sys

from .check import check


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: handoff-card CARD.json  (use - to read from stdin)", file=sys.stderr)
        return 2
    try:
        if args[0] == "-":
            card = json.load(sys.stdin)
        else:
            with open(args[0], encoding="utf-8") as f:
                card = json.load(f)
    except (OSError, ValueError) as e:
        print(f"cannot read card: {e}", file=sys.stderr)
        return 2
    problems = check(card)
    for p in problems:
        print("-", p)
    print("DONE" if not problems else "NOT DONE")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
