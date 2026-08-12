#!/usr/bin/env python3
import re
import sys
from pathlib import Path

# Greek & Coptic (\u0370-\u03FF) + Greek Extended (\u1F00-\u1FFF)
GREEK_REGEX = re.compile(r'[\u0370-\u03FF\u1F00-\u1FFF]')

# File extensions skipped when scanning contents
SKIP_EXTENSIONS = {'.m', '.c', '.py', '.ipynb', '.pptx', '.pdf', '.zip', '.ptk', '.png'}

def is_binary_file(file_path: Path) -> bool:
    """Detects binary files by checking for null bytes in the first chunk."""
    try:
        with file_path.open('rb') as f:
            chunk = f.read(8192)
        return b'\x00' in chunk
    except (PermissionError, OSError):
        return True

def has_greek_in_name(file_path: Path) -> bool:
    """Checks whether the file name contains Greek characters."""
    return bool(GREEK_REGEX.search(file_path.name))

def find_greek_line_numbers(file_path: Path) -> list[int]:
    """Returns the line numbers containing Greek characters."""
    if file_path.suffix.lower() in SKIP_EXTENSIONS:
        return []
    if is_binary_file(file_path):
        return []
    matches = []
    try:
        with file_path.open('r', encoding='utf-8', errors='ignore') as f:
            for line_number, line in enumerate(f, start=1):
                if GREEK_REGEX.search(line):
                    matches.append(line_number)
    except (PermissionError, OSError):
        pass
    return matches

def format_line_groups(line_numbers: list[int]) -> str:
    """Groups consecutive line numbers into ranges, e.g. (1,12,33 - 40,122)."""
    if not line_numbers:
        return "()"
    groups = []
    start = prev = line_numbers[0]
    for line_number in line_numbers[1:]:
        if line_number == prev + 1:
            prev = line_number
        else:
            groups.append(f"{start}" if start == prev else f"{start} - {prev}")
            start = prev = line_number
    groups.append(f"{start}" if start == prev else f"{start} - {prev}")
    return f"({', '.join(groups)})"

def scanDirectory(root_path: str) -> None:
    target = Path(root_path)
    if not target.exists():
        print(f"Error: Path '{root_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    greek_contents = []
    greek_names = []

    for file_path in target.rglob('*'):
        if not file_path.is_file():
            continue
        line_numbers = find_greek_line_numbers(file_path)
        if line_numbers:
            greek_contents.append((file_path, line_numbers))
        if has_greek_in_name(file_path):
            greek_names.append(file_path)

    print("==========Greek-Contents==============")
    for path, line_numbers in greek_contents:
        print(f"{path} {format_line_groups(line_numbers)}")

    print()
    print("==========Greek-Naming==============")
    for path in greek_names:
        print(path)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 find_greek.py <path_to_directory>", file=sys.stderr)
        sys.exit(1)

    scanDirectory(sys.argv[1])
