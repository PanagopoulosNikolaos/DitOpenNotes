# Operating Systems

## Course Overview
This course provides a comprehensive foundation in modern operating system architecture, kernel mechanisms, and concurrent systems programming. Topics include process lifecycles and context switching, CPU scheduling algorithms, inter-process communication (IPC), concurrency synchronization primitives (mutexes, semaphores, condition variables), deadlock analysis, virtual memory management, demand paging and page replacement policies, UNIX file system internals, and POSIX shell automation.

## Course Code
402 (OPERATING SYSTEMS)

## Prerequisites
* C Programming II (Code: 201)
* Computer Architecture (Code: 301)
* Data Structures and Algorithms (Code: 305)

---

## Topics Covered
* **Kernel & Architectural Foundations**: Dual-mode execution (user mode vs. kernel mode), privileged instructions, trap handling, system call interfaces, and monolithic vs. microkernel designs.
* **Process Management & CPU Scheduling**: Process Control Blocks (PCB), process states, context switching overhead, fork-exec model, scheduling criteria, and algorithms (FCFS, SJF, SRTF, Round Robin with dynamic quantum, Multi-Level Feedback Queues).
* **Concurrency & Synchronization**: Race conditions, critical section problem, Peterson's algorithm, hardware primitives (Test-And-Set, Compare-And-Swap), mutex locks, counting and binary semaphores, monitors, and classic concurrency problems (Producer-Consumer, Readers-Writers, Dining Philosophers).
* **Deadlock Analysis**: Coffman conditions, resource allocation graphs (RAG), deadlock prevention, deadlock avoidance via Dijkstra's Banker's Algorithm, and deadlock detection and recovery.
* **Memory Management & Virtual Memory**: Contiguous memory allocation, external/internal fragmentation, compaction, paging architecture, Page Tables, Translation Lookaside Buffers (TLB), effective memory access time (EMAT), multi-level paging, and page replacement policies (FIFO, Optimal, LRU, Second-Chance/Clock).
* **Storage & File Systems**: File system abstractions, inode structures, hard links vs. symbolic links, directory representations, disk allocation methods, and UNIX file permissions.
* **UNIX Systems Programming**: POSIX IPC channels (pipes, named FIFOs), signal handling (`kill`, `sigaction`), and shell scripting pipelines.

---

## Learning Objectives
* Write robust concurrent C programs utilizing POSIX processes (`fork`, `exec`, `waitpid`), pipes, and synchronization primitives.
* Evaluate CPU scheduling algorithms by calculating average waiting time, turnaround time, and response time across diverse workload patterns.
* Formulate mathematical proofs and algorithms for deadlock avoidance utilizing Dijkstra's Banker's Algorithm.
* Calculate TLB hit rates, page fault rates, and effective access times under multi-level paging hierarchies.
* Automate operating system administration and log analysis tasks using modular Bash shell scripts with regular expressions and pipes.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules and departmental UNIX/OS slides |
| [`Exercises/`](Exercises/) | Numerical and conceptual drills on CPU scheduling, paging, permissions, and command filters |
| [`Examples/`](Examples/) | Executable POSIX C systems code, shell automation scripts, and walkthrough guides |
| [`Assignments/`](Assignments/) | Practical laboratory assignments on shell scripting and multi-process IPC |
| [`Tutorials/`](Tutorials/) | Hands-on guides for UNIX file system hierarchy, permissions, and pipeline redirection |
| [`Projects/`](Projects/) | Capstone design specification for an interactive custom UNIX shell interpreter in C |
| [`Exams/`](Exams/) | Past laboratory and theory examination papers, practice exams, and grading criteria |
| [`Resources/`](Resources/) | Consolidated lecture notes, UNIX command guides, topic mindmaps, and external literature |

---

## Tooling and Simulation Environment

### POSIX C Compilation & Execution
To compile and execute systems C code under strict POSIX compliance:
```bash
gcc -Wall -Wextra -pedantic -std=c11 Examples/examples_posix_processes_and_pipes.c -o run_pipes
./run_pipes
```

### Memory Leak Detection with Valgrind
To detect memory leaks or file descriptor leaks:
```bash
valgrind --leak-check=full --track-origins=yes ./run_pipes
```

### UNIX Shell Script Execution
To validate and run system automation scripts:
```bash
bash -n Examples/examples_unix_shell_automation.sh
chmod +x Examples/examples_unix_shell_automation.sh
./Examples/examples_unix_shell_automation.sh
```