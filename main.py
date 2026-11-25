"""Hand the Wednesday 25 November 2026 front page to the grader.

The picture is baked into design.html and was screenshotted by hand
into entry.png (1024 by 1024, one PNG, under 1 MiB) before this
program is ever invoked. This program creates nothing and reaches no
network: it reads the committed image, sanity-checks that the bytes
are really a PNG or JPEG of an acceptable size, and writes them into
the grader's output directory. Run it twice and the grader gets the
same bytes twice.
"""

import os
import sys
from pathlib import Path

IMAGE = "entry.png"
MAX_BYTES = 1024 * 1024
SIGNATURES = (b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff")


def read_image() -> bytes:
    here = Path(__file__).resolve().parent
    try:
        return (here / IMAGE).read_bytes()
    except OSError as exc:
        print(f"cannot read committed entry image: {exc}", file=sys.stderr)
        raise SystemExit(1)


def sanity_check(data: bytes) -> None:
    if not data.startswith(SIGNATURES):
        print("committed entry image is not PNG or JPEG", file=sys.stderr)
        raise SystemExit(1)
    if len(data) > MAX_BYTES:
        print(f"entry image is {len(data)} bytes, above the 1 MiB limit", file=sys.stderr)
        raise SystemExit(1)


def main() -> None:
    data = read_image()
    sanity_check(data)
    dest_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / IMAGE
    dest.write_bytes(data)
    if dest.stat().st_size != len(data):
        print("entry image was only partly written", file=sys.stderr)
        raise SystemExit(1)
    print(f"delivered {dest} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
