# 5. UNIX File Viewing and Linking

***

## Viewing File Contents

### `cat` — Concatenate and Print

The `cat` command is primarily used to display the entire contents of a file on the terminal screen.

**Syntax:**
```sh
cat <file_name>
cat file1 file2       # Displays the contents of file1 followed immediately by file2
```

**Common Flags:**
- `-n`: Numbers all output lines.
- `-A`: Displays non-printable characters (e.g., ends of lines as `$`, tabs as `^I`).

*(Note: `cat` is not ideal for very large files because it prints everything at once, causing the text to scroll by too quickly to read. For large files, pagers like `less` or `more` are preferred.)*

### `less` and `more` — Pagers

Pagers allow you to view the contents of a file one screen at a time.

```sh
less large_log.txt
```
**Navigation in `less`:**
- `Spacebar` or `Page Down`: Scroll down one screen.
- `b` or `Page Up`: Scroll up one screen.
- `Down Arrow` / `Up Arrow`: Scroll line by line.
- `q`: Quit and return to the prompt.
- `/pattern`: Search forward for a specific word or pattern.

### `head` — View the Beginning of a File

Displays the first few lines of a file (default is 10 lines).

**Syntax:**
```sh
head <file_name>
head -n 20 <file_name>    # Displays the first 20 lines
head -c 50 <file_name>    # Displays the first 50 bytes/characters
```

### `tail` — View the End of a File

Displays the last few lines of a file (default is 10 lines).

**Syntax:**
```sh
tail <file_name>
tail -n 15 <file_name>    # Displays the last 15 lines
```

**Following a file:**
The `-f` (follow) flag is incredibly useful for monitoring log files. It keeps the file open and displays new lines as they are appended in real-time.
```sh
tail -f /var/log/syslog
```
*(Press `Ctrl + C` to stop following the file.)*

***

## File Analysis Commands

### `wc` — Word Count

Counts the number of lines, words, and characters in a file.

**Syntax:**
```sh
wc <file_name>
```

**Output example:**
```text
  45  130  850 report.txt
```
*(Represents 45 lines, 130 words, 850 characters)*

**Common Flags:**
- `-l`: Print only the line count.
- `-w`: Print only the word count.
- `-c`: Print only the byte/character count.

### `sort` — Sort Lines of Text

Sorts the contents of a text file line by line. By default, it sorts in lexicographical (alphabetical) ascending order.

**Syntax:**
```sh
sort data.txt
```

**Common Flags:**
- `-r`: Reverse the sorting order (descending).
- `-n`: Sort numerically rather than alphabetically (e.g., treats "10" as greater than "2").
- `-u`: Unique. Removes duplicate lines from the output.

***

## Linking Files

UNIX allows you to create links to files. A link is essentially a pointer or an alias to an existing file. There are two types: Hard Links and Symbolic (Soft) Links.

### Symbolic Links (Soft Links)

A symbolic link is a special type of file that simply contains the path to another file. If you delete the original file, the symbolic link becomes "broken" or "dangling."

**Creating a Symbolic Link:**
```sh
ln -s <target_file> <link_name>
```

**Examples:**
```sh
ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/myapp.conf
```
*(Creates a symlink in `sites-enabled` pointing to the actual configuration file.)*

When you run `ls -l`, symbolic links are indicated by an `l` in the permissions string and an arrow `->` pointing to the target:
```text
lrwxrwxrwx 1 user user 35 Oct 24 10:00 myapp.conf -> /etc/nginx/sites-available/myapp.conf
```

### Hard Links

A hard link creates a direct pointer to the underlying data (inode) on the hard drive. The system treats a hard link identically to the original file. If you delete the original file, the data remains accessible via the hard link until all hard links to that data are deleted.

**Creating a Hard Link:**
```sh
ln <target_file> <link_name>
```

**Differences between Hard and Soft Links:**
- Hard links cannot cross different file systems or partitions; soft links can.
- Hard links cannot point to directories; soft links can.
- Soft links are far more common in everyday UNIX usage.
