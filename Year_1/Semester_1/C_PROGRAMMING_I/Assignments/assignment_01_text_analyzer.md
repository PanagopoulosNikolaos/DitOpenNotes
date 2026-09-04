# Assignment 01: Modular Text Analyzer Utility

## Objective
Design and implement a modular command-line text analyzer utility in C. This assignment evaluates understanding of standard input processing, string parsing, arrays, modular function decomposition, and basic file reading.

---

## Technical Specifications

### 1. Functional Requirements
The program must accept a text file path via command-line arguments:
```bash
./text_analyzer --input sample.txt
```

The utility must parse the contents of the target text file and compute:
1. **Total Character Count**: Total bytes read (including whitespace and punctuation).
2. **Whitespace Count**: Total spaces, tabs, and newline characters.
3. **Word Count**: Total continuous sequences of non-whitespace characters.
4. **Sentence Count**: Total sentences demarcated by '.', '!', or '?'.
5. **Character Frequency Distribution**: Frequency table of all alphabetical letters ('a'-'z', case-insensitive).
6. **Average Word Length**: Ratio of total non-whitespace alphabetical characters to total words.

### 2. Architecture and Data Structures
Organize the solution across modular header and implementation files:
```c
typedef struct {
    size_t total_chars;
    size_t whitespace_chars;
    size_t word_count;
    size_t sentence_count;
    unsigned int letter_frequency[26];
    double average_word_length;
} TextStatistics;
```

Required functions:
* `void initializeStatistics(TextStatistics *stats)`: Zeros all counters and frequency bins.
* `int analyzeFile(const char *filepath, TextStatistics *stats)`: Streams and processes file content.
* `void displayReport(const TextStatistics *stats)`: Prints a formatted console summary and ASCII frequency histogram.

### 3. Deliverables and Constraints
* Source files: `main.c`, `analyzer.c`, `analyzer.h`, and `Makefile`.
* Compilation flags: `-Wall -Wextra -Werror -std=c11 -pedantic`.
* Clean error handling for missing CLI arguments, unreadable files, and empty input files.
* Code must adhere to Google-style docstrings and strict casing conventions.

---

## Evaluation Rubric

| Criterion | Description | Points |
|:---|:---|:---:|
| Correctness of Metrics | Accurately counts characters, words, sentences, and letter frequencies | 30 |
| Modular Code Architecture | Clear separation across header and source files with Makefile | 25 |
| Robust Error Handling | Validates file existence, empty files, and CLI parameters gracefully | 20 |
| Code Standards & Docstrings | Conforms to Google-style docstrings, PascalCase, camelCase, snake_case | 15 |
| Presentation & Output Format | Formats text tables cleanly and outputs readable frequency histogram | 10 |
| **Total** | | **100** |

