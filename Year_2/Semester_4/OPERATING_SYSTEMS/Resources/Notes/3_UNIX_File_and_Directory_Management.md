# 3. UNIX File and Directory Management

***

## File and Directory Deletion

### `rm` — Remove Files and Directories

The `rm` command deletes files permanently. Unlike modern graphical desktop environments, the UNIX terminal does not have a "Recycle Bin." Once a file is removed with `rm`, it is generally unrecoverable.

**Syntax:**
```sh
rm <file_name>
```

**Common Flags:**

| Flag | Description |
|------|-------------|
| `-i` | Interactive mode. Prompts for confirmation before deleting each file. |
| `-r` or `-R` | Recursive mode. Required to delete directories and their contents. |
| `-f` | Force mode. Ignores nonexistent files and never prompts for confirmation. Use with extreme caution. |

**Examples:**

```sh
rm report.txt              # Deletes a single file silently
rm -i important_data.csv   # Asks for confirmation before deletion
```
```text
rm: remove regular file 'important_data.csv'? y
```

**Deleting Directories:**
To delete a directory that contains files, you cannot use `rmdir`. You must use `rm -r`.

```sh
rm -r old_project/         # Deletes the directory and everything inside it
rm -ri old_project/        # Deletes recursively, but asks for confirmation at each step
```

**Warning:** Running `rm -rf /` is catastrophically destructive as it attempts to forcefully delete the entire file system starting from the root directory. Never run this command.

***

## Copying Files and Directories

### `cp` — Copy

The `cp` command duplicates files or directories from a source to a destination.

**Syntax:**
```sh
cp <source> <destination>
```

**Common Flags:**

| Flag | Description |
|------|-------------|
| `-r` or `-R` | Recursive mode. Required when copying directories. |
| `-i` | Interactive mode. Prompts before overwriting an existing file at the destination. |
| `-v` | Verbose mode. Prints the name of each file as it is copied. |

**Usage Scenarios:**

1. **Copying a single file to a new name:**
   ```sh
   cp original.txt backup.txt
   ```

2. **Copying a file into another directory:**
   ```sh
   cp original.txt /tmp/
   ```

3. **Copying multiple files into a directory:**
   ```sh
   cp file1.txt file2.txt /backup_dir/
   ```

4. **Copying an entire directory:**
   ```sh
   cp -r project_source/ project_backup/
   ```

**Overwriting Files:**
If a file with the target name already exists at the destination, `cp` will silently overwrite it by default. Using the `-i` flag prevents accidental data loss.

***

## Moving and Renaming

### `mv` — Move / Rename

The `mv` command is used for two distinct operations: moving files from one location to another, and renaming files. It does not require a recursive flag for directories.

**Syntax:**
```sh
mv <source> <destination>
```

**Usage Scenarios:**

1. **Renaming a file (moving it within the same directory):**
   ```sh
   mv old_name.txt new_name.txt
   ```

2. **Moving a file to another directory:**
   ```sh
   mv data.csv /home/user/archives/
   ```

3. **Moving and renaming simultaneously:**
   ```sh
   mv /tmp/download.zip /home/user/software_v2.zip
   ```

4. **Moving a directory:**
   ```sh
   mv my_project/ /var/www/html/
   ```

***

## Listing Directory Contents

### `ls` — List

The `ls` command displays the contents of a directory. By default, it lists files in the current working directory in alphabetical order.

**Syntax:**
```sh
ls [options] [directory]
```

**Common Flags:**

| Flag | Description |
|------|-------------|
| `-l` | Long listing format. Displays permissions, ownership, size, and timestamps. |
| `-a` | Show all files, including hidden files (those starting with a dot `.`). |
| `-h` | Human-readable file sizes (e.g., 1K, 234M, 2G). Often used with `-l`. |
| `-R` | Recursive listing. Lists the contents of all subdirectories. |
| `-t` | Sort by modification time, newest first. |

**Understanding `ls -l` Output:**

Running `ls -l` produces a detailed output row for each file:

```text
-rw-r--r-- 1 user group 1024 Oct 24 10:00 document.txt
drwxr-xr-x 2 user group 4096 Oct 24 10:05 my_folder
```

**Field Breakdown:**
1. **Type and Permissions:** The first 10 characters (e.g., `-rw-r--r--` or `drwxr-xr-x`). The first character indicates the file type (`-` for file, `d` for directory). The next 9 characters represent read, write, and execute permissions.
2. **Hard Links:** The number of hard links pointing to the inode.
3. **Owner:** The user who owns the file.
4. **Group:** The group that owns the file.
5. **Size:** The file size in bytes.
6. **Modification Date:** The date and time the file was last modified.
7. **Name:** The file or directory name.

**Combining Flags:**
Flags can be combined to form powerful commands.
```sh
ls -la       # Long listing, including hidden files
ls -lh       # Long listing with human-readable file sizes
ls -lt       # Long listing sorted by newest modification time
```
