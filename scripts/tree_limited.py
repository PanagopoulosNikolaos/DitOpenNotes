#!/usr/bin/env python3
"""
Generates a recursive directory tree with a configurable maximum number of files
displayed per directory. Respects .gitignore patterns to skip ignored directories.
"""

import fnmatch
import os
import sys
from pathlib import Path


def loadGitignorePatterns(root: Path) -> list[str]:
    """
    Reads .gitignore patterns from the root directory.

    Args:
        root (Path): The project root directory.

    Returns:
        list[str]: A list of gitignore patterns relevant to directories.
    """
    gitignore_path = root / ".gitignore"
    if not gitignore_path.exists():
        return []

    patterns: list[str] = []
    try:
        with open(gitignore_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                # Skip blank lines and comments
                if not stripped or stripped.startswith("#"):
                    continue
                # Collapse leading ./ (equivalent to no prefix)
                if stripped.startswith("./"):
                    stripped = stripped[2:]
                patterns.append(stripped)
    except OSError:
        pass

    return patterns


def isIgnored(relative_path: str, patterns: list[str]) -> bool:
    """
    Checks whether a relative path matches any of the gitignore patterns.

    Implements basic gitignore semantics:
    - A trailing slash indicates a directory pattern.
    - Patterns without a slash match the basename of any path.
    - Patterns with a slash match from the root of the ignored tree.
    - Leading `!` negates a pattern (not implemented here since we only check
      directories that would be included).

    Args:
        relative_path (str): The path relative to the repo root, with forward
            slashes.
        patterns (list[str]): Parsed gitignore patterns.

    Returns:
        bool: True if the path should be ignored.
    """
    for pattern in patterns:
        # Skip negated patterns for simplicity (only additive ignore)
        if pattern.startswith("!"):
            continue

        # Normalise: strip trailing slash for matching
        p = pattern.rstrip("/")

        # Determine if pattern is "anchored" (contains a slash besides trailing)
        anchored = "/" in p

        if anchored:
            # Match from root of relative_path
            if fnmatch.fnmatch(relative_path, p) or relative_path.startswith(
                p + "/"
            ):
                return True
        else:
            # Match against any path component
            parts = relative_path.split("/")
            if any(fnmatch.fnmatch(part, p) for part in parts):
                return True

    return False


def treeLimited(
    root: str,
    max_files: int = 2,
    prefix: str = "",
    _is_root: bool = True,
    _patterns: list[str] | None = None,
) -> None:
    """
    Recursively prints a directory tree, showing at most `max_files` file
    entries per directory. Directories matching gitignore patterns are skipped.

    Args:
        root (str): Path to the directory to display.
        max_files (int): Maximum number of file entries shown per directory.
            Defaults to 2.
        prefix (str): Indentation string prepended to each line during
            recursion. Defaults to "".
        _is_root (bool): Internal flag indicating the top-level invocation.
            Defaults to True.
        _patterns (list[str] | None): Parsed gitignore patterns, loaded
            automatically on first call. Defaults to None.
    """
    root_path = Path(root).resolve()

    # Load gitignore patterns on first invocation
    if _patterns is None:
        _patterns = loadGitignorePatterns(root_path)

    if _is_root:
        print(root_path)

    try:
        entries = sorted(
            root_path.iterdir(),
            key=lambda e: (e.is_file(), e.name.lower()),
        )
    except PermissionError:
        print(f"{prefix}└── [Permission Denied]")
        return

    dirs: list[Path] = []
    files: list[Path] = []

    for e in entries:
        # Always skip .git directory
        if e.name == ".git":
            continue

        # Build relative path from the repository root
        try:
            rel = str(e.relative_to(root_path))
        except ValueError:
            rel = e.name

        # If the entry matches any gitignore pattern, skip it entirely
        if isIgnored(rel, _patterns):
            continue

        if e.is_dir():
            dirs.append(e)
        elif e.is_file():
            files.append(e)

    shown_files = files[:max_files]
    hidden_count = len(files) - max_files

    all_shown = shown_files + dirs

    for i, entry in enumerate(all_shown):
        is_last = (i == len(all_shown) - 1) and hidden_count <= 0
        connector = "└── " if is_last else "├── "
        new_prefix = "    " if is_last else "│   "

        print(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():
            treeLimited(
                str(entry),
                max_files,
                prefix + new_prefix,
                _is_root=False,
                _patterns=_patterns,
            )

    if hidden_count > 0:
        connector = "└── " if not dirs else "├── "
        print(f"{prefix}{connector}[+{hidden_count} more file(s)]")


def main() -> None:
    """
    Parses command-line arguments and invokes the limited tree display.
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Display a directory tree with a configurable maximum "
        "number of files per directory. Skips .gitignore'd paths."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Root directory to display (default: current directory)",
    )
    parser.add_argument(
        "-n",
        "--max-files",
        type=int,
        default=2,
        help="Maximum number of files to show per directory (default: 2)",
    )

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    treeLimited(args.directory, args.max_files)


if __name__ == "__main__":
    main()