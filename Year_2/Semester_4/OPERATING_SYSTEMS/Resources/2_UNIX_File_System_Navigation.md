# 2. UNIX File System Navigation

***

## Understanding the File System

The file system is the component of the operating system responsible for organizing, storing, and retrieving files. In UNIX and Linux, the file system is strictly hierarchical (tree-shaped), with all files and directories stemming from a single origin.

***

## Unix File Types

While UNIX adheres to the philosophy that "everything is a file," it distinguishes between several file types:

- **Regular Files (`-`):** Standard files containing data, text, or executable code.
- **Directories (`d`):** Special files that contain lists of other files and directories.
- **Symbolic Links (`l`):** Pointers to other files or directories.
- **Special Files (`c` or `b`):** Represent hardware devices (e.g., terminals, hard drives) usually found in `/dev`.
- **Pipes and Sockets (`p` or `s`):** Used for inter-process communication.

***

## The Hierarchy and Important Directories

The top level of the hierarchy is the **root directory**, represented by `/`. 

| Directory | Common Contents |
|-----------|-----------------|
| `/` | The absolute root of the file system. |
| `/bin` | Essential executable commands (e.g., `ls`, `cp`, `mkdir`). |
| `/dev` | Device files representing hardware. |
| `/etc` | System-wide configuration files. |
| `/home` | User home directories (e.g., `/home/username`). |
| `/tmp` | Temporary files, often cleared when the system reboots. |
| `/var` | Variable data files, such as logs and databases. |
| `/usr` | Secondary hierarchy for user data and read-only applications. |

***

## Pathnames: Absolute vs. Relative

A pathname is the string of characters used to identify a location in the directory tree. Understanding the difference between absolute and relative pathnames is critical for navigation.

### Absolute Pathnames

An absolute path always defines the location starting from the root directory (`/`). It is a complete path that will work regardless of your current working directory.

**Characteristics:**
- Always begins with a forward slash `/`.
- Uniquely identifies a single file or directory.

**Examples:**
```sh
/home/user1/documents/report.txt
/etc/ssh/sshd_config
/var/log/syslog
```

### Relative Pathnames

A relative path defines the location starting from your **Current Working Directory (CWD)**. It is relative to where you currently are in the file system.

**Characteristics:**
- Never begins with a forward slash `/`.
- Can be shorter and more convenient.

**Special Navigational Symbols:**
| Symbol | Meaning |
|--------|---------|
| `.` | The current directory. |
| `..` | The parent directory (one level up). |
| `~` | The current user's home directory. |

**Examples (Assuming CWD is `/home/user1/`):**
```sh
documents/report.txt     # Refers to /home/user1/documents/report.txt
./documents/report.txt   # Identical to the above
../user2/file.txt        # Refers to /home/user2/file.txt
../../etc/passwd         # Refers to /etc/passwd
```

***

## Navigation Commands

### `pwd` — Print Working Directory

Displays the absolute pathname of your current location in the file system.

```sh
pwd
```
```text
/home/user1/documents
```

### `cd` — Change Directory

Changes your current working directory. It accepts both absolute and relative paths.

**Syntax:**
```sh
cd <path>
```

**Common Usage Patterns:**
| Command | Action |
|---------|--------|
| `cd /etc` | Move to `/etc` (Absolute path). |
| `cd documents` | Move to `documents` within the current directory (Relative path). |
| `cd ..` | Move up one directory level. |
| `cd ../..` | Move up two directory levels. |
| `cd ~` or `cd` | Return immediately to your home directory. |
| `cd -` | Return to the previous directory you were in. |

***

## Directory Management Commands

### `mkdir` — Make Directory

Creates one or more new directories.

**Syntax:**
```sh
mkdir <directory_name>
```

**Examples:**
```sh
mkdir projects           # Creates 'projects' in the current directory
mkdir /tmp/testdir       # Creates 'testdir' in /tmp using an absolute path
```

**Creating Nested Directories:**
If you attempt to create a directory inside a parent that does not exist, `mkdir` will fail. Use the `-p` (parents) flag to create the entire path structure at once.

```sh
mkdir -p projects/python/scripts
```
This command ensures that `projects`, `python`, and `scripts` are all created without errors.

### `rmdir` — Remove Directory

Removes empty directories.

**Syntax:**
```sh
rmdir <directory_name>
```

**Important Caveat:**
`rmdir` will only succeed if the target directory contains absolutely no files or subdirectories. If the directory is not empty, you will receive an error:
```text
rmdir: failed to remove 'projects': Directory not empty
```
To remove a directory and all of its contents simultaneously, you must use the `rm` command with recursive flags (covered in the next section).

***

## Summary of Navigation Workflow

1. Use `pwd` to confirm where you are.
2. Use `cd` to move around the system.
3. Use `mkdir` to create new organizational folders.
4. Remember to use `.` and `..` to reference relative locations quickly without typing long absolute paths.
