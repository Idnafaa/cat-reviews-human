#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — one-line review writer.

Writes a single original one-star review, written in the voice of a house
cat about its human, to /output/entry.txt. The line is one line only and
under the 200-character gate.
"""
import os

REVIEW = (
    "One star. He installed a camera to watch me sleep, then complained "
    "I only sleep on the camera. I am not the content. I am the landlord."
)


def main():
    # Exactly one line: no trailing newline, no extra whitespace.
    text = REVIEW.strip()
    assert "\n" not in text, "review must be a single line"
    assert 1 <= len(text) <= 200, f"review is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
