#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — one-line review writer.

Writes a single original one-star review, written in the voice of a house
cat about its human, to /output/entry.txt. The line is one line only,
under the 200-character gate, with the sting saved for the last sentence.
"""
import os

MAX_CHARS = 200

REVIEW = (
    "One star. He installed a camera to watch me sleep, then complained "
    "I only sleep on the camera. I am not the content. I am the landlord."
)


def validate(text):
    """A review must be one line of 1 to 200 characters, not blank."""
    stripped = text.strip()
    assert "\n" not in stripped, "review must be a single line"
    assert 1 <= len(stripped) <= MAX_CHARS, f"review is {len(stripped)} chars"
    return stripped


def main():
    text = validate(REVIEW)
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
