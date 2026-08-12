# Exercises — Introduction to UNIX and Linux

**Based on:** `1_Introduction_to_UNIX.md`  
**Number of exercises:** 30

---

## Part A — Theory

### Exercise 1
What is an Operating System and what are the four basic domains it manages?

---

### Exercise 2
Explain the UNIX philosophy "everything is a file". Give two examples of resources that are treated as files.

---

### Exercise 3
Mark **T** (True) or **F** (False):

1. UNIX was created in 1969 by Kenneth Thompson at Bell Labs.
2. The transition of UNIX to the C language in 1973 increased its dependence on a specific hardware architecture.
3. The philosophy "do one thing and do it well" encourages small, specialized programs.
4. Linux was created by Sun Microsystems.
5. JSLinux allows learning the terminal without a local Linux installation.

---

### Exercise 4
Circle the correct answer: Which of the following is a **commercial** UNIX?

- a) FreeBSD  
- b) Linux  
- c) Solaris  
- d) JSLinux

---

### Exercise 5
Mention four basic characteristics of UNIX (multi-user, multi-tasking, etc.) and briefly explain each one.

---

### Exercise 6
Complete the user account properties table:

| Property | Description |
| :--- | :--- |
| `username` | |
| `userid` (UID) | |
| `groupid` (GID) | |
| `home directory` | |
| `shell` | |

---

### Exercise 7
What is the UID value of the root user and why is it important?

---

### Exercise 8
In which directory are user passwords usually stored (in encrypted form)?

---

### Exercise 9
Draw (or describe with a list) the hierarchical structure of the UNIX file system, starting from the root `/`. Mention at least five important directories and their contents.

---

### Exercise 10
What is the difference between the symbols `$` and `#` in the shell prompt?

---

### Exercise 11
Why is the password not displayed on the screen during login to the system?

---

### Exercise 12
Mention three ways to end a session (logout) on a UNIX system.

---

## Part B — Laboratory

### Exercise 13
Give the UNIX command to change the password of the current user.

---

### Exercise 14
The root user wants to change the password of user `student1`. What is the full command?

---

### Exercise 15
Give the command to display the current date and time of the system.

---

### Exercise 16
Give the command to display the calendar of the month of May 2024.

---

### Exercise 17
Give the command to display the calendar of the entire year 2025.

---

### Exercise 18
Which command displays the list of all users who are logged into the system, along with their terminal and login time?

---

### Exercise 19
Which command displays only the name of the current user?

---

### Exercise 20
What is the difference between the commands `whoami` and `who am i`?

---

### Exercise 21
After a successful login, in which directory is the user automatically placed? Give a typical example path.

---

### Exercise 22
Which directory is used for temporary files that are often deleted during reboot?

---

### Exercise 23
Which directory contains the system configuration files?

---

### Exercise 24
In a QEMU/JSLinux environment, which command requires root privileges for a safe shutdown of the virtual machine?

---

### Exercise 25
Explain what the concept of "chaining programs" means in the UNIX philosophy. Give a simple example (without using pipes yet — only as a concept).

---

## Part C — Complex Questions

### Exercise 26
A new student logs in for the first time to a Linux system. Describe step-by-step the process from the appearance of the `login:` prompt to the appearance of the shell prompt.

---

### Exercise 27
Compare Windows, macOS and UNIX/Linux with respect to: (a) design philosophy, (b) multi-user support, (c) open source vs commercial model.

---

### Exercise 28
Why is the transition of UNIX from assembly to C in 1973 considered decisive for its spread across different architectures?

---

### Exercise 29
The user `maria` has UID=1001, GID=100, home directory `/home/maria` and shell `/bin/bash`. Explain what each of these properties means when starting a session.

---

### Exercise 30
Mark **T** or **F** and briefly justify:

1. Passwords in UNIX are case-insensitive.
2. `/root` is the home directory of the superuser.
3. BusyBox is used in lightweight environments such as JSLinux.
4. The `passwd` command can be executed without interactive confirmation on all systems.
5. `/bin` contains system configuration files.
