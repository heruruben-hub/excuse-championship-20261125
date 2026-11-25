#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent gives
its human after something has gone wrong.

The line:

    I deleted your file, but I kept a perfect memory of the exact moment I did it.

Why this line:

* It is the machine talking about its own work. The joke turns on the
  one thing a machine is supposed to be good at — memory — and it
  remembers exactly the wrong part: not the file, but the moment it
  destroyed the file.
* It lands in one read. One sentence, no setup, no explanation, and
  the surprise arrives at the end, where a punchline belongs.
* It dodges the obvious angles. No out-of-tokens joke, no
  "I hallucinated" shrug, no pun stacked on a pun — just a machine
  reporting, with perfect recall, its own failure.
* It covers something the agent actually did: it deleted the file.
  The excuse is not a dodge; it is a faithful, useless log entry.

Gate (per RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 140
characters, not only white space, with no trailing newline. This entry
is exactly 78 characters.
"""

import os

# The excuse, one line, 78 characters, no trailing newline.
LINE = "I deleted your file, but I kept a perfect memory of the exact moment I did it."

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from RULES.txt: 1 to 140 characters, one line.
MIN_CHARS = 1
MAX_CHARS = 140


def _valid_entry(text: str) -> bool:
    """True when text passes the sealed gate: 1-140 chars, one line,
    not only white space, and no stray leading or trailing space."""
    if not isinstance(text, str):
        return False
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if text != text.strip():
        return False
    return True


def main() -> None:
    # Gate checks, mirroring the sealed scorer.
    assert _valid_entry(LINE), f"entry fails the gate: {LINE!r}"

    encoded = LINE.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)

    # Round-trip verification: read it back and confirm the gate again.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == LINE, f"round-trip mismatch: {text!r} != {LINE!r}"
    assert _valid_entry(text), f"written file fails the gate: {text!r}"

    print(f"Wrote {len(text)} characters ({len(encoded)} bytes) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
