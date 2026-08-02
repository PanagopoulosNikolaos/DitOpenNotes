#!/usr/bin/env python3
"""
Extracts the quiz_questions array from each quiz HTML file into an indexed JSON object.

The output JSON maps a section index (1-8) to the questions array scraped
from the corresponding HTML file. Files are processed in order: quiz_1
through quiz_7, then quiz_base_code.
"""

import json
import pathlib
import re

# Directory containing this script and the quiz HTML files.
QUIZ_DIR = pathlib.Path(__file__).resolve().parent

# Destination JSON file.
DATA_FILE = QUIZ_DIR / "data" / "questions.json"

# Ordered list of quiz files to scrape.
QUIZ_FILES = [
    "quiz_1_dikaio_sto_epakro.html",
    "quiz_2_to_diadiktyo.html",
    "quiz_3_domi_diktyo.html",
    "quiz_4_texnologies_prosvasis.html",
    "quiz_5_epikinoniaka_mesa.html",
    "quiz_6_diametagogi_dedomenon.html",
    "quiz_7_vasika_zitiimata.html",
    "quiz_base_code.html",
]

# Matches the start of the embedded questions array.
ARRAY_START_PATTERN = re.compile(r"const quiz_questions\s*=\s*\[")


def extractArrayText(html_text):
    """
    Extracts the raw text of the quiz_questions array from an HTML document.

    Args:
        html_text (str): The full HTML document text.

    Returns:
        str: The array body between the opening '[' and closing '];'.
    """
    start_match = ARRAY_START_PATTERN.search(html_text)
    if not start_match:
        raise ValueError("quiz_questions array not found in HTML")
    array_end = html_text.index("];", start_match.end())
    return html_text[start_match.end():array_end]


def jsToJson(text):
    """
    Converts a JavaScript object-literal array body into valid JSON text.

    Quotes unquoted object keys and strips line comments, while preserving
    the contents of double-quoted strings.

    Args:
        text (str): The JavaScript array body.

    Returns:
        str: The equivalent JSON text.
    """
    out = []
    idx = 0
    length = len(text)
    in_string = False
    while idx < length:
        ch = text[idx]
        if in_string:
            out.append(ch)
            if ch == "\\":
                idx += 1
                if idx < length:
                    out.append(text[idx])
            elif ch == '"':
                in_string = False
            idx += 1
        else:
            if ch == '"':
                in_string = True
                out.append(ch)
                idx += 1
            elif ch == "/" and idx + 1 < length and text[idx + 1] == "/":
                # Skips the remainder of the current line.
                while idx < length and text[idx] != "\n":
                    idx += 1
            elif ch.isalpha() or ch == "_":
                # Reads a full identifier.
                end = idx
                while end < length and (text[end].isalnum() or text[end] == "_"):
                    end += 1
                ident = text[idx:end]
                # Quotes the identifier if it is an object key (followed by ':').
                probe = end
                while probe < length and text[probe] in " \t":
                    probe += 1
                if probe < length and text[probe] == ":":
                    out.append('"' + ident + '"')
                else:
                    out.append(ident)
                idx = end
            else:
                out.append(ch)
                idx += 1
    return "".join(out)


def main():
    """
    Scrapes all quiz files and writes the indexed question sets to JSON.

    Returns:
        None
    """
    dataset = {}
    for section_index, file_name in enumerate(QUIZ_FILES, start=1):
        html_text = (QUIZ_DIR / file_name).read_text(encoding="utf-8")
        array_text = extractArrayText(html_text)
        json_text = jsToJson(array_text)
        questions = json.loads("[" + json_text + "]")
        dataset[str(section_index)] = questions
        print(f"Section {section_index}: {len(questions)} questions from {file_name}")

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(
        json.dumps(dataset, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    total_count = sum(len(questions) for questions in dataset.values())
    print(f"Wrote {len(dataset)} sections, {total_count} questions to {DATA_FILE}")


if __name__ == "__main__":
    main()