"""make.fun ai-joke-03 entry: writes one fixed one-liner about AI coding
agents to <output>/entry.txt.

The output directory is $MAKEFUN_OUTPUT_DIR when set, else /output.
The joke is a constant: the program runs twice and must write identical
bytes, so there is no randomness, no clock and no input.
"""

import os

JOKE = "I asked my agent to fix a typo. It refactored nine files, and now the typo is spelled consistently across the codebase."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
