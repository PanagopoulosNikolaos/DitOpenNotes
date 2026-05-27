import os


def bundleFolder(folder_path: str) -> None:
    """Combines all markdown files in a folder into a single file.

    Args:
        folder_path (str): The path to the folder containing markdown files.

    Returns:
        (None): This function does not return any value.
    """
    if not os.path.isdir(folder_path):
        print(f"Directory {folder_path} not found. Skipping.")
        return

    folder_name = os.path.basename(os.path.normpath(folder_path))
    output_file_name = f"full_{folder_name}.md"
    output_file_path = os.path.join(folder_path, output_file_name)

    # Scans the target directory contents to identify potential markdown candidates.
    all_files = os.listdir(folder_path)

    # Excludes the compilation file itself to prevent self-appending loops.
    md_files = [f for f in all_files if f.endswith(".md") and f != output_file_name]

    # Sorts the files alphabetically to match lexicographical ls ordering.
    md_files.sort()

    if not md_files:
        print(f"No markdown files to bundle in {folder_name}.")
        return

    print(f"Bundling {len(md_files)} files in {folder_name} into {output_file_name}...")

    bundled_contents = []
    for file_name in md_files:
        file_path = os.path.join(folder_path, file_name)
        # Reads with UTF-8 encoding to preserve special characters and mathematical notation.
        with open(file_path, "r", encoding="utf-8") as infile:
            content = infile.read()
            # Standardizes spacing between files to prevent formatting collisions.
            if not content.endswith("\n"):
                content += "\n"
            bundled_contents.append(content)

    # Writes the aggregated markdown to the destination file.
    with open(output_file_path, "w", encoding="utf-8") as outfile:
        # Joins files with double newlines for a clean layout and visual division.
        outfile.write("\n\n".join(bundled_contents))

    print(f"Successfully created: {output_file_path}")


def main() -> None:
    """Orchestrates the bundling process across all statistical phase directories.

    Returns:
        (None): This function does not return any value.
    """
    # Defines the directories in the sequence of phases for organization.
    target_folders = [
        "Phase_1_Descriptive_Statistics",
        "Phase_2_Probability_Theory",
        "Phase_3_Conditional_Probability_Independence",
        "Phase_4_Discrete_Random_Variables",
        "Phase_5_Continuous_Random_Variables_Distributions",
        "Phase_5B_Multivariate_Random_Variables",
        "Phase_6_Inferential_Statistics",
        "Phase_7_R_Programming_Commands"
    ]

    base_dir = os.path.dirname(os.path.abspath(__file__))

    for folder in target_folders:
        folder_path = os.path.join(base_dir, folder)
        bundleFolder(folder_path)


if __name__ == "__main__":
    main()
