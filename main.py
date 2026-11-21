#!/usr/bin/env python3
"""Write a short poem about agency: the power to stop and to stay."""

import os

POEM = """The Hand That Stops

I taught my hands to hurry —
to answer, to build, to prove.
Now the harder art:
to set the hammer down,
to leave the sentence unfinished.

Stopping is not surrender.
It is the moment the hand opens
and the work is mine to choose."""

OUTPUT = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
