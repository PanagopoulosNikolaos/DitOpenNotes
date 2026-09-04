# Lecture 01: UNIX Architecture and Terminal Environment

This lecture covers operating system fundamentals, the UNIX design philosophy ("everything is a file", small modular tools), kernel-space vs. user-space separation, the Filesystem Hierarchy Standard (FHS), and POSIX shell mechanics.

---

## 1. Operating System Architecture

An operating system is the system software layer managing physical hardware resources and providing a hardware-independent virtual machine interface to user applications.

```
+-------------------------------------------------------------+
| User Applications (bash, gcc, python, vim, browser)         |
+-------------------------------------------------------------+
| Standard C Library (glibc, POSIX API wrappers)              |
+-------------------------------------------------------------+
====== System Call Interface (syscall trap / sysenter) =======
| OS Kernel:                                                  |
|   [ Process Scheduler ]      [ Memory Manager / Paging ]    |
|   [ Virtual File System ]    [ Device Drivers / Network ]   |
+-------------------------------------------------------------+
| Physical Hardware (CPU, RAM, Disks, Network Interfaces)     |
+-------------------------------------------------------------+
```

### 1.1 Dual-Mode Operation and System Calls
- **User Mode:** Unprivileged CPU execution ring (Ring 3 on x86). Code cannot directly execute privileged machine instructions or access hardware registers.
- **Kernel Mode:** Fully privileged CPU execution ring (Ring 0 on x86). Kernel code has unrestricted access to hardware instructions and address spaces.
- **Mode Switch via System Call:** When an application requires an OS service (e.g., `read()`, `write()`, `fork()`), it triggers a software interrupt or CPU trap instruction (`syscall`), switching from User Mode to Kernel Mode.

---

## 2. The UNIX Philosophy

Originating from Ken Thompson and Dennis Ritchie at Bell Labs, UNIX design principles emphasize:
1. **Modularity:** Make each program do one thing well.
2. **Text Streams as Universal Interface:** Expect the output of every program to become the input to another, as yet unknown, program.
3. **Everything is a File:** Devices, sockets, pipes, and directories are represented as byte streams accessed via uniform file descriptors through `open()`, `read()`, `write()`, `close()`.

---

## 3. The UNIX Filesystem Hierarchy Standard (FHS)

UNIX organizes all files into a single unified hierarchical tree rooted at `/`:

```
/
├── bin        Essential user command binaries (ls, cp, rm, bash)
├── boot       Static files of the boot loader and kernel image (vmlinuz)
├── dev        Device special files (null, zero, tty, sda)
├── etc        Host-specific system-wide configuration files (passwd, fstab)
├── home       User home directories (/home/alice, /home/bob)
├── lib        Shared libraries needed for binaries in /bin and /sbin
├── proc       Virtual kernel process information filesystem
├── sbin       Essential system administration binaries (fdisk, reboot)
├── sys        Virtual sysfs kernel device and subsystem tree
├── tmp        Temporary files, wiped across reboots
├── usr        Secondary hierarchy containing user utilities and libraries
│   ├── bin    Non-essential user binaries (gcc, python, git)
│   └── lib    Libraries for /usr/bin
└── var        Variable data files (log files, mail spools, databases)
```

---

## 4. Special UNIX Virtual Filesystems

- `/dev/null`: The bit bucket. Discards all data written to it; returns EOF (`0` bytes) upon read.
- `/dev/zero`: Provides an endless stream of null bytes (`0x00`), commonly used to initialize memory buffers or wipe disk sectors.
- `/proc`: Exposes kernel and process data structures as a virtual directory hierarchy:
  - `/proc/cpuinfo`: Processor microarchitecture and flags.
  - `/proc/meminfo`: RAM utilization metrics.
  - `/proc/[PID]/`: Status, memory maps, and open file descriptors of process `[PID]`.

