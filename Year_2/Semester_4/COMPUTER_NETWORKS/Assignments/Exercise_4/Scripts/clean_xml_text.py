import sys
import os
import string

class TextCleaner:
    """
    Provides methods to clean and normalize text extracted from XML files.

    Contains the following functions:
    - normalizeText: Converts text to a lowercase, alphanumeric-only format for comparison.
    - cleanText: Reads a file, removes boilerplate and duplicates, and saves the cleaned text.
    """

    def normalizeText(self, text: str) -> str:
        """
        Normalizes text for comparison by removing punctuation and whitespace.

        Args:
            text (str): The raw string to be normalized.

        Returns:
            str: A lowercase string containing only alphanumeric characters.
        """
        # Processes each character to filter out punctuation and spaces for consistent comparison.
        return "".join(char.lower() for char in text if char not in string.punctuation and not char.isspace())

    def cleanText(self, file_path: str) -> None:
        """
        Cleans up the text from a PowerPoint-extracted XML file.

        Args:
            file_path (str): The absolute or relative path to the target file.

        Returns:
            None: Modifies the file in-place.
        """
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Defines common PowerPoint boilerplate strings to be excluded from the final text.
        boilerplate = [
            "<number>",
            "Click to edit Master title style",
            "Click icon to add picture",
            "Click to edit Master text styles",
            "Second level",
            "Third level",
            "Fourth level",
            "Fifth level",
            "“",
            "”"
        ]

        cleaned_lines = []
        seen_normalized = set()

        for line in lines:
            original_line = line.strip()
            
            if not original_line:
                continue
                
            # Filters out non-content lines identified as PowerPoint interface instructions.
            if any(b in original_line for b in boilerplate):
                continue
                
            if original_line.isdigit():
                continue
            
            normalized = self.normalizeText(original_line)
            
            # Identifies unique content by comparing normalized versions to avoid redundant translations or repetitions.
            if normalized and normalized not in seen_normalized:
                cleaned_lines.append(original_line)
                seen_normalized.add(normalized)

        # Overwrites the original file with the filtered and de-duplicated content.
        with open(file_path, 'w', encoding='utf-8') as f:
            for line in cleaned_lines:
                f.write(line + '\n')

        print(f"Success: Cleaned '{file_path}'.")

if __name__ == "__main__":
    target_file = "File-Path-Here"
    cleaner = TextCleaner()
    cleaner.cleanText(target_file)
