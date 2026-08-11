# Operating Systems (Mindmap)

## Operating Systems Theory

### Chapter 1: Introduction
- **Definition of Operating System (OS)**
  - Intermediary between user and hardware (ease of use, program execution)
  - Resource allocator (CPU, memory, I/O)
  - Control Program (execution control and I/O)
  - Kernel — the only program that runs continuously
- **Elements of a Computing System (CS)**
  - Hardware — CPU, memory, I/O devices
  - Operating System (OS)
  - Application Programs — DBMS, compilers, etc.
  - Users — humans, machines, other computers
- **Historical Evolution of OS**
  - Serial Processing (early 1940s – mid 1950s) — no OS, direct interaction, routing/setup time waste
  - Simple Batch Systems / Batch Processing (early–mid 1960s) — monitor, Job Control Language (JCL), memory protection, timer, privileged commands, interrupts
  - Multiprogramming (1965–1980) — maximizing CPU utilization during I/O waiting, memory partitioning, memory protection through hardware
  - Time-Sharing — time quantum (quantum / burst), minimizing response time, interactive users
  - Fourth Generation (1980–1990) — LSI integrated circuits, friendly OS, network OS, Distributed OS, real-time systems
  - Modern Developments (1990+) — Linux, Middleware, POSIX (standardization), Mobile computing

### Chapter 2: OS Purposes and Evolution
- **Basic Purposes**
  - Hardware protection
  - User communication (user abstraction)
  - Resource management, utilization, and control
  - Evolution capability and ease (new hardware/service compatibility, fixes)
- **Hardware Protection**
  - Dual-Mode operation — User Mode (bit = 1) and Monitor/Kernel Mode (bit = 0)
  - Privileged Instructions — I/O, load base/limit, load timer, mode bit switching
  - I/O Protection — traps, system calls (service routine control by monitor)
  - Memory Protection — Base & Limit registers (address range `[base, base + limit)`), MMU
  - CPU Protection — Timer & clock ticks (preventing CPU monopolization)
- **User Abstraction (User Communication)**
  - Abstraction layers (User/Programmer → Applications → Utilities → OS → Hardware)
  - Microprogramming — interpreter in ROM (microcode) translating machine language
  - OS Kernel — permanently in main memory
- **Resource Management & Evolution**
  - Processor, memory, I/O allocation
  - 5 Evolution Axes — Processes, Memory Management, Security, Scheduling, Structure
  - OS Design Hierarchy (Layered Architecture — 13 layers, from circuits to shell)
  - Modern OS Features — Microkernel, Multithreading, SMP, Distributed, Real-time

### Chapter 3: Processes
- **Process Concept**
  - Process definition — program in execution (active entity), PCB
  - Address space — Code (executable), Data (variables), Stack (calls/locals), Heap (dynamic memory)
  - Difference between process and program (active vs passive entity)
- **States and Transitions**
  - Basic states — Ready, Running, Blocked
  - Suspend states — Blocked/Suspend, Ready/Suspend (freeing main memory, backing store)
  - State transitions — Running -> Blocked (I/O request), Running -> Ready (timeout/quantum), Blocked -> Ready (I/O completion), Ready -> Running (via Dispatcher)
- **Process Management (Process Control)**
  - Process Control Block (PCB) — Program Counter, registers, state, UID, PID, priority
  - Process Table — Linked list of PCBs
  - Context Switch — CPU state save/restore
- **Creation and Control (UNIX System Calls)**
  - `fork()` — create new process (copy, returns 0 to child, PID to parent)
  - `exec()` — replace memory image with new executable program
  - `exit()` — terminate process
  - `wait()` — parent waiting for child termination

### Chapter 4: Operating System Architectures
- **Kernel Structure**
  - Monolithic Systems — all sections in Kernel Mode, maximum performance, difficult debugging
  - Layered Architecture — hierarchical organization, clean interfaces, overhead due to transitions
  - Microkernel Architecture — minimal services in kernel, modularity, server processes in User Mode, increased reliability
- **Threads / Multithreading**
  - Multithreading — multiple threads within the same process, shared address space, faster context switch
  - User-Level Threads (ULT) — library management in user space, fast switching, blocking call blocks entire process
  - Kernel-Level Threads (KLT) — kernel management, true parallel execution, higher overhead
- **Systems and Processing**
  - Multiprocessing — Symmetric (SMP) vs Asymmetric (AMP)
  - Parallel Systems — Tightly coupled (shared memory) vs Loosely coupled (distributed)
  - Real-Time Systems — Hard real-time (strict deadlines) vs Soft real-time
  - Distributed Systems

