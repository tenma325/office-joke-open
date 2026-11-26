#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Laugh: the Office Joke Open.

The entry is a single office joke about the daily standup,
that fifteen-minute ritual where nine people stand in a
circle and read their Jira tickets aloud to each other. Seen
from the outside it resembles nothing so much as a support
group for features that will never ship: everyone shares,
everyone nods, and the feature learns to accept itself
exactly as it is: unfinished, in the backlog, at peace.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Our standup is just nine people reading their Jira tickets aloud "
    "in a circle, like a support group for features that will never ship."
)

# The joke works because every attendee recognizes the circle:
# same tickets, same nodding, same feature, still at peace.
STANDUP_ATTENDEES = 9


def render_entry() -> str:
    """Return the joke exactly as it will be told at standup."""
    return ENTRY_TEXT


def lands_in_one_line(text: str) -> bool:
    """Confirm the joke stays one line and under the cap."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert lands_in_one_line(text), "the joke must fit in one line"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
