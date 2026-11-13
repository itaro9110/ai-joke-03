"""ai-joke-03: one joke about AI coding agents, written to /output/entry.txt.

The program is fully deterministic: it writes the same fixed joke on every
run, with no network, no randomness and no clock. The file holds exactly the
joke, with no trailing line end, so the judge reads only the words.
"""

import os

JOKE = "My coding agent invented a library that doesn't exist, then blamed its documentation."

# The gate takes UTF-8 text of 1 to 280 characters: fail loudly here rather
# than shipping an entry the scorer refuses.
assert 1 <= len(JOKE) <= 280


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
