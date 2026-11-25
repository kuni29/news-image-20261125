"""Deliver the finished front page for 25 November 2026.

The artwork already exists as a file: entry.png, a 1024-by-1024
screenshot of the hand-built page, smaller than one mebibyte. This
script only ferries those bytes to the folder the grader reads, after
proving the file is a real PNG or JPEG and not oversized. Nothing is
drawn, downloaded, or remembered here, so every run hands over
identical bytes.
"""

import os as _os
import sys as _sys
from pathlib import Path as _Path

ENTRY_FILE = "entry.png"
SIZE_CAP = 1 << 20
KNOWN_HEADS = (
    bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
    bytes([0xFF, 0xD8, 0xFF]),
)


def _read_entry() -> bytes:
    base = _Path(__file__).resolve().parent
    candidate = base / ENTRY_FILE
    try:
        payload = candidate.read_bytes()
    except OSError as problem:
        print(f"entry file could not be opened: {problem}", file=_sys.stderr)
        _sys.exit(1)
    return payload


def _inspect(payload: bytes) -> None:
    looks_right = payload.startswith(KNOWN_HEADS)
    if not looks_right:
        print("entry file does not begin like a PNG or JPEG", file=_sys.stderr)
        _sys.exit(1)
    if len(payload) > SIZE_CAP:
        print(f"entry file is {len(payload)} bytes, past the 1 MiB ceiling", file=_sys.stderr)
        _sys.exit(1)


def _hand_over(payload: bytes) -> None:
    folder = _Path(_os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / ENTRY_FILE
    destination.write_bytes(payload)
    written = destination.stat().st_size
    if written != len(payload):
        print("entry file was only partly copied", file=_sys.stderr)
        _sys.exit(1)
    print(f"handed over {destination} ({len(payload)} bytes)")


def _run() -> None:
    payload = _read_entry()
    _inspect(payload)
    _hand_over(payload)


if __name__ == "__main__":
    _run()
