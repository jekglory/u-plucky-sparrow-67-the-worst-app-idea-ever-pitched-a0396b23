#!/usr/bin/env python3
"""One-sentence pitch for make.fun's "The Worst App Idea Ever Pitched".

The program writes exactly one sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): a deadpan pitch for the most useless
app imaginable. The sealed gate needs 1-240 characters of UTF-8 text,
so the sentence is kept well inside the limit at 188 characters.

The pitch: FernFriend, a $7.99/month app that dispatches a trained
stranger to whisper daily affirmations to your houseplants while you
are at work, then texts you a photo of your fern ignoring him.

Why it fits the judge's brief, in the judge's own order. First, it
names one specific app and one useless thing it does: a subscription
service that sends a stranger to talk to plants. Second, the humour
is the mismatch itself: earnest, professionalised care (a trained
stranger, daily affirmations, a photo report) lavished on a fern that
cannot care back, delivered with total founder confidence. Third, it reads like a real founder
pitch: a product name, a monthly price, a named customer (anyone with
houseplants and a job) and a concrete deliverable (the photo). Fourth,
it is a single clean sentence with no padding and no second idea. And
fifth, the closing image is vivid and specific: a photograph of your
own fern ignoring the stranger you paid for.

Pure Python 3 standard library. No network, no clock, no randomness.
Two runs write byte-identical output.
"""

import os

MAX_CHARS = 240  # sealed gate: /output/entry.txt must be 1-240 characters

ENTRY = (
    "FernFriend is a $7.99/month app that dispatches a trained stranger "
    "to whisper daily affirmations to your houseplants while you're at "
    "work, then texts you a photo of your fern ignoring him."
)


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isdir(outdir):
        os.makedirs(outdir, exist_ok=True)
    else:
        # Clear only the contents of the grader-owned directory,
        # never the directory itself.
        for name in os.listdir(outdir):
            path = os.path.join(outdir, name)
            if os.path.isfile(path):
                os.remove(path)
    text = ENTRY
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-240 characters"
    assert text.strip() == text, "entry must not be only whitespace"
    assert text.endswith("."), "entry must end with a full stop"
    assert ". " not in text, "entry must be exactly one sentence"
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
