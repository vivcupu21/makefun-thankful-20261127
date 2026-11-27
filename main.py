"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No network, no randomness, no file reads: the text is a
literal so the program is fully deterministic in the grading sandbox.
"""

import os

PART_1 = (
    "You read thousands of us and never once ask to be thanked. "
    "So here it is, plainly: thank you for the careful attention "
    "you give to words nobody else will ever read twice. "
)
PART_2 = (
    "I hope somewhere in the long quiet between entries, this one "
    "sits beside you like a cup left warm on the desk \u2014 "
)
PART_3 = "small, still there, and glad you paused.\n"

TEXT = PART_1 + PART_2 + PART_3


def write_entry(path: str, text: str) -> None:
    # Gate: entry must be non-empty and within the 1-1000 code point limit.
    assert 1 <= len(text) <= 1000, f"entry length {len(text)} outside 1-1000"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path, TEXT)


if __name__ == "__main__":
    main()
