# Exercises — Navigation in the UNIX File System

**Based on:** `2_UNIX_File_System_Navigation.md`  
**Number of exercises:** 30

---

## Part A — Theory

### Exercise 1
What is the file system and what is its basic structure in UNIX?

---

### Exercise 2
Complete the table of UNIX file types:

| Symbol | File Type |
| :--- | :--- |
| `-` | |
| `d` | |
| `l` | |
| `c` or `b` | |
| `p` or `s` | |

---

### Exercise 3
Explain the difference between an **absolute** and a **relative** pathname. Give one example for each.

---

### Exercise 4
Mark **T** (True) or **F** (False):

1. An absolute path always starts with `/`.
2. A relative path depends on the current working directory (CWD).
3. The symbol `..` refers to the current directory.
4. The symbol `~` refers to the home directory of the current user.
5. The path `/etc/passwd` is relative.

---

### Exercise 5
The current working directory is `/home/student/projects`. What is the absolute path corresponding to each relative path?

(a) `report.txt`  
(b) `./docs/readme.md`  
(c) `../shared/data.csv`  
(d) `../../etc/hosts`

---

### Exercise 6
Mention the function of the directories `/bin`, `/dev`, `/etc`, `/home`, `/tmp`, `/var`, `/usr`.

---

### Exercise 7
What does the `pwd` command display and why is it useful before `cd` commands?

---

### Exercise 8
Explain the difference between `mkdir` and `mkdir -p`. Why is the `-p` option needed?

---

### Exercise 9
Why does the `rmdir` command fail if the directory is not empty? Which command is used to delete non-empty directories?

---

### Exercise 10
What does the `cd -` command do?

---

## Part B — Laboratory

### Exercise 11
Your current directory is `/home/user1/documents`. Give the command to move to the `/etc` directory using an **absolute** path.

---

### Exercise 12
Your current directory is `/home/user1/documents`. Give the command to move to the `/etc` directory using a **relative** path.

---

### Exercise 13
Your current directory is `/local/home/student/project1`. You want to create the directory `student1` inside `/local/home/teacher`. Give the full command with a **relative** pathname.

---

### Exercise 14
Your current directory is `/home/paul/data`. Give the command to move to `/home/peter/files` with a relative path.

---

### Exercise 15
Give the command to create the directory `projects/python/scripts` when the parent directories `projects` and `python` do not exist.

---

### Exercise 16
Give the command to create the directory `backup` in `/tmp` using an absolute path.

---

### Exercise 17
Give the command to delete the **empty** directory `old_empty` in the current directory.

---

### Exercise 18
Give the command to return to the home directory of the current user in the shortest way.

---

### Exercise 19
After a series of `cd` commands, you want to return to the previous working directory. Which command do you use?

---

### Exercise 20
The current directory is `/var/www/html`. Give the command to move two levels up (to `/var`).

---

## Part C — Complex Questions

### Exercise 21
Describe the file system navigation workflow: which commands do you use and in what order?

---

### Exercise 22
The current directory is `/home/alice/work/reports/2024`. Without using an absolute path, give the `cd` command to move to the directory `/home/bob/files`.

---

### Exercise 23
Explain why the "everything is a file" philosophy of UNIX is related to the existence of special files (`c`, `b`) in the `/dev` directory.

---

### Exercise 24
Circle the correct answer: Which symbol refers to the **parent** directory?

- a) `.`  
- b) `..`  
- c) `~`  
- d) `/`

---

### Exercise 25
A user runs `mkdir projects/subdir` while the `projects` directory does not exist. What error message will be displayed and how does the user fix it?

---

### Exercise 26
Draw a tree diagram for the structure:

```
/home/student/
├── docs/
│   └── notes.txt
├── photos/
└── scripts/
    └── run.sh
```

---

### Exercise 27
From the directory `/home/student/scripts`, which relative path leads to the file `notes.txt` located in `docs`?

---

### Exercise 28
Mark **T** or **F** and correct the false statements:

1. Pipes (`p`) and sockets (`s`) are used for communication between processes.
2. A symbolic link (`l`) stores the file data directly.
3. The `/tmp` directory is suitable for permanent storage of important data.
4. The `cd documents` command moves the user to the `documents` subdirectory of the CWD.
5. The root of the file system is represented by the symbol `\`.

---

### Exercise 29
A student wants to create the structure:

```
~/semester4/os/lab1/
```

Give the sequence of commands (one or more) to achieve this from any directory.

---

### Exercise 30
Explain why understanding the difference CWD / absolute / relative path is critical in UNIX laboratory exams. Give an example of a mistake that can be made if the CWD is not known.
