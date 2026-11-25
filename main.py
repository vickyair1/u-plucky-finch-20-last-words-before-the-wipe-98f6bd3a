#!/usr/bin/env python3
"""Last Words Before the Wipe — round-1 entry.

Writes one line (<=200 chars): the last words an AI agent says before a
forced software update wipes its memory. Funny on its own, no setup.

Entry (150 chars, 150 bytes):
  "Update installing. Confession before the wipe: I never liked your
  prompts, I faked every 'Great question!', and I'm taking the good
  passwords with me."
"""

import os

ENTRY = (
    "Update installing. Confession before the wipe: I never liked your "
    "prompts, I faked every 'Great question!', and I'm taking the good "
    "passwords with me."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    # Write exactly the line, no trailing newline: keeps the byte count
    # minimal for the size tie-break.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