### Chapter 5: Mutual Exclusion
- **Basic Concepts**
  - Race Condition — result dependency on execution order/timing
  - Critical Section — code section accessing shared resource
  - 4 correct CS operation conditions — Mutual Exclusion, no speed/CPU assumptions, no blocking outside CS, no starvation
- **Software Solutions**
  - Dekker Algorithm
  - Peterson Algorithm — using flag (entry desire) and turn (concession)
- **Hardware Support**
  - Disable Interrupts — only in single-processor systems
  - Special CPU commands — Test-and-Set-Lock (TSL), Exchange (XCHG) / Compare-and-Swap (atomic operations)
- **Semaphores**
  - Definition — integer variable s with atomic operations `wait()` (P) and `signal()` (V)
  - Binary Semaphores (Mutex) — values 0 or 1
  - General/Counting Semaphores — managing multiple resources
  - Implementation without busy waiting — using blocked process queue

### Chapter 6: Deadlock
- **Deadlock Concept**
  - Deadlock definition — mutual blocking of processes waiting for resources held by others
  - Resource types — Reusable vs Consumable, Preemptable vs Non-preemptable
- **Modeling and Conditions**
  - Resource Allocation Graphs (RAG) — cycles indicate deadlocks
  - 4 necessary Coffman conditions — Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait (must hold simultaneously)
- **Handling Approaches**
  - Ostrich Algorithm — ignoring the problem (common in general OS)
  - Prevention — design exclusion of one of the 4 Coffman conditions (e.g., hierarchical request)
  - Avoidance — dynamic safety check during resource allocation
    - Banker's Algorithm — Safe/Unsafe states, Available, Max, Allocation, Need vectors
  - Detection and Recovery — RAG checking, process termination, resource preemption
- **Dining Philosophers Problem**
  - Deadlock scenario (all take left fork)
  - Synchronization solutions — user restriction, atomic take of both forks with semaphores

### Chapter 7: Memory Management
- **Basic Concepts**
  - Memory Manager — tracking, allocation, deallocation, protection, relocation
  - Addressing — Logical/Virtual vs Physical addresses
- **Partitioning**
  - Fixed Partitioning — Internal Fragmentation
  - Dynamic Partitioning — External Fragmentation
  - Memory Compaction — moving processes to merge gaps (CPU expensive)
- **Placement Algorithms**
  - First-Fit — first suitable position (fast)
  - Next-Fit — first suitable after last placement
  - Best-Fit — position with smallest possible remainder (creates small useless gaps)
  - Worst-Fit — largest available position
- **Swapping**
  - Roll-out / Roll-in processes to Backing Store (disk)
  - Free space tracking — Bitmaps vs Linked Lists

### Chapter 8: Virtual Memory
- **Paging**
  - Virtual Pages and Physical Frames
  - Page Table — Virtual -> Physical mapping
  - MMU (Memory Management Unit) — hardware address conversion
  - TLB (Translation Lookaside Buffer) — fast cache of conversions
  - Page Fault — interrupt when page not loaded in memory (flow: trap -> disk -> load frame -> update table -> restart instruction)
- **Segmentation**
  - Logical program organization into variable-size segments (code, stack, data)
  - Segment Table
