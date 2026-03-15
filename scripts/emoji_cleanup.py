import os
import re

def removeEmojisFromText(text: str) -> str:
    """
    Removes Unicode emojis and symbols from a given string.

    Args:
        text (str): The input string containing potential emojis.

    Returns:
        str: The cleaned string without emojis.
    """
    # Pattern covers a wide range of Unicode emojis and symbols
    emoji_pattern = re.compile(
    "["
    "\U0001f300-\U0001f64f"  # Emoticons & Misc symbols
    "\U0001f680-\U0001f6ff"  # Transport & Map
    "\U0001f1e6-\U0001f1ff"  # Regional Indicator Symbols (Flags)
    "\U00002700-\U000027bf"  # Dingbats
    "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs (Food, Animals, etc.)
    "\U0001fa70-\U0001faff"  # Symbols and Pictographs Extended-A (Objects, Faces)
    "\u2600-\u26ff"          # Miscellaneous Symbols
    "\u2700-\u27bf"          # Dingbats (Duplicate block for BMP)
    "\u231a-\u231b"          # Watch/Hourglass
    "\u23e9-\u23ec"          # Fast-forward/Rewind
    "\u23f0-\u23f3"          # Alarm clocks
    "\u25fd-\u25fe"          # Geometric shapes
    "\U0001f004"            # Mahjong Tile Red Dragon
    "\U0001f0cf"            # Joker
    "\U0001f300-\U0001f5ff"  # Misc Symbols and Pictographs
    "\u203c"                # Double exclamation
    "\u2049"                # Exclamation interrogation
    "\u2139"                # Information
    "\u2194-\u2199"          # Arrows
    "\u21a9-\u21aa"          # Arrows
    "\u2328"                # Keyboard
    "\u2b05-\u2b07"          # Arrows
    "\u2b1b-\u2b1c"          # Squares
    "\u2b50"                # Star
    "\u2b55"                # Circle
    "\u3030"                # Wavy dash
    "\u303d"                # Part alternation mark
    "\u3297"                # Congratulation sign
    "\u3299"                # Secret sign
    "]+", flags=re.UNICODE
    )
    
    cleaned_text = emoji_pattern.sub('', text)
    
    # Target combined emojis like number boxes (digit + variation selector + keycap)
    cleaned_text = re.sub(r'[0-9]\ufe0f?\u20e3', '', cleaned_text)
    
    return cleaned_text

def processProjectFiles(root_dir: str):
    """
    Recursively traverses the project to remove emojis from non-HTML files.

    Args:
        root_dir (str): The starting directory for the search.
    """
    # Supported file extensions for cleaning (per user's preference to keep HTML)
    target_extensions = ('.md', '.py', '.c', '.cpp', '.h', '.hpp', '.sh', '.txt')
    
    ignore_dirs = {'.git', '.obsidian', '.vscode', 'node_modules'}

    for root, dirs, files in os.walk(root_dir):
        # Exclude hidden or dependency directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for file_name in files:
            if file_name.lower().endswith(target_extensions):
                file_path = os.path.join(root, file_name)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        original_content = f.read()
                    
                    new_content = removeEmojisFromText(original_content)
                    
                    if new_content != original_content:
                        print(f"Cleaning emojis from: {file_path}")
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                            
                except (UnicodeDecodeError, PermissionError):
                    # Silently skip files that cannot be processed as UTF-8 text
                    continue

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"Starting emoji cleanup in: {project_root}")
    processProjectFiles(project_root)
    print("Cleanup complete.")
