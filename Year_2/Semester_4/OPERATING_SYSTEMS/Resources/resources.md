# Operating Systems: Curated Resources and Reference Guide

A curated reference guide of authoritative textbooks, kernel programming documentation, UNIX standards, and system tracing utilities for Operating Systems (Course Code 402).

---

## 1. Foundational Textbooks

- **Operating System Concepts**  
  *Authors:* Abraham Silberschatz, Peter B. Galvin, and Greg Gagne.  
  *Annotation:* The standard textbook on operating system design principles, covering process synchronization, deadlock handling, CPU scheduling, memory management, and paging.

- **Modern Operating Systems**  
  *Author:* Andrew S. Tanenbaum and Herbert Bos.  
  *Annotation:* Renowned systems textbook emphasizing architectural trade-offs, monolithic vs microkernels, IPC mechanisms, and virtualization.

- **The Linux Programming Interface (TLPI)**  
  *Author:* Michael Kerrisk.  
  *Annotation:* The definitive reference manual for Linux and UNIX system programming, providing authoritative explanations of `fork()`, `execve()`, signals, pipes, and POSIX threads.

---

## 2. UNIX Standards and Kernel Documentation

- **The Open Group Base Specifications Issue 7 / IEEE Std 1003.1 (POSIX.1)**  
  *URL:* `https://pubs.opengroup.org/onlinepubs/9699919799/`  
  *Description:* Authoritative specification of the standard POSIX C library, system calls, and shell environment utilities.

- **Linux Kernel Documentation**  
  *URL:* `https://www.kernel.org/doc/html/latest/`  
  *Description:* Official architecture and subsystem documentation for process scheduling (CFS), virtual memory subsystem, and filesystem drivers.

- **GNU Coreutils Manual**  
  *URL:* `https://www.gnu.org/software/coreutils/manual/`  
  *Description:* Complete technical guide for basic file, shell, and text manipulation utilities (`cat`, `ls`, `chmod`, `sort`, `uniq`).

---

## 3. Systems Debugging and Profiling Utilities

- **Valgrind**  
  *URL:* `https://valgrind.org/`  
  *Description:* Instrumentation framework for memory debugging, memory leak detection, and cache profiling.

- **strace**  
  *URL:* `https://strace.io/`  
  *Description:* Diagnostic utility that monitors and logs system calls made by a process and the signals received.

