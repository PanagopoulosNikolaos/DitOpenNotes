# Exercises — UNIX File and Directory Management

**Based on:** `3_UNIX_File_and_Directory_Management.md`  
**Number of exercises:** 32

---

## Part A — Theory

### Exercise 1
Explain why the `rm` command in UNIX is dangerous compared to the "Recycle Bin" in graphical environments.

---

### Exercise 2
Complete the table of options of the `rm` command:

| Option | Description |
| :--- | :--- |
| `-i` | |
| `-r` / `-R` | |
| `-f` | |

---

### Exercise 3
What is the difference between `rmdir` and `rm -r`? When is each one used?

---

### Exercise 4
Mark **T** (True) or **F** (False):

1. The `cp` command requires the `-r` option to copy directories.
2. The `mv` command requires the `-r` option to move directories.
3. `mv` can be used to rename a file.
4. `cp` silently replaces an existing file in the destination by default.
5. The command `rm -rf /` is safe in an educational environment.

---

### Exercise 5
Interpret the output of the `ls -l` command:

```text
-rw-r--r-- 1 user group 1024 Oct 24 10:00 document.txt
drwxr-xr-x 2 user group 4096 Oct 24 10:05 my_folder
```

Mention what each field means.

---

### Exercise 6
What does the number `2` mean in the line `drwxr-xr-x 2 user group ... my_folder`?

---

### Exercise 7
Explain the function of the options `-l`, `-a`, `-h`, `-R`, `-t` of the `ls` command.

---

### Exercise 8
What is the difference between `ls -lh` and `ls -lt`?

---

## Part B — Laboratory

### Exercise 9
Give the command to delete the file `report.txt` in the current directory.

---

### Exercise 10
Give the command to delete the file `important_data.csv` with confirmation before each deletion.

---

### Exercise 11
Give the command to delete the directory `old_project/` and all its contents.

---

### Exercise 12
Give the command to copy `original.txt` to `backup.txt` in the same directory.

---

### Exercise 13
Give the command to copy `original.txt` to the `/tmp/` directory.

---

### Exercise 14
Give the command to copy the files `file1.txt` and `file2.txt` to the `/backup_dir/` directory.

---

### Exercise 15
Give the command to copy the entire directory `project_source/` to `project_backup/`.

---

### Exercise 16
Give the command to rename `old_name.txt` to `new_name.txt`.

---

### Exercise 17
Give the command to move `data.csv` to `/home/user/archives/`.

---

### Exercise 18
Give the command to move and rename simultaneously: `/tmp/download.zip` should be moved as `/home/user/software_v2.zip`.

---

### Exercise 19
Give the command to move the directory `global` (in the current directory) to `/local`.

---

### Exercise 20
Give the command to display all files (including hidden ones) in list format with details.

---

### Exercise 21
Give the command to recursively display all files and subdirectories of the current directory in list format with details, including hidden ones.

---

### Exercise 22
What will happen if the command `ls -Rla .` is executed on a UNIX system? Answer in detail.

---

### Exercise 23
Give the command to display directory contents sorted by modification time (newest first), with human-readable sizes.

---

## Part C — Complex Questions

### Exercise 24
You want to copy the directory `src/` to `dst/` but avoid accidentally overwriting existing files. Which option of `cp` do you use?

---

### Exercise 25
Explain why `mv` does not need `-r` while `cp` needs it for directories.

---

### Exercise 26
A user runs `rm -ri old_project/`. Describe the behavior of the command step by step.

---

### Exercise 27
In the `ls -l` output, the following appears:

```text
lrwxrwxrwx 1 user user 20 Jun 10 09:00 link -> /etc/hosts
```

What file type is `link` and what does the `->` mean?

---

### Exercise 28
Circle the correct answer: Which command does **not** change the inode number of the file?

- a) `cp original.txt copy.txt`  
- b) `mv old.txt new.txt`  
- c) `rm old.txt`  
- d) `ln original.txt hardlink`

---

### Exercise 29
Give the sequence of commands for: (1) creating a `backup` directory, (2) copying all `.txt` files of the current directory to `backup`, (3) displaying the contents of `backup` in list format.

---

### Exercise 30
Mark **T** or **F**:

1. The `-v` option of `cp` displays the name of each copied file.
2. `ls` without arguments displays the contents of the current directory.
3. `rm -f` always asks for confirmation before deleting.
4. The first character in the permissions column of `ls -l` indicates the file type.
5. `mv` can move files only within the same directory.

---

### Exercise 31
The current directory contains 50 files. You want to see only the 5 most recently modified in list format. Which command do you use? (Hint: combine `ls` with `head`.)

---

### Exercise 32
Explain what the warning about `rm -rf /` means and why even experienced administrators may run it by mistake. Suggest a security practice.
