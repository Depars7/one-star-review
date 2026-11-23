import os

PARTS = (
    "Gravity, one star: drops my phone face-down, ",
    "pulls my posture and my face steadily south, ",
    "and still charges full force on every stair.",
)


def entry_line() -> str:
    return "".join(PARTS)


def main() -> None:
    text = entry_line()
    assert 1 <= len(text) <= 160, f"entry must be 1-160 chars, got {len(text)}"
    assert text.strip() == text and text.strip(), "entry must not be blank"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert "!" not in text, "deadpan: no exclamation marks"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
