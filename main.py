#!/usr/bin/env python3
"""Write one sentence explaining the modern internet to a traveler from 1800.

Deterministic: no clock, no randomness, no network, no input. The same
sentence is written on every run, byte for byte.
"""
import os

ENTRY = ("It is one coffeehouse holding every newspaper and letter in the "
         "world, where you may ask anything and hear the world answer at once.")

def main():
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry length %d outside 1-200" % len(text))
    if not text.strip():
        raise SystemExit("entry is blank")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)

if __name__ == "__main__":
    main()
