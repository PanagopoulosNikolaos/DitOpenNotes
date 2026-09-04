# Tutorial 02: UNIX Pipelines, I/O Redirection, and Text Processing Filters

This practical laboratory tutorial covers standard POSIX input/output streams, file descriptor redirection, inter-process communication using anonymous pipelines (`|`), and powerful text transformation filters (`grep`, `awk`, `sed`, `sort`, `uniq`, `cut`).

---

## 1. POSIX Standard Streams and File Descriptors

Every standard UNIX process begins execution with three pre-opened file descriptors:
- **`0` - Standard Input (`stdin`):** Defaults to keyboard stream.
- **`1` - Standard Output (`stdout`):** Defaults to terminal screen.
- **`2` - Standard Error (`stderr`):** Defaults to terminal screen (unbuffered error messages).

---

## 2. Shell Redirection Operators

```bash
# Redirect stdout to file, overwriting existing contents
command > output.txt

# Redirect stdout to file, appending to existing contents
command >> output.txt

# Redirect stdin from an existing file
command < input.txt

# Redirect stderr to an error log file
command 2> error.log

# Redirect both stdout and stderr to the same file
command > full_log.txt 2>&1
# or modern bash shorthand:
command &> full_log.txt

# Discard unwanted diagnostic output
command 2> /dev/null
```

---

## 3. UNIX Command Pipelines (`|`)

A pipeline connects the standard output stream of the left-hand process directly to the standard input stream of the right-hand process via a kernel buffer:

```
[ Process 1 ] === stdout (fd 1) ===> [ Kernel Pipe Buffer ] === stdin (fd 0) ===> [ Process 2 ]
```

The pipe operator provides streaming execution without creating intermediate temporary files on disk.

---

## 4. Fundamental Text Processing Filters

### 4.1 Filter Syntax Overview

| Filter Utility | Primary Functionality | Canonical Example |
|---|---|---|
| `grep` | Pattern searching using Regular Expressions | `grep -E '^[0-9]{3}' log.txt` |
| `cut` | Extract delimiter-separated fields from lines | `cut -d: -f1,7 /etc/passwd` |
| `sort` | Sort text lines alphabetically or numerically | `sort -n -k2 data.csv` |
| `uniq` | Report or filter adjacent duplicate lines | `sort file.txt \| uniq -c` |
| `wc` | Count lines (`-l`), words (`-w`), or bytes (`-c`) | `wc -l /etc/passwd` |
| `sed` | Stream editor for text transformation / replacement | `sed 's/old_text/new_text/g' file.txt` |
| `awk` | Pattern scanning and columnar data extraction language | `awk '{print $1, $NF}' access.log` |

### 4.2 Comprehensive Worked Pipeline Scenarios

#### Scenario 1: Top 5 Active System Users by Process Count
```bash
ps -eo user | sort | uniq -c | sort -rn | head -n 5
```
**Explanation:**
1. `ps -eo user`: Lists username of owner for every running system process.
2. `sort`: Groups identical usernames adjacent to each other.
3. `uniq -c`: Counts occurrences of each unique consecutive username.
4. `sort -rn`: Numerically (`-n`) sorts in descending reverse (`-r`) order.
5. `head -n 5`: Outputs the top 5 entries.

#### Scenario 2: Extracting Unique Client IP Addresses from Apache Web Logs
```bash
awk '{print $1}' /var/log/apache2/access.log | sort -u | wc -l
```
**Explanation:**
1. `awk '{print $1}'`: Extracts the first column (client IP address) from each log record.
2. `sort -u`: Sorts and eliminates duplicates in a single pass.
3. `wc -l`: Computes total unique visiting clients.

