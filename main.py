import os
import sys

ENTRY = "On rainy evenings my grandmother ladled rice into my chipped blue bowl while the tin roof drummed above us, and I never once asked why she always served herself last."
MAX_CHARS = 280


def main():
    text = ENTRY
    if not text or not text.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print("error: entry is %d chars, max %d" % (len(text), MAX_CHARS), file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("error: entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %d chars to %s/entry.txt" % (len(text), out_dir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
