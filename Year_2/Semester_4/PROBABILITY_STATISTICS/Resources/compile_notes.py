import os
import re
import argparse
import sys


def getSortKey(file_path: str) -> tuple:
    """
    Extracts phase and section numbers from the filename for sorting.

    Example: 'phase_1_2_measures.md' -> (1, 2)

    Args:
        file_path (str): Full or relative path to the markdown file.

    Returns:
        tuple: (phase_number, section_number). Returns (999, 999) for
               files that do not match the expected pattern, placing them
               at the end of the sorted list.
    """
    filename = os.path.basename(file_path)
    match = re.search(r'phase_(\d+)_(\d+)', filename)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    return (999, 999)


def collectPhaseFiles(resources_dir: str) -> list:
    """
    Walks the Resources directory and collects all phase markdown files.

    Only includes files matching the 'phase_X_Y_*.md' pattern. Files are
    sorted by their phase and section numbers.

    Args:
        resources_dir (str): Path to the Resources directory containing
                             Phase_* subdirectories.

    Returns:
        list: Sorted list of full paths to phase markdown files.
    """
    md_files = []
    for root, dirs, files in os.walk(resources_dir):
        for file in files:
            if file.endswith('.md') and re.search(r'phase_\d+_\d+', file):
                md_files.append(os.path.join(root, file))

    md_files.sort(key=getSortKey)
    return md_files


def mergeFiles(phase_files: list, output_path: str) -> None:
    """
    Merges the contents of phase markdown files into a single compilation file.

    Each file's content is prefixed with an HTML source comment and separated
    by a horizontal rule. The output file is written with UTF-8 encoding.

    Args:
        phase_files (list): Sorted list of file paths to merge.
        output_path (str): Destination path for the compiled markdown file.

    Raises:
        IOError: If any source file cannot be read or the output file cannot
                 be written.
    """
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write("# Statistics Notes - Full Compilation\n\n")
        outfile.write("Generated from individual lecture phases.\n\n---\n\n")

        for file_path in phase_files:
            relative_path = os.path.relpath(file_path, os.path.dirname(output_path))
            print(f"  Appending: {relative_path}")

            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()

            outfile.write(f"<!-- Source: {relative_path} -->\n")
            outfile.write(content)
            outfile.write("\n\n---\n\n")


def compileNotes(lectures_dir: str = None, resources_dir: str = None) -> None:
    """
    Compiles phase markdown files from Resources into a single notes file.

    The script locates all phase markdown files in the Resources directory's
    Phase_* subdirectories, sorts them numerically, and merges them into a
    single markdown file located in the Lectures directory.

    Args:
        lectures_dir (str, optional): Path to the Lectures directory. Defaults
                                      to '../Lectures' relative to the script.
        resources_dir (str, optional): Path to the Resources directory. Defaults
                                       to the directory containing this script.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if resources_dir is None:
        resources_dir = base_dir
    if lectures_dir is None:
        lectures_dir = os.path.join(base_dir, '..', 'Lectures')

    # Resolve to absolute paths
    resources_dir = os.path.abspath(resources_dir)
    lectures_dir = os.path.abspath(lectures_dir)
    output_file = os.path.join(lectures_dir, 'StatisticsNotes.md')

    # Validate directories
    if not os.path.isdir(resources_dir):
        print(f"Error: Resources directory not found: {resources_dir}")
        sys.exit(1)
    if not os.path.isdir(lectures_dir):
        print(f"Error: Lectures directory not found: {lectures_dir}")
        sys.exit(1)

    print(f"Scanning for phase files in: {resources_dir}")
    phase_files = collectPhaseFiles(resources_dir)

    if not phase_files:
        print("Warning: No phase files found. Check that the Resources "
              "directory contains Phase_*_* subdirectories with .md files.")
        sys.exit(0)

    print(f"Found {len(phase_files)} phase files to merge.")
    print(f"Output file: {output_file}")
    print()

    try:
        mergeFiles(phase_files, output_file)
        print(f"\nSuccessfully created: {output_file}")
    except IOError as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


def main() -> None:
    """
    Parses command-line arguments and invokes the compilation process.
    """
    parser = argparse.ArgumentParser(
        description="Compile phase markdown files into a single Statistics Notes document."
    )
    parser.add_argument(
        '--resources-dir',
        type=str,
        default=None,
        help="Path to the Resources directory (default: script's own directory)."
    )
    parser.add_argument(
        '--lectures-dir',
        type=str,
        default=None,
        help="Path to the Lectures directory (default: ../Lectures relative to script)."
    )

    args = parser.parse_args()
    compileNotes(
        lectures_dir=args.lectures_dir,
        resources_dir=args.resources_dir
    )


if __name__ == "__main__":
    main()