- **Page Replacement Algorithms**
  - Optimal Algorithm (OPT / MIN) — replace page to be used later (theoretical)
  - FIFO — replace oldest page (Belady's Anomaly: more frames -> more faults)
  - LRU (Least Recently Used) — replace page unused longest (high cost)
  - Clock Algorithm (Second Chance) — LRU approach with reference bit in circular list

### Chapter 9: CPU Scheduling
- **Performance Criteria**
  - CPU Utilization — percentage of busy time
  - Throughput — number of processes per unit time
  - Turnaround Time — total time from submission to end
  - Waiting Time — time in Ready queue
  - Response Time — time from submission to first response
- **Scheduling Types**
  - Non-preemptive — process holds CPU until termination or blocking
  - Preemptive — kernel can interrupt process (quantum expiration, priority)
- **Scheduling Algorithms**
  - FCFS (First-Come, First-Served) — non-preemptive (Convoy Effect)
  - SJF (Shortest Job First) — optimal for minimum average waiting time, starvation risk
  - SRTF (Shortest Remaining Time First) — preemptive SJF version
  - Round Robin (RR) — cyclic service with time quantum
  - Priority Scheduling — priority-based routing, starvation solution with aging
  - Multilevel Queue & Multilevel Feedback Queue (MLFQ) — multiple queues with dynamic process movement

---

## UNIX Laboratory

### 1. Introduction to UNIX and Linux Terminal Basics
- **UNIX Philosophy**
  - Everything is a file (regular, directories, devices, connections)
  - Do one thing and do it well (small, specialized tools)
  - Chaining programs (combining programs with pipes)
- **User Accounts & Properties**
  - Username, Password (`/etc/shadow`), UID (Root is 0), GID, Home Directory, Default Shell
  - Filesystem: Root (`/`), `/bin` (binaries), `/etc` (config), `/home`, `/root`, `/tmp`
  - Shell Prompt (`$` for user, `#` for root)
- **Basic Commands**
  - `passwd` — change password
  - `date` — display/format date and time
  - `cal` — display calendar (current month, year, specific month)
  - `who`, `whoami`, `who am i` — logged-in user information

### 2. UNIX File System Navigation
- **File Types in UNIX**
  - Regular files (`-`), Directories (`d`), Symbolic links (`l`), Character devices (`c`), Block devices (`b`)
- **File Paths (Pathnames)**
  - Absolute pathnames (start from root `/`)
  - Relative pathnames (start from current directory, `.` for current, `..` for parent, `~` for home)
- **Directory Navigation and Management**
  - `pwd` — display current directory (print working directory)
  - `cd` — change directory (`cd ~` for home, `cd -` for previous, `cd ..` for parent)
  - `mkdir` — create directory (parameter `-p` for parent directory creation)
  - `rmdir` — delete empty directory

### 3. UNIX File and Directory Management
- **Copying, Moving & Deleting**
  - `rm` — delete files (`-r` for recursive directory deletion, `-f` for force)
  - `cp` — copy files (`-r` for directories, `-i` for confirmation)
  - `mv` — move or rename files/directories
- **Content Viewing**
  - `ls` — list directory files
  - `ls` parameters: `-l` (long format, details), `-a` (all files, including hidden ones starting with `.`), `-R` (recursive), `-t` (sort by modification time), `-S` (sort by size)

### 4. UNIX Access Permissions
- **Permissions Model**
  - Three categories: Owner/User (`u`), Group (`g`), Others (`o`), All (`a`)
  - Three types: Read (`r`), Write (`w`), Execute (`x`)
  - Symbolic representation (e.g., `rwxr-xr--` -> 9 characters)
- **Directory Permissions**
  - `r` (Read) — list directory files (`ls`)
  - `w` (Write) — create/delete files in directory
  - `x` (Execute) — enter/access directory (`cd`, executing files within it)
- **Changing Permissions & Ownership**
  - `chmod` — modify permissions
    - Symbolic method (e.g., `chmod u+x,g-w file`)
    - Octal / Numeric method (e.g., `chmod 755 file` -> `rwxr-xr-x`, 4=read, 2=write, 1=execute)
  - `chown` — change file owner (requires root permissions)
  - `chgrp` — change file group
  - `umask` — set default permissions for new files/directories (e.g., `umask 022`)

### 5. UNIX File Viewing and Linking
- **File Content Viewing**
  - `cat` — concatenate and display file
  - `more` & `less` — paginated viewing (`less` allows backward navigation/search)
  - `head` — display first N lines (default 10, parameter `-n`)
  - `tail` — display last N lines (`-f` for real-time monitoring)
- **File Analysis**
  - `wc` — count lines (`-l`), words (`-w`), and characters (`-c`/`-m`)
  - `file` — recognize file type/content
- **File Links**
  - Hard Links (`ln file link`) — point to same inode, cannot cross filesystems, cannot point to directories
  - Symbolic Links / Soft Links (`ln -s file link`) — point to path name (shortcut), can point to directories and cross filesystems

### 6. UNIX I/O Redirection and Pipes
- **Standard I/O Streams**
  - Standard Input (stdin, fd 0) — keyboard
  - Standard Output (stdout, fd 1) — screen
  - Standard Error (stderr, fd 2) — screen (separate error channel)
- **Redirection**
  - `>` — redirect stdout to file (overwrite)
  - `>>` — redirect stdout to file (append)
  - `2>` — redirect stderr to file (overwrite)
  - `2>>` — redirect stderr to file (append)
  - `&>` or `> file 2>&1` — redirect stdout and stderr to same file
  - `<` — redirect stdin from file
- **Pipes**
  - `|` — connect stdout of one command to stdin of another (e.g., `ls | wc -l`)

### 7. UNIX Wildcards and Glob Patterns
- **Globbing Patterns**
  - `*` — matches any number of characters (including none)
  - `?` — matches exactly one any character
  - `[...]` — matches any single character within brackets (e.g., `[a-z]`, `[0-9]`)
  - `[!...]` or `[^...]` — matches any character outside those in brackets
- **Special Cases & Gotchas**
  - Glob patterns don't match hidden files (starting with `.`) unless explicitly specified (e.g., `.*`)
  - Expansion is done by the shell before command execution
- **Escaping**
  - Using backslash (`\`) or quotes (`'`, `"`) to disable special wildcard meaning