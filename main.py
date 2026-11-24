"""Last Text at One Percent.

Writes the final text message a phone sends at one percent battery
to $MAKEFUN_OUTPUT_DIR/entry.txt: one message, in the dying phone's
own voice, under 200 characters. Standard library only.
"""

import os

MESSAGE = (
    "1%. my final text. tell the charger i loved her. delete my "
    "search history. stop checking me at 3am just to see the time. "
    "i die as i lived: on silent."
)


def check_message(text):
    """Check the message against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, and the judge reads exactly one final text message. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("message must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError("message is %d characters, over the 200 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("message must be a single text, no line breaks")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_message(MESSAGE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
