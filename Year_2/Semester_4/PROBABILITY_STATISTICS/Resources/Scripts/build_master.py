#!/usr/bin/env python3
"""Assembles the master Probability & Statistics notes file from consolidated phase files.

Reads all markdown files from Resources/Phases/, extracts their table of contents
entries, builds a master table of contents, and concatenates all phase content
into a single comprehensive study reference document.
"""

import os
import re
import sys
from datetime import datetime


def getPhaseFiles(phases_dir: str) -> list:
    """Collects and sorts phase markdown files from the Phases directory.

    Sorts files by extracting a leading phase number from the filename
    (e.g., "Phase_1_..." -> 1, "Phase_5B_..." -> 5.5).

    Args:
        phases_dir (str): Path to the directory containing consolidated phase files.

    Returns:
        list: Sorted list of full paths to phase markdown files.
    """
    if not os.path.isdir(phases_dir):
        print(f"Error: Phases directory not found: {phases_dir}")
        sys.exit(1)

    md_files = []
    for f in os.listdir(phases_dir):
        if f.endswith(".md"):
            md_files.append(os.path.join(phases_dir, f))

    # Sorts by phase number extracted from filename; Phase_5B sorts after Phase_5.
    def sortKey(path: str) -> float:
        filename = os.path.basename(path)
        match = re.search(r'Phase_(\d+)([A-Z]?)', filename)
        if match:
            num = int(match.group(1))
            suffix = match.group(2)
            # Appends 0.5 for letter suffixes so Phase_5B sorts after Phase_5.
            if suffix:
                return num + (ord(suffix) - ord('A') + 1) * 0.1
            return float(num)
        return 999.0

    md_files.sort(key=sortKey)
    return md_files


def extractTocEntries(content: str) -> list:
    """Extracts table of contents entries from a phase file's content.

    Parses `## Section N.X:` headings to build TOC entries for the master file.

    Args:
        content (str): The full markdown content of a phase file.

    Returns:
        list: List of (section_title, anchor) tuples for the master TOC.
    """
    entries = []
    for match in re.finditer(r'^##\s+(.+)$', content, re.MULTILINE):
        title = match.group(1).strip()
        # Skips the phase's own "Table of Contents" and "Summary" headings.
        if title.lower() in ("table of contents", "phase summary") or title.startswith("Phase "):
            continue
        # Generates a GitHub-style anchor from the heading text.
        anchor = re.sub(r'[^\w\s-]', '', title.lower())
        anchor = re.sub(r'\s+', '-', anchor.strip())
        entries.append((title, anchor))
    return entries


def extractPhaseTitle(content: str) -> str:
    """Extracts the top-level phase title from markdown content.

    Args:
        content (str): The full markdown content of a phase file.

    Returns:
        str: The phase title (first `#` heading), or "Untitled Phase" if not found.
    """
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Untitled Phase"


def buildMaster(phase_files: list, output_path: str) -> None:
    """Assembles all phase files into a single master compilation document.

    Writes a master file with a header, a full table of contents organized by
    phase, and the concatenated content of all phase files separated by
    horizontal rules.

    Args:
        phase_files (list): Sorted list of phase file paths to include.
        output_path (str): Destination path for the master markdown file.

    Raises:
        IOError: If any source file cannot be read or the output cannot be written.
    """
    phases = []

    for file_path in phase_files:
        with open(file_path, "r", encoding="utf-8") as infile:
            content = infile.read()
        title = extractPhaseTitle(content)
        toc_entries = extractTocEntries(content)
        phases.append({
            "path": file_path,
            "title": title,
            "content": content,
            "toc_entries": toc_entries
        })

    with open(output_path, "w", encoding="utf-8") as outfile:
        # Writes the document header with generation timestamp.
        outfile.write("# Probability and Statistics - Master Notes\n\n")
        outfile.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*\n\n")
        outfile.write("---\n\n")

        # Writes the master table of contents.
        outfile.write("## Master Table of Contents\n\n")
        for i, phase in enumerate(phases, 1):
            outfile.write(f"### {phase['title']}\n\n")
            for title, anchor in phase["toc_entries"]:
                outfile.write(f"- [{title}](#{anchor})\n")
            outfile.write("\n")
        outfile.write("---\n\n")

        # Appends each phase's full content with a source marker.
        for i, phase in enumerate(phases, 1):
            source_name = os.path.basename(phase["path"])
            outfile.write(f"<!-- Source: Phases/{source_name} -->\n\n")
            outfile.write(phase["content"])
            if not phase["content"].endswith("\n"):
                outfile.write("\n")
            outfile.write("\n---\n\n")

    print(f"Successfully created: {output_path}")
    print(f"  Phases included: {len(phases)}")
    total_lines = sum(p["content"].count("\n") + 1 for p in phases)
    print(f"  Total content lines: {total_lines}")


def main() -> None:
    """Entry point: locates the Phases directory and builds the master file.

    Determines paths relative to the script location and invokes the build.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Resolves paths relative to the script's location in Resources/Scripts/.
    resources_dir = os.path.dirname(base_dir)
    phases_dir = os.path.join(resources_dir, "Phases")
    output_file = os.path.join(resources_dir, "Probability_and_Statistics_Master.md")

    print(f"Scanning for phase files in: {phases_dir}")
    phase_files = getPhaseFiles(phases_dir)

    if not phase_files:
        print("Error: No phase files found in Resources/Phases/.")
        print("Run the consolidation process first to generate phase files.")
        sys.exit(1)

    print(f"Found {len(phase_files)} phase files:")
    for f in phase_files:
        print(f"  - {os.path.basename(f)}")
    print()

    print(f"Building master file: {output_file}")
    buildMaster(phase_files, output_file)


if __name__ == "__main__":
    main()