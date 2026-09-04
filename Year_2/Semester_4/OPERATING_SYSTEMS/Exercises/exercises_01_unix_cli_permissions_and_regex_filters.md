# Exercises 01: UNIX Terminal Navigation, Permissions, and Shell Pipelines

This practice problem set provides step-by-step solutions for octal permission conversions, symbolic `chmod` operations, and pipeline filter constructions.

---

## Problem 1: File Access Permissions and Octal Representation

### Question 1.1
Convert the following symbolic permission strings into their 3-digit octal representations:
1. `-rwxr-x---`
2. `-rw-rw-r--`
3. `-r--------`
4. `drwxrwxrwx`

#### Solution
Recall: $r=4$, $w=2$, $x=1$.
1. `rwx` = $4+2+1=7$, `r-x` = $4+0+1=5$, `---` = $0 \implies \mathbf{750}$
2. `rw-` = $4+2+0=6$, `rw-` = $4+2+0=6$, `r--` = $4+0+0=4 \implies \mathbf{664}$
3. `r--` = $4+0+0=4$, `---` = $0$, `---` = $0 \implies \mathbf{400}$
4. `rwx` = $7$, `rwx` = $7$, `rwx` = $7 \implies \mathbf{777}$ (directory flag `d` is not part of the numeric octal mask)

---

### Question 1.2
A file currently has permissions `rw-r--r--` (`644`).
1. Write the symbolic `chmod` command to grant write permissions to group members without altering owner or other permissions.
2. Write the symbolic `chmod` command to revoke read permissions from others.
3. Write the single octal `chmod` command that achieves both modifications simultaneously.

#### Solution
1. `chmod g+w filename`
2. `chmod o-r filename`
3. Original: `rw-r--r--` (`644`). After changes: `rw-rw----` ($4+2=6, 4+2=6, 0 \implies \mathbf{660}$). Command: `chmod 660 filename`.

---

## Problem 2: Constructing Single-Line Shell Pipelines

### Question 2.1
Given the system password file `/etc/passwd` (colon-delimited, where field 1 is username, field 3 is UID, and field 7 is login shell):
Write a single-line shell pipeline that extracts and lists all distinct login shells used by accounts whose UID is strictly greater than or equal to 1000, sorted alphabetically.

#### Solution
```bash
awk -F: '$3 >= 1000 {print $7}' /etc/passwd | sort -u
```
**Explanation:**
- `-F:` sets the input field separator to colon.
- `$3 >= 1000`: Evaluates condition on field 3 (UID).
- `{print $7}`: Prints field 7 (login shell path).
- `sort -u`: Sorts the resulting shell names alphabetically and removes duplicate entries.

---

### Question 2.2
Write a pipeline to count how many `.c` source files located within the directory tree `~/projects` contain more than 100 lines of code.

#### Solution
```bash
find ~/projects -name '*.c' -exec wc -l {} + | awk '$1 > 100 && $2 != "total" {count++} END {print count+0}'
```
**Explanation:**
- `find ~/projects -name '*.c'`: Locates all C source files recursively.
- `-exec wc -l {} +`: Batches line counting efficiently across all found files.
- `awk`: Filters entries where the line count ($1) exceeds 100 (ignoring summary line `"total"`), increments counter, and prints the result.

