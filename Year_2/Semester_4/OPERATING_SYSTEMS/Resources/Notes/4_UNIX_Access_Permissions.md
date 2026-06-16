# 4. UNIX Access Permissions

***

## The Permission Model

UNIX is a multi-user operating system. To maintain security and privacy, every file and directory is protected by a set of permissions that dictate who can read, modify, or execute them.

Permissions are categorized into three ownership tiers:

1. **User (Owner - `u`):** The account that owns the file (usually the creator).
2. **Group (`g`):** A defined collection of users who share access rights to the file.
3. **Other (`o`):** Everyone else on the system who is not the owner and not in the group.

For each of these tiers, three types of permissions can be granted:

| Permission | Symbol | Value | Meaning on a File | Meaning on a Directory |
|------------|--------|-------|-------------------|------------------------|
| **Read** | `r` | 4 | View file contents. | List the files inside the directory (`ls`). |
| **Write** | `w` | 2 | Modify or delete file contents. | Create, delete, or rename files inside the directory. |
| **Execute**| `x` | 1 | Run the file as a program or script. | Traverse the directory (access files within it). |

***

## Interpreting Permission Strings

When you run `ls -l`, the first column displays a 10-character string representing the file type and permissions.

```text
-rwxr-x--- 1 user1 staff  1024 Oct 24 file.txt
drwxr-xr-x 2 user1 staff  4096 Oct 24 folder/
```

**Deconstructing `-rwxr-x---`:**
- `[` `-` `]` Type: Regular file.
- `[` `rwx` `]` User (Owner): Has Read, Write, and Execute permissions.
- `[` `r-x` `]` Group: Has Read and Execute permissions, but cannot Write (modify).
- `[` `---` `]` Other: Has no access whatsoever.

***

## Directories: The `Execute` Bit

A common point of confusion is how permissions apply to directories.

- To use `cd` to enter a directory, you **must** have Execute (`x`) permission on it.
- To see the names of files inside a directory (using `ls`), you need Read (`r`) permission.
- However, to read the attributes of the files inside (using `ls -l`), you need **both** Read and Execute permissions on the directory.
- To create or delete a file inside a directory, you need Write (`w`) and Execute (`x`) permissions on the directory, regardless of the permissions of the file itself.

***

## Modifying Permissions: `chmod`

The `chmod` (change mode) command is used to alter permissions. Only the file owner or the `root` user can change a file's permissions.

There are two primary methods to use `chmod`: Numeric (Octal) and Symbolic.

### Method 1: Numeric (Octal) Notation

This method uses numbers to represent permission sets. You sum the values of the permissions you want to grant for each tier.
- Read = 4
- Write = 2
- Execute = 1

**Examples:**
- `rwx` = 4 + 2 + 1 = **7**
- `rw-` = 4 + 2 + 0 = **6**
- `r-x` = 4 + 0 + 1 = **5**
- `r--` = 4 + 0 + 0 = **4**

You construct a 3-digit number representing User, Group, and Other:

```sh
chmod 755 script.sh
```
*Sets `rwxr-xr-x`. Owner can do everything; Group and Other can read and execute.*

```sh
chmod 644 document.txt
```
*Sets `rw-r--r--`. Owner can read/write; Group and Other can only read. (Standard file permission)*

```sh
chmod 700 private_folder/
```
*Sets `rwx------`. Only the owner has access. (Standard for private directories)*

### Method 2: Symbolic Notation

This method uses letters to selectively add or remove permissions without affecting others.

**Syntax:** `chmod [who][operator][permission] file`

- **Who:** `u` (user), `g` (group), `o` (other), `a` (all)
- **Operator:** `+` (add), `-` (remove), `=` (set exactly)
- **Permission:** `r`, `w`, `x`

**Examples:**

```sh
chmod u+x script.sh         # Add execute permission for the owner
chmod go-w file.txt         # Remove write permission for group and others
chmod a+r public.txt        # Add read permission for everyone
chmod g=rx shared_dir/      # Set group permission exactly to read and execute
chmod u=rwx,g=rx,o=r file   # Set multiple permissions separated by commas
```

***

## Ownership Commands

### `chown` — Change Owner

Changes the user ownership of a file or directory.

```sh
chown user2 report.txt              # Change owner to user2
chown user2:finance report.txt      # Change owner to user2 and group to finance
chown -R user2 project_dir/         # Recursively change ownership for a directory
```

### `chgrp` — Change Group

Changes only the group ownership of a file or directory.

```sh
chgrp finance report.txt
```

*(Note: In most Linux systems, including JSLinux, changing ownership usually requires `root` privileges via `sudo` or logging in as root.)*

***

## Default Permissions: `umask`

When you create a new file or directory, the system assigns default permissions based on the `umask` (user file-creation mode mask).

The default maximum permissions are `666` for files and `777` for directories. The `umask` value is *subtracted* from these maximums.

If your `umask` is `022`:
- New files will have `666 - 022 = 644` (`rw-r--r--`).
- New directories will have `777 - 022 = 755` (`rwxr-xr-x`).

You can check or set your umask:
```sh
umask        # Displays current umask (e.g., 0022)
umask 027    # Sets new umask, resulting in files (640) and dirs (750)
```
