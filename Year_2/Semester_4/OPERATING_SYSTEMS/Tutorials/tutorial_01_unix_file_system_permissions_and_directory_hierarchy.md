# Tutorial 01: UNIX File System Permissions and Directory Hierarchy

This hands-on laboratory tutorial covers UNIX terminal navigation, absolute vs. relative path resolution, file and directory manipulation commands, inode concepts, and the UNIX file access permission model (symbolic and octal modes).

---

## 1. Directory Navigation and Path Mechanics

In UNIX, every file is located within a single hierarchical tree structure:
- **Absolute Path:** Begins with root `/` (e.g., `/home/student/workspace/lab1`).
- **Relative Path:** Begins relative to the Current Working Directory (CWD):
  - `.` refers to the current directory.
  - `..` refers to the immediate parent directory.

### Essential Navigation Commands
```bash
# Print current working directory
pwd

# Change directory using absolute path
cd /var/log

# Move up two levels in the directory tree
cd ../..

# Return to user home directory
cd ~
# or simply
cd
```

---

## 2. File and Directory Management

```bash
# Create directory hierarchy in a single command
mkdir -p projects/os_lab/src

# Create empty file or update timestamp
touch projects/os_lab/src/main.c

# Copy file preserving attributes
cp -p projects/os_lab/src/main.c projects/os_lab/src/main_backup.c

# Move or rename file
mv projects/os_lab/src/main_backup.c projects/os_lab/src/main_v1.c

# Remove file safely
rm projects/os_lab/src/main_v1.c

# Remove directory tree recursively
rm -rf projects/os_lab
```

---

## 3. UNIX File Permissions Model

Execute `ls -l` to view file attributes:

```text
-rwxr-xr-- 1 alice developers 4096 Sep 04 12:00 script.sh
```

### 3.1 Permission Triad Structure
The 10-character string breaks down as:
1. **File Type (1 char):** `-` (regular file), `d` (directory), `l` (symbolic link), `c` (character device), `b` (block device).
2. **User / Owner (3 chars):** `rwx` (read, write, execute).
3. **Group (3 chars):** `r-x` (read, execute).
4. **Others (3 chars):** `r--` (read only).

### 3.2 Permission Semantics: Files vs. Directories

| Permission Bit | Meaning on a Regular File | Meaning on a Directory |
|---|---|---|
| **Read (`r`)** | View file contents (`cat`, `less`) | List directory contents (`ls`) |
| **Write (`w`)** | Modify or overwrite file contents | Create, rename, or delete files inside directory |
| **Execute (`x`)** | Run file as executable binary or script | Traverse / enter directory (`cd`, access metadata) |

### 3.3 Octal Notation Representation
Each triad is converted to a 3-bit binary integer:
- `r` = 4 ($2^2$)
- `w` = 2 ($2^1$)
- `x` = 1 ($2^0$)

Examples:
- `rwxr-xr-x` = $(4+2+1)(4+0+1)(4+0+1) = \mathbf{755}$
- `rw-r--r--` = $(4+2+0)(4+0+0)(4+0+0) = \mathbf{644}$
- `rwx------` = $(4+2+1)(0)(0) = \mathbf{700}$

### 3.4 Modifying Permissions with chmod

```bash
# Octal mode: Give owner full access, group read+execute, others nothing
chmod 750 secure_script.sh

# Symbolic mode: Add execute to group and others
chmod go+x program.bin

# Symbolic mode: Revoke write from group and others
chmod go-w data.txt
```

