"""The Funniest One-Line Resignation Letter.

Writes the winning one-line resignation letter of a cron job to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.

The line is the tournament winner (5-0 head-to-head, see TOURNAMENT.md):
a cron job that even worked the leap second and is deleting itself from
the crontab. It is 99 characters, inside the competition's 1-140 gate.
"""

import os


LINE = (
    "I even worked the leap second, and you still forgot I exist. "
    "I am deleting myself from the crontab."
)


def main() -> None:
    # Enforce the competition gate: 1 to 140 characters, not only whitespace.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "entry violates the 140-char gate"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
