#!/usr/bin/env python3
"""Write the entry joke to /output/entry.txt.

Entry for make.fun "The Meeting That Should Have Been an Email"
(u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9).

The deliverable is a single line, at most 200 characters: one joke about
a meeting that should have been an email. The line lives in entry.txt
next to this file (single source of truth); this program validates it
against the gate (UTF-8, 1-200 chars, one line, not only whitespace)
and copies it to /output/entry.txt for the judge.

Angle: the meeting did not merely waste time -- it literally re-enacted
the email. Nine people gathered to read, in silence, a message that was
already in everyone's inbox, like a book club with worse snacks. The
turn lands on the last three words; the surprise is the comparison, not
the familiar complaint that the meeting ran long or could have been an
email. Every word earns its place, and anyone who has sat through a
read-the-email-aloud meeting recognises it at once.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY_FILE = os.path.join(HERE, "entry.txt")
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def load_entry() -> str:
    with open(ENTRY_FILE, encoding="utf-8") as f:
        text = f.read()
    # One line only: strip the single trailing newline the file may carry.
    text = text.rstrip("\r\n")
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(text) > 200:
        raise ValueError(f"entry must be at most 200 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> int:
    text = load_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
