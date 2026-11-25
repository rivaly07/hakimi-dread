from pathlib import Path
import os

ENTRY = "Approving. Small diff, green build, and the last outage started exactly like this. Ship it before I remember why we stopped."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
