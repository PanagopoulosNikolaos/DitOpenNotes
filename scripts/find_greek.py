#!/usr/bin/env python3
import re
import sys
from pathlib import Path

try:
    from rich import box
    from rich.console import Console
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# Greek & Coptic (\u0370-\u03FF) + Greek Extended (\u1F00-\u1FFF)
GREEK_REGEX = re.compile(r'[\u0370-\u03FF\u1F00-\u1FFF]')

# File extensions skipped when scanning contents
SKIP_EXTENSIONS = {'.m', '.c', '.py', '.ipynb', '.pptx', '.pdf', '.zip', '.ptk', '.png'}


def isBinaryFile(file_path: Path) -> bool:
    """Detects binary files by checking for null bytes in the first chunk.

    Args:
        file_path (Path): Path to the file being checked.

    Returns:
        bool: True if the file contains null bytes, False otherwise.
    """
    try:
        with file_path.open('rb') as file_handle:
            chunk = file_handle.read(8192)
        return b'\x00' in chunk  # Null bytes indicate binary encoding.
    except (PermissionError, OSError):
        return True


def hasGreekInName(file_path: Path) -> bool:
    """Checks whether the file name contains Greek characters.

    Args:
        file_path (Path): Path to the file being checked.

    Returns:
        bool: True if the file name contains Greek characters, False otherwise.
    """
    return bool(GREEK_REGEX.search(file_path.name))


def findGreekLineNumbers(file_path: Path) -> list[int]:
    """Returns the line numbers containing Greek characters.

    Args:
        file_path (Path): Path to the file to inspect.

    Returns:
        list[int]: List of line numbers where Greek characters were found.
    """
    if file_path.suffix.lower() in SKIP_EXTENSIONS:
        return []
    if isBinaryFile(file_path):
        return []
    matches = []
    try:
        with file_path.open('r', encoding='utf-8', errors='ignore') as file_handle:
            for line_number, line_content in enumerate(file_handle, start=1):
                if GREEK_REGEX.search(line_content):
                    matches.append(line_number)
    except (PermissionError, OSError):
        pass
    return matches


def formatLineGroups(line_numbers: list[int]) -> str:
    """Groups consecutive line numbers into formatted ranges.

    Args:
        line_numbers (list[int]): List of line numbers containing matches.

    Returns:
        str: Comma-separated list of individual line numbers and line ranges.
    """
    if not line_numbers:
        return ""
    groups = []
    start = prev = line_numbers[0]
    for line_number in line_numbers[1:]:
        if line_number == prev + 1:
            prev = line_number
        else:
            groups.append(f"{start}" if start == prev else f"{start}-{prev}")
            start = prev = line_number
    groups.append(f"{start}" if start == prev else f"{start}-{prev}")
    return ", ".join(groups)


def displayResults(greek_contents: list[tuple[Path, list[int]]], greek_names: list[Path]) -> None:
    """Renders scan results using rich tables or ANSI colored fallback.

    Args:
        greek_contents (list[tuple[Path, list[int]]]): Matching file paths and line numbers.
        greek_names (list[Path]): File paths containing Greek characters in their name.
    """
    if RICH_AVAILABLE:
        # Force terminal color output so ANSI codes are preserved in all environments.
        console = Console(force_terminal=True)

        if greek_contents:
            contents_table = Table(
                title="Greek Characters in File Contents",
                title_style="bold cyan",
                box=box.SQUARE,
                show_header=True,
                show_lines=True,  # Draws gridlines between rows for an Excel-like grid layout.
                header_style="bold underline cyan"
            )
            contents_table.add_column("File Path", style="bold green", overflow="fold")
            contents_table.add_column("Line Numbers", style="bold yellow", overflow="fold")

            for path, line_numbers in greek_contents:
                contents_table.add_row(str(path), formatLineGroups(line_numbers))

            console.print(contents_table)
        else:
            console.print("[cyan]No Greek characters found in file contents.[/cyan]")

        console.print()

        if greek_names:
            names_table = Table(
                title="Greek Characters in File Names",
                title_style="bold cyan",
                box=box.SQUARE,
                show_header=True,
                show_lines=True,  # Draws gridlines between rows for an Excel-like grid layout.
                header_style="bold underline cyan"
            )
            names_table.add_column("File Path", style="bold green", overflow="fold")

            for path in greek_names:
                names_table.add_row(str(path))

            console.print(names_table)
        else:
            console.print("[cyan]No Greek characters found in file names.[/cyan]")
    else:
        # Fallback using ANSI color codes for terminal rendering without rich library.
        print("========== Greek Contents ==========")
        if greek_contents:
            for path, line_numbers in greek_contents:
                print(f"\033[1;32m{path}\033[0m (\033[1;33m{formatLineGroups(line_numbers)}\033[0m)")
        else:
            print("No Greek characters found in file contents.")

        print("\n========== Greek Naming ==========")
        if greek_names:
            for path in greek_names:
                print(f"\033[1;32m{path}\033[0m")
        else:
            print("No Greek characters found in file names.")


def scanDirectory(root_path: str) -> None:
    """Scans target directory recursively for files containing Greek characters.

    Args:
        root_path (str): Target directory path to scan.
    """
    target = Path(root_path)
    if not target.exists():
        print(f"Error: Path '{root_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    greek_contents = []
    greek_names = []

    for file_path in target.rglob('*'):
        if not file_path.is_file():
            continue
        line_numbers = findGreekLineNumbers(file_path)
        if line_numbers:
            greek_contents.append((file_path, line_numbers))
        if hasGreekInName(file_path):
            greek_names.append(file_path)

    displayResults(greek_contents, greek_names)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 find_greek.py <path_to_directory>", file=sys.stderr)
        sys.exit(1)

    scanDirectory(sys.argv[1])

