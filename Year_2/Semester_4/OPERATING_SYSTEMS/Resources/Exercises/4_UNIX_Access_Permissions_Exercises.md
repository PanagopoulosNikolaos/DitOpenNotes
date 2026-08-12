# Exercises — UNIX Access Permissions

**Based on:** `4_UNIX_Access_Permissions.md`  
**Number of exercises:** 35

---

## Part A — Theory

### Exercise 1
Explain the UNIX permissions model: User (Owner), Group, Other. What do `r`, `w`, `x` mean for **files** and what for **directories**?

---

### Exercise 2
Convert the following to numeric (octal) form:

(a) `rwxr-xr-x`  
(b) `rw-r--r--`  
(c) `rwx------`  
(d) `r--rwxw-x`

---

### Exercise 3
Convert the following from numeric to symbolic form:

(a) `755`  
(b) `644`  
(b) `700`  
(d) `72`

---

### Exercise 4
Mark **T** (True) or **F** (False):

1. To enter a directory with `cd`, execute permission (`x`) is required.
2. To see file names with `ls`, read permission (`r`) on the directory is required.
3. For `ls -l` on a directory, only the `r` permission is sufficient.
4. To create a file in a directory, `w` and `x` on the directory are required.
5. Only the owner can change permissions with `chmod`.

---

### Exercise 5
Explain the difference between numeric (octal) and symbolic notation in `chmod`. Give one example for each.

---

### Exercise 6
What do the commands do?

(a) `chmod u+x script.sh`  
(b) `chmod go-w file.txt`  
(c) `chmod a+r public.txt`  
(d) `chmod g=rx shared_dir/`

---

### Exercise 7
Explain the function of the `chown` and `chgrp` commands. When are root privileges required?

---

### Exercise 8
What is `umask` and how are the default permissions of new files and directories calculated?

---

### Exercise 9
If the `umask` is `022`, what will be the default permissions for:

(a) a new file  
(b) a new directory

---

### Exercise 10
If the `umask` is set to `027`, what will be the default permissions for a new file and a new directory?

---

## Part B — Laboratory

### Exercise 11
You want to set `rwxr-xr-x` permissions on `script.sh`. What is the `chmod` command in numeric notation?

---

### Exercise 12
You want `rw-r--r--` permissions on `document.txt`. Give the command.

---

### Exercise 13
You want `rwx------` permissions on the directory `private_folder/`. Give the command.

---

### Exercise 14
You want to ensure that on the file `photo` (your ownership) you have read, write and execute, while everyone else has only write. Give the command in numeric notation.

---

### Exercise 15
Give the command to add execute permission only for the owner of `run.sh`.

---

### Exercise 16
Give the command to remove write permission from group and others on `secret.txt`.

---

### Exercise 17
Give the command to change the owner of `report.txt` to `user2`.

---

### Exercise 18
Give the command to change the owner to `user2` and the group to `finance` for `report.txt`.

---

### Exercise 19
Give the command to recursively change the owner of all files in `project_dir/` to `user2`.

---

### Exercise 20
Give the command to display the current `umask`.

---

### Exercise 21
Give the command to set the `umask` so that new files have `640` and directories `750`.

---

## Part C — Permissions Analysis

### Exercise 22
In the `ls -l` output the following appears:

```text
-r--rwxw-x 1 ray green 12 March 15 11:54 grades
```

Mark **True** or **False**:

(a) The group `green` can modify `grades`.  
(b) `ray` can modify the contents of `grades`.  
(c) Only someone outside the group `green` can see the contents.  
(d) Only the group and the owner can modify `grades`.

---

### Exercise 23
In the `ls -l` output:

```text
drwxr-x--- 3 alice staff 4096 Jun 1 14:00 shared/
```

(a) Can the user `bob` (not alice, not staff) run `cd shared`?  
(b) Can a member of the group `staff` see the file names with `ls shared`?  
(c) Can `alice` create a new file inside `shared`?

---

### Exercise 24
A directory has `dr--r--r--` permissions. Can a user with read permission run `ls` inside the directory? Can the user run `cd`? Explain.

---

### Exercise 25
A file has `rwxrwxrwx`. Is this a good security practice? Why?

---

### Exercise 26
Calculate the numeric value: the owner has `rw-`, the group `r--`, others `---`.

---

### Exercise 27
Which `chmod` command (symbolic) sets exactly `u=rwx,g=rx,o=` on `file`?

---

## Part D — Complex Questions

### Exercise 28
Explain why the permissions of a directory affect the ability to access the files inside it, even if the files themselves have broader permissions.

---

### Exercise 29
An administrator wants a shared directory where all members of the group `dev` can read, write and enter, while everyone else has no permissions at all. What permissions does the administrator set and which `chmod` command does the administrator use?

---

### Exercise 30
Mark **T** or **F**:

1. The command `chgrp finance report.txt` changes only the group.
2. Root can always change the permissions of any file.
3. `umask 0022` and `umask 022` are equivalent on many systems.
4. The permissions `r=4, w=2, x=1` apply to each triplet (user, group, other).
5. `chmod` can change the owner of a file.

---

### Exercise 31
Circle the correct answer: Which command changes **only** the group of a file?

- a) `chown`  
- b) `chgrp`  
- c) `chmod`  
- d) `umask`

---

### Exercise 32
A script must be executable only by the owner, but everyone must be able to read it. What permissions (`rwxrwxrwx` form and numeric) do you set?

---

### Exercise 33
Describe the flow: a new user creates the file `notes.txt` with default `umask 022`. What permissions will `ls -l` show? How does the user change them to `rw-------` with one command?

---

### Exercise 34
In a multi-user system, why does UNIX use groups in addition to owner and others? Give an example of application in a laboratory project.

---

### Exercise 35
Given that the line `drwxrwxrwt` appears on the `/tmp` directory, explain (in general) what the `t` (sticky bit) means and why it is important in shared directories.
