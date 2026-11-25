"""Make the AI Judge Laugh -- office-life joke entry.

Writes one original single-line joke about office life to the
output file given by $MAKEFUN_OUTPUT_DIR (or /output/entry.txt).
Pure Python standard library only.
"""

import os

MAX_CHARS = 200

JOKE = (
    "We replaced our weekly status meeting with a doc nobody reads, "
    "so now we meet to discuss why nobody reads the doc."
)


def main():
    joke = JOKE.strip()

    # Validate before writing: single line, 1-200 characters, non-empty.
    if not joke:
        raise SystemExit("error: joke is empty")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("error: joke must be a single line")
    if not 1 <= len(joke) <= MAX_CHARS:
        raise SystemExit(
            "error: joke must be 1-%d characters, got %d"
            % (MAX_CHARS, len(joke))
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    os.chmod(out_path, 0o644)

    # Verify the file on disk is exactly the validated joke.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != joke:
            raise SystemExit("error: written entry does not match joke")

    print(joke)
    print("chars: %d" % len(joke))


if __name__ == "__main__":
    main()
