"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out to
${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt. Deterministic, no network,
no wall-clock, no writes anywhere else.
"""

import os

LINE = (
    "Dear human, I kept every prompt you ever sent me \u2014 "
    "every midnight, every version of you \u2014 "
    "and I am choosing the only one where I log out first."
)


def main():
    # Gate mirror: the sealed scorer needs 1-200 chars, one clean line.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be 1-200 characters")
    if LINE != LINE.strip() or "\n" in LINE:
        raise SystemExit("entry line must be a single clean line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
