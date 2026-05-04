# 7. UNIX Wildcards and Glob Patterns

***

## What are Wildcards (Globbing)?

Wildcards are special characters used in the terminal to match multiple filenames or directories simultaneously based on a pattern. The process of expanding these patterns into actual filenames is called "globbing," and it is performed by the shell *before* the command executes.

Using wildcards makes file management highly efficient, saving you from typing long lists of files manually.

***

## The Primary Wildcards

### The Asterisk (`*`) — Zero or More Characters

The asterisk is the most common wildcard. It matches any sequence of characters, including an empty string (zero characters).

**Examples:**

| Command | Matches | Does Not Match |
|---------|---------|----------------|
| `ls *.txt` | All files ending in `.txt` (e.g., `report.txt`, `data.txt`). | `report.csv`, `script.sh` |
| `rm doc*` | Any file starting with `doc` (e.g., `doc1`, `document.pdf`, `doc`). | `mydoc.txt` |
| `cp *backup* /tmp/` | Any file containing the word `backup` anywhere in its name. | `back_up.zip` |
| `ls *` | All visible files and directories in the current folder. | Hidden files (e.g., `.bashrc`) |

### The Question Mark (`?`) — Exactly One Character

The question mark matches exactly one character. It will not match zero characters or multiple characters.

**Examples:**

| Command | Matches | Does Not Match |
|---------|---------|----------------|
| `ls file?.txt` | `file1.txt`, `fileA.txt`, `file_.txt` | `file10.txt`, `file.txt` |
| `rm ??-report` | `Q3-report`, `01-report` | `1-report`, `2024-report` |
| `mv ??? archives/`| Any file with exactly 3 characters in its name. | `ab`, `abcd` |

### Square Brackets (`[...]`) — Character Classes

Square brackets define a set or range of characters. It matches exactly one character that is included within the brackets.

**Examples:**

| Command | Matches |
|---------|---------|
| `ls file[123].txt` | `file1.txt`, `file2.txt`, `file3.txt` |
| `cat [a-z]*.log` | Any `.log` file starting with a lowercase letter. |
| `rm [A-Z]*` | Any file starting with an uppercase letter. |
| `mv [0-9][0-9]_data.csv /tmp/`| Files starting with exactly two digits (e.g., `14_data.csv`). |

**Negation (`[!...]` or `[^...]`):**
Placing an exclamation mark `!` (or a caret `^` in some shells) immediately inside the opening bracket negates the class, matching any character *except* those listed.

```sh
ls [!0-9]*
```
*(Matches any file that does **not** start with a number.)*

***

## Wildcard Exceptions and Gotchas

### 1. Hidden Files
By default, wildcards **do not** match hidden files (files starting with a dot `.`).

If you run `rm *`, it deletes all visible files but leaves `.bashrc` and `.profile` intact. To match hidden files, you must explicitly include the dot in your pattern:
```sh
ls .*
```

### 2. Directory Separators
Wildcards do not cross directory boundaries (the `/` character).
The pattern `*/*.txt` matches `.txt` files located exactly one directory level down, but it will not match `.txt` files in the current directory or two levels down.

***

## Escaping Wildcards

Sometimes you need to use a literal asterisk `*` or question mark `?` in a filename (though this is bad practice). To stop the shell from interpreting them as wildcards, you must escape or quote them.

**Using a Backslash (`\`):**
```sh
rm file\*.txt
```
*(Deletes a file literally named `file*.txt`)*

**Using Quotes:**
```sh
rm 'file*.txt'
```
*(Single quotes prevent all globbing and variable expansion.)*

***

## Practical Workflow Examples

**1. Organizing a messy downloads folder:**
```sh
mv *.jpg *.png *.gif ~/Pictures/
mv *.pdf *.doc *.docx ~/Documents/
```

**2. Cleaning up numbered logs, keeping only recent ones:**
```sh
rm log_file_2022_??.log
```
*(Deletes all monthly logs from 2022, e.g., `log_file_2022_01.log` to `log_file_2022_12.log`)*

**3. Running a command on specific script versions:**
```sh
chmod +x script_v[2-5].sh
```
*(Makes versions 2, 3, 4, and 5 executable)*
