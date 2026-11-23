#!/usr/bin/env python3
"""Real-Life Patch Notes entry: writes one patch-note line to /output/entry.txt."""

import os

VERSION = "v2.3.1"
BUG = "the phone vibrated in a pocket containing no phone"


def patch_note():
    """Build the single changelog line from its version and bug parts."""
    return f"{VERSION}: fixed a bug where {BUG}."


def write_entry(path="/output/entry.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(patch_note())


def main():
    write_entry()


if __name__ == "__main__":
    main()
