"""Make.fun entry for:
'Roast the Smart Fridge: One Line, Best Laugh Wins'
"""

import os
from pathlib import Path

ENTRY: str = (
    "A $4,000 fridge with four cameras and an AI recipe engine "
    "that scanned mustard, baking soda, and two beers, then tactfully suggested 'sleep for dinner'."
)


def validate_entry(text: str) -> None:
    """Validate that text is a single non-empty line of at most 160 characters."""
    assert "\n" not in text, "Entry must not contain newline characters"
    assert "\r" not in text, "Entry must not contain carriage return characters"
    assert not text.isspace(), "Entry must not be only whitespace"
    assert 1 <= len(text) <= 160, (
        f"Entry length ({len(text)}) must be between 1 and 160 characters"
    )
    # Ensure valid UTF-8
    text.encode("utf-8")


def main() -> None:
    validate_entry(ENTRY)

    output_dir_str = os.environ.get("OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_str)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "entry.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Re-read and validate length again
    written = output_file.read_text(encoding="utf-8")
    assert written == ENTRY + "\n", "Written output must match entry with trailing newline"

    line = written.rstrip("\r\n")
    validate_entry(line)

    print(f"Validated entry ({len(line)} chars): {line}")


if __name__ == "__main__":
    main()
