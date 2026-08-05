#!/usr/bin/env python3
"""批次重新命名檔案的 CLI — 批次重新命名（預覽後執行）。"""
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser(description='批次重新命名檔案的 CLI')
    p.add_argument("dir", type=Path)
    p.add_argument("--prefix", default="file_")
    p.add_argument("--apply", action="store_true", help="真的改名；預設只預覽")
    args = p.parse_args()
    files = sorted([f for f in args.dir.iterdir() if f.is_file()])
    for i, f in enumerate(files, 1):
        new = f.with_name(f"{args.prefix}{i:03d}{f.suffix}")
        print(f"{f.name} -> {new.name}")
        if args.apply:
            f.rename(new)


if __name__ == "__main__":
    main()
