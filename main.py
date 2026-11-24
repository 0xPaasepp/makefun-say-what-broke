"""Say What Actually Broke.

Writes the single-line entry to /output/entry.txt, with no trailing
newline, after validating the line is well formed.
"""

import os

ENTRY_LINE = "The disk filled up with logs explaining why the disk was filling up. I deleted the explanation. Try again."
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry line is well formed and return it unchanged."""
    assert isinstance(text, str), "entry must be a string"
    assert text.strip(), "entry must not be blank"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.encode("utf-8").decode("utf-8") == text, "entry must survive a UTF-8 round-trip"
    return text


def main():
    line = validate_entry(ENTRY_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as out_file:
        out_file.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
