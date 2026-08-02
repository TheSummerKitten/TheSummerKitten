#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from opencc import OpenCC


DEFAULT_POST_ROOT = Path("source/_posts")
DEFAULT_EXTENSIONS = {".md", ".markdown"}


def iter_markdown_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        yield root
        return

    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in DEFAULT_EXTENSIONS:
            yield path


def convert_file(src: Path, dst: Path, cc: OpenCC) -> None:
    text = src.read_text(encoding="utf-8")
    converted = cc.convert(text)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(converted, encoding="utf-8")


def build_output_path(src: Path, out_dir: Path | None, suffix: str | None, in_place: bool) -> Path:
    if in_place:
        return src

    if out_dir is None:
        out_dir = src.parent

    if suffix:
        return out_dir / f"{src.stem}{suffix}{src.suffix}"

    try:
        relative = src.relative_to(DEFAULT_POST_ROOT)
        return out_dir / relative
    except ValueError:
        return out_dir / src.name


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert Hexo Markdown posts from Traditional Chinese to Simplified Chinese with OpenCC."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=str(DEFAULT_POST_ROOT),
        help="A markdown file or a directory. Defaults to source/_posts.",
    )
    parser.add_argument(
        "-c",
        "--config",
        default="t2s",
        help="OpenCC config name, such as t2s, tw2s, hk2s, s2t. Defaults to t2s.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default=None,
        help="Directory for converted files. Defaults to each source file's directory.",
    )
    parser.add_argument(
        "--suffix",
        default="-简体",
        help="Suffix for output files when not using --in-place. Use empty string to keep the same name.",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite the original file instead of writing a copy.",
    )
    args = parser.parse_args()

    root = Path(args.path)
    if not root.exists():
        raise SystemExit(f"Path not found: {root}")

    out_dir = Path(args.output_dir) if args.output_dir else None
    suffix = args.suffix
    if suffix == "":
        suffix = None

    cc = OpenCC(args.config)
    files = list(iter_markdown_files(root))
    if not files:
        print("No markdown files found.")
        return 0

    for src in files:
        dst = build_output_path(src, out_dir, suffix, args.in_place)
        convert_file(src, dst, cc)
        print(f"{src} -> {dst}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
