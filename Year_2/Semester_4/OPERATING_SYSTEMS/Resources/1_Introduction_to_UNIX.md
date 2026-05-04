# 1. Introduction to UNIX and Linux Terminal Basics

***

## What is an Operating System?

An Operating System (OS) is the foundational software layer that manages all hardware and software resources of a computer. Without an OS, computers are unusable by standard applications and end-users. It handles CPU scheduling, memory management, file systems, and peripheral devices.

Common operating systems include Windows, macOS, UNIX, and Linux distributions.

***

## History and Philosophy of UNIX

| Year | Event |
|------|-------|
| 1969 | Created by Kenneth Thompson at Bell Labs, written in PDP-7 assembly (initially single-user). |
| 1971 | Rewritten in PDP-11 assembly. |
| 1973 | Rewritten entirely in the C programming language by Dennis Ritchie at Bell Labs. This transition made it multi-user and highly portable. |
| 1984 | Standardization efforts began to ensure portability across various hardware architectures. |

**UNIX Philosophy Highlights:**
- **Everything is a file:** From regular text files to directories, keyboards, and network connections, UNIX treats almost all resources as files.
- **Do one thing and do it well:** Programs are designed to be small, modular, and focused on a single task.
- **Chaining programs:** Complex tasks are accomplished by combining simple programs together.

***

## UNIX and Linux Distributions

UNIX evolved into numerous commercial and open-source variants:
- **Commercial UNIX:** Solaris (Sun Microsystems), AIX (IBM), HP/UX (Hewlett-Packard).
- **Free/Open Source:** Linux (originally created by Linus Torvalds), FreeBSD.
- **JSLinux / Lightweight Terminals:** Environments like JSLinux run a minimal Linux kernel (often using BusyBox) directly in a web browser, providing a lightweight sandbox for learning terminal basics without local installation.

***

## UNIX Core Features

- **Multi-User / Time Sharing:** Multiple users can access the system simultaneously, sharing the CPU and memory.
- **Multi-Tasking:** Each user can run multiple programs concurrently.
- **User Accounts:** Every user has a dedicated account, ensuring security and isolation of file spaces.
- **Networking:** Built from the ground up with networking in mind, allowing remote access and resource sharing.

***

## User Account Properties

When you interact with a Linux terminal, you do so under a specific user account.

| Property | Description |
|----------|-------------|
| `username` | The identifier used to log in. |
| `password` | The secret authentication key (stored in encrypted format, usually in `/etc/shadow`). |
| `userid` (UID) | A unique integer representing the user internally. Root is always `0`. |
| `groupid` (GID) | An integer identifying the user's primary group, used for resource access control. |
| `home directory` | The dedicated directory where the user stores personal files (e.g., `/home/username`). |
| `shell` | The command-line interpreter that processes your commands (e.g., `/bin/bash`, `/bin/sh`). |

***

## The Filesystem Structure

The UNIX filesystem is organized as a hierarchical tree. The absolute top of this tree is the **root directory**, represented by a single forward slash `/`.

```text
/
├── bin/      (Essential command binaries)
├── etc/      (System configuration files)
├── home/     (User home directories)
│   ├── fred/
│   ├── sue/
│   └── user1/
├── root/     (Home directory for the root superuser)
└── tmp/      (Temporary files)
```

***

## Login, Logout, and the Shell

### The Login Process

When you connect to a UNIX system, you are prompted for your credentials.

```sh
login: user1
Password: 
```

- Passwords are **case-sensitive** and are **never echoed** to the screen for security reasons.
- Upon successful authentication, the system sets your current working directory to your home directory and launches your default **shell**.

### The Shell Prompt

The shell indicates it is ready to accept commands by displaying a prompt.
- `$` usually denotes a standard user.
- `#` usually denotes the root user (superuser).

### Logout

To terminate your session, use any of the following methods:

```sh
exit
```
```sh
logout
```
Alternatively, press `Ctrl + D` (which sends an End-of-File signal to the shell).

***

## Basic Terminal Commands

### `passwd` — Change Password

Changes the password for the current user. Root users can change any user's password by supplying the username as an argument.

```sh
passwd
```

**Interactive Flow:**
```text
Changing password for user1.
(current) UNIX password: 
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
```

### `date` — Display Date and Time

Outputs the current system date and time.

```sh
date
```
```text
Thu Oct 24 10:00:00 UTC 2024
```

**Custom Formatting:**
```sh
date +"%Y-%m-%d %H:%M:%S"
```

### `cal` — Display Calendar

Displays a formatted calendar.

```sh
cal               # Shows the current month
cal 2024          # Shows the entire year 2024
cal 5 2024        # Shows May 2024
```

### `who` and `whoami` — User Information

Identify who is currently logged into the system.

```sh
who
```
Displays a list of all currently logged-in users, their terminal line, and login time.

```sh
whoami
```
Displays only the username associated with the current effective user ID.

```sh
who am i
```
Displays details specifically for the current terminal session.

***

## Lab Environment Note: QEMU / JSLinux

If you are using a virtualized environment like QEMU or a browser-based emulator like JSLinux:
- You are typically interacting with a minimal command-line interface.
- You may start out automatically logged in as `root` or a generic user.
- To shut down a virtual machine safely from the command line, use the `halt`, `poweroff`, or `shutdown -h now` commands (requires root privileges).
