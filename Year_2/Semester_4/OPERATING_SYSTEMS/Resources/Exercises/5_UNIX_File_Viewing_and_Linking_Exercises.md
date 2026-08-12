# Exercises — UNIX File Viewing and Links

**Based on:** `5_UNIX_File_Viewing_and_Linking.md`  
**Number of exercises:** 28

---

## Part A — Theory

### Exercise 1
What is the basic difference between `cat`, `less` and `more`? When do we prefer `less`?

---

### Exercise 2
Explain the function of the `head` and `tail` commands. What is their default behavior?

---

### Exercise 3
What does the `-f` option of the `tail` command do and in which cases is it useful?

---

### Exercise 4
Interpret the output of the `wc report.txt` command:

```text
  45  130  850 report.txt
```

---

### Exercise 5
Explain the `-l`, `-w`, `-c` options of the `wc` command.

---

### Exercise 6
What is the difference between `sort`, `sort -r`, `sort -n` and `sort -u`?

---

### Exercise 7
Explain the difference between a **symbolic** (soft) and a **hard** link.

---

### Exercise 8
Complete the table:

| Feature | Hard Link | Symbolic Link |
| :--- | :--- | :--- |
| Crosses file systems? | | |
| Can point to a directory? | | |
| What happens if the original file is deleted? | | |
| Creation command | | |

---

### Exercise 9
Mark **T** (True) or **F** (False):

1. `cat -n` numbers the output lines.
2. A hard link shares the same inode as the original file.
3. If the original file is deleted, the symbolic link continues to work normally.
4. `tail -n 5` displays the last 5 lines.
5. `sort -n` sorts numerically (e.g., 10 after 2).

---

## Part B — Laboratory

### Exercise 10
Give the command to display the contents of `readme.txt` on the screen.

---

### Exercise 11
Give the command to display the contents of `file1.txt` and `file2.txt` one after the other.

---

### Exercise 12
Give the command to view `large_log.txt` one screen at a time with scrolling capability.

---

### Exercise 13
Which keys are used in `less` for: (a) scrolling one screen down, (b) scrolling one screen up, (c) exiting?

---

### Exercise 14
Give the command to display the first 20 lines of `data.txt`.

---

### Exercise 15
Give the command to display the last 15 lines of `log.txt`.

---

### Exercise 16
Give the command to monitor in real time new lines added to `/var/log/syslog`.

---

### Exercise 17
Give the command to count only the number of lines in `file.txt`.

---

### Exercise 18
Give the command to sort `data.txt` in descending alphabetical order.

---

### Exercise 19
Give the command to sort numerically and remove duplicate lines from `numbers.txt`.

---

### Exercise 20
Give the command to create a symbolic link `myapp.conf` pointing to `/etc/nginx/sites-available/myapp.conf`.

---

### Exercise 21
Give the command to create a hard link `backup_link` to `original.txt`.

---

## Part C — Complex Questions

### Exercise 22
Why is `cat` not suitable for very large files? Which alternative do you suggest?

---

### Exercise 23
How does a symbolic link appear in the `ls -l` output? Give an example line.

---

### Exercise 24
A symbolic link points to a file that was deleted. What is this state called and what happens when you try to read the link?

---

### Exercise 25
You have a file `scores.txt` with 1000 lines. You want to see lines 990–1000. Which command(s) do you use?

---

### Exercise 26
Circle the correct answer: Which command does **not** change the content of the original file?

- a) `cat file.txt`  
- b) `ln file.txt hardlink`  
- c) `ln -s file.txt symlink`  
- d) `head file.txt`

---

### Exercise 27
Explain when you would prefer a hard link instead of a symbolic link and vice versa.

---

### Exercise 28
Mark **T** or **F** and justify:

1. Two hard links to the same file have the same inode number.
2. `wc -lw file.txt` counts lines and words without displaying the file name if input redirection is used.
3. `sort` always modifies the original file.
4. `cat -A` helps detect hidden characters (tabs, line endings).
5. Symbolic links appear with `l` in the first column of `ls -l`.
