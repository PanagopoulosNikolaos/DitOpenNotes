# Exercises — UNIX Wildcards and Glob Patterns

**Based on:** `7_UNIX_Wildcards_and_Glob_Patterns.md`  
**Number of exercises:** 32

---

## Part A — Theory

### Exercise 1
What is globbing and who performs it — the command or the shell?

---

### Exercise 2
Explain the function of the wildcards `*`, `?` and `[...]`. Give one example for each.

---

### Exercise 3
What is the difference between `*` and `?`? Which files match `file?.txt` and which do **not**?

---

### Exercise 4
Explain negation in character classes: `[!...]` and `[^...]`. What does `[!0-9]*` match?

---

### Exercise 5
Why does `rm *` **not** delete hidden files (files starting with `.`)? How do we include them?

---

### Exercise 6
Explain why wildcards do not cross directory boundaries (`/`). What does `*/*.txt` match?

---

### Exercise 7
How do we "avoid" wildcard interpretation when we want a literal `*` or `?` in a file name?

---

### Exercise 8
Mark **T** (True) or **F** (False):

1. `*` matches zero or more characters.
2. `?` matches exactly one character.
3. `ls *.txt` also matches `report.csv`.
4. `rm doc*` deletes files starting with `doc`.
5. Single quotes `'...'` prevent globbing.

---

## Part B — Pattern Matching

### Exercise 9
Which of the following files match `*.txt`?

`report.txt`, `data.csv`, `notes.TXT`, `file.txt.bak`, `tmp`

---

### Exercise 10
Which match `file?.txt`?

`file1.txt`, `file10.txt`, `fileA.txt`, `file.txt`, `file_.txt`

---

### Exercise 11
Which match `??-report`?

`Q3-report`, `01-report`, `1-report`, `2024-report`

---

### Exercise 12
Which match `file[123].txt`?

`file1.txt`, `file2.txt`, `file4.txt`, `file12.txt`

---

### Exercise 13
Which match `[0-9][0-9]_data.csv`?

`14_data.csv`, `1_data.csv`, `99_data.csv`, `abc_data.csv`

---

### Exercise 14
Which match `[!0-9]*`?

`report.txt`, `1file.txt`, `data.csv`, `.hidden`

---

## Part C — Laboratory

### Exercise 15
Give the command to display all files ending in `.txt` in the current directory.

---

### Exercise 16
Give the command to delete all files starting with `doc`.

---

### Exercise 17
Give the command to copy all files containing the word `backup` anywhere in their name to `/tmp/`.

---

### Exercise 18
Give the command to delete files in the current directory that start with `grade`, end in `.tmp` and consist of **a total** of 15 characters.

---

### Exercise 19
Give the command to move files with exactly 3 characters in their name to the `archives/` directory.

---

### Exercise 20
Give the command to set execute permissions on `script_v2.sh`, `script_v3.sh`, `script_v4.sh`, `script_v5.sh` (without affecting other versions).

---

### Exercise 21
Give the command to delete the monthly logs of 2022: `log_file_2022_01.log` to `log_file_2022_12.log`.

---

### Exercise 22
Give the command to display hidden files in the current directory.

---

### Exercise 23
Give the command to delete a file with the literal name `file*.txt` (not a glob pattern).

---

### Exercise 24
Give commands to organize a downloads folder:

- Move images (`.jpg`, `.png`, `.gif`) to `~/Pictures/`
- Move documents (`.pdf`, `.doc`, `.docx`) to `~/Documents/`

---

## Part D — Complex Questions

### Exercise 25
The current directory contains: `grade12345.tmp`, `grade123456.tmp`, `gradeABCDE.tmp`. Which of these match `grade??????.tmp` (6 question marks)?

---

### Exercise 26
What happens if `rm *` is executed in a directory containing only the hidden files `.bashrc` and `.profile`? Explain.

---

### Exercise 27
Explain why `cp *backup* /tmp/` matches `mybackup.zip` but not necessarily `back_up.zip`.

---

### Exercise 28
Circle the correct answer: Which pattern matches `.log` files starting with a lowercase letter?

- a) `[A-Z]*.log`  
- b) `[a-z]*.log`  
- c) `[a-Z]*.log`  
- d) `*.log`

---

### Exercise 29
Design a scenario where the careless use of a wildcard leads to the accidental deletion of important files. How do we avoid it?

---

### Exercise 30
Give the command to display `.txt` files located **exactly one level** below the current directory.

---

### Exercise 31
Mark **T** or **F**:

1. Globbing happens before the command is executed.
2. `ls *` matches directories too.
3. `[A-Z]*` matches files starting with an uppercase letter.
4. `rm 'file?.txt'` deletes files that match the pattern `file?.txt`.
5. Wildcards work inside double quotes `"..."` for all characters.

---

### Exercise 32
A student wants to delete all `temp` files followed by exactly one digit (e.g., `temp1`, `temp9`) but not `temp10`. Which pattern does the student use and what is the command?
