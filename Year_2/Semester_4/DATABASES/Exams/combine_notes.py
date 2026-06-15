import glob
import os

def combineMarkdownFiles(output_path: str) -> None:
    """Combines Markdown notes numbered 1 to 7 into a single file.

    Iterates through the numbers 1 to 7, locates the corresponding markdown
    file in the current directory, and appends its contents to the output file.
    Prepend a header indicating the origin file name before each section.

    Args:
        output_path (str): The path to the output merged markdown file.

    Returns:
        None: Does not return any value.
    """
    # Opens the file in write mode to initialize a clean, empty output document.
    with open(output_path, "w", encoding="utf-8") as out_file:
        for i in range(1, 9):
            # Locates files prefix-matched with the current index to ensure ordered processing.
            pattern = f"Practice_Exam_{i}_*.md"
            matched_files = glob.glob(pattern)

            if not matched_files:
                continue

            # Selects the first matched file under the assumption of unique indexing.
            file_path = matched_files[0]
            file_name = os.path.basename(file_path)

            # Appends the formatted file name header to demarcate document sections.
            out_file.write(f"---\n# {file_name}\n---\n\n")
            print("Appended " + file_name + " to " + output_path)

            # Transfers the entire source document content into the merged destination.
            with open(file_path, "r", encoding="utf-8") as in_file:
                content = in_file.read()
                out_file.write(content)
                # Appends trailing newlines to prevent formatting overlap between topics.
                if not content.endswith("\n"):
                    out_file.write("\n")
                out_file.write("\n")

if __name__ == "__main__":
    # Establishes the default destination file name for the combined markdown results.
    combined_output = "all_exams.md"
    combineMarkdownFiles(combined_output)
