# Operating Systems — Chapter 1: Introduction

The first chapter introduces the fundamental concepts of Operating Systems (OS): their definition, the components of a computer system, their historical evolution from serial processing to modern distributed systems, and the basic features for multiprogramming and time-sharing. It constitutes the necessary foundation for all subsequent chapters on processes, memory management, and scheduling.

---

## 1. Definition of the Operating System

### 1.1 What is an OS

An Operating System (OS) is a program that acts as an **intermediary** between the users of the Computer System (CS) and its hardware.

**Goals of an OS:**
- Execution of user programs
- Ease of use of the CS
- Effective / efficient use of hardware and peripherals
- Protection of programs and data of different users

### 1.2 Attempts at Definition

| Approach | Description | Example |
| :--- | :--- | :--- |
| Extended machine (extended/virtual machine) | Hides from the user/programmer the complexity of the hardware | Simplified file/directory management, interrupt handling |
| Resource allocator | Distributes the system's resources among applications | Correct print order of a shared printer, memory management & protection in multiuser environments |

### 1.3 Final Definition

The OS is ultimately defined as a combination of:
- **Resource allocator**
- **Control program**: controls the execution of user programs and the operation of I/O devices
- **Kernel**: the only program that runs **continuously** while the CS is in operation — everything else is additional services or applications

> **[Key Insight]** The Kernel is the core of the OS — it never terminates during system operation. Anything executed outside the kernel is considered a user application.

---

## 2. Components of Computer Systems

A CS consists of four layers:

1. **Hardware:** Provides the basic computing resources — CPU, memory, I/O devices.
2. **Operating System:** Controls and coordinates the use of hardware among application programs and users.
3. **Application Programs:** Define the ways of using resources to solve computing problems (e.g., compilers, DBMS, business applications).
4. **Users:** Humans, machines, other computers.

**Typical CS hardware includes:** CPU, disk controller, USB controller, graphics adapter, memory, disks, mouse, keyboard, printer, monitor.

---

## 3. Historical Evolution of OS

### 3.1 Evolution I — Serial Processing (early 1940s – mid 1950s)

There was no OS. Users interacted directly with the hardware.

**Problems:**
- **Scheduling:** Waste of time, programs that stalled halfway due to a large block of time
- **Setup time:** A single program (job) loaded the compiler + the high-level program, stored the object code, loaded it and linked it with libraries — a time-consuming process

### 3.2 Evolution II — Simple Batch Systems / Batch Process (early–mid 1960s)

**Reason for development:** Very expensive machines → reduction of idle time.

**Central idea — Monitor:**
- Software that controls the programs being executed
- Groups jobs together (batching)
- Permanently resident in main memory
- After the end of each job, control returns to the monitor

**Job Control Language (JCL):** Command language addressed to the monitor (which compiler, which data).

**Required hardware features for the Monitor:**

| Feature | Purpose |
| :--- | :--- |
| Memory protection | Prevention of modification of the monitor's area by the user program |
| Timer | Avoidance of system monopolization by a single job |
| Privileged instructions | Executed only by the monitor, mainly for I/O |
| Interrupts | Mechanisms for granting/reclaiming control |

### 3.3 Evolution III — Multiprogrammed Batch Systems (1965–1980)

**Reason for development:** The processor remained idle due to the speed difference with I/O devices.

**Problem of uniprogramming:** When a job waited for I/O, the CPU remained idle.

**Example of waste:**
```
Read one record from file   →  0.0015 sec
Execute 100 instructions    →  0.0001 sec
Write one record to file    →  0.0015 sec
TOTAL                       →  0.0031 sec
CPU Utilization = 0.0001 / 0.0031 ≈ 3.2%
```

**Solution — Multiprogramming:**
- Partitioning of memory into segments, one for each process
- When a process waits for I/O, the CPU serves another process
- Possibility of using the CPU up to 100%
- **Requirement:** protection against memory overlaps through hardware

**OS features for multiprogramming:**

| Function | Description |
| :--- | :--- |
| Memory management | Splitting of memory into segments, protection of each segment from interference |
| Process management | Selection of which processes acquire space in memory |
| CPU scheduling | Selection of which loaded process is executed from those in memory |
| Resource allocation | Avoidance of interaction between executing processes |

**OS performance measures:**
- Average resource utilization
- Throughput
- Response time

**Foundations of multiprogrammed systems:**
- Hardware features (interrupts, I/O, DMA)
- Memory management
- Scheduling algorithms

### 3.4 Time-Sharing Systems

**Arose** from user complaints about waiting hours/days for results from batch systems.

**Operating principle:**
- Each user connects through a terminal
- The CPU serves each user program in turn with a short **quantum** or computational **burst**
- Exploits the relatively slow human reaction time for the illusion of parallel service

**Comparison of Multiprogramming vs Time-Sharing:**

| Criterion | Multiprogramming | Time-Sharing |
| :--- | :--- | :--- |
| Goal | Maximization of processor usage | Minimization of response time |
| Command input | Via Job Control Language (JCL) | Directly from a terminal |
| Job type | Batch jobs | Interactive users |

### 3.5 Evolution IV — Fourth Generation (1980–1990)

- Appearance of **LSI** type integrated circuits
- User-friendly OS
- **Network OS:** each computer runs its own OS
- **Distributed OS:**
  - Appear as traditional single-processor systems
  - Users do not care where their programs are executed or where their files are located
  - Allow execution on different processors simultaneously
  - Require complex scheduling algorithms
- **Real-time systems** (e.g., airline reservations)

### 3.6 Modern Developments (1990+)

**1990–2000:**
- Leaps in hardware performance (MIPS)
- World Wide Web → increase in distributed processing, need to integrate web-based processes
- Establishment of object-oriented technology
- Spread of open-source technology
- Emergence of **Linux**

**2000+:**
- **Middleware:** software that connects two separate applications, often over a network
- **Web services:** applications published on the Internet through high-speed connections
- Improved network architectures + increase in parallel processing
- **POSIX** (Portable Operating System Interface): OS standardization
- Computing on portable devices (PDA, mobile phones)

---

## 4. OS and CS Architecture

- OS have a relationship of **dependence** with the architecture of CS
- Hardware developments enabled new functions → led to OS evolution
- Initially: only one process is executed at a time (e.g., DOS)

---

## 5. Course Material

### Theory
- Introduction (basic concepts)
- Purposes of operating systems
- Processes
- OS architectures (microkernel, threads, parallel systems)
- Mutual exclusion
- Deadlock
- Memory management
- Virtual Memory
- Process scheduling

### Laboratory (Unix)
- User accounts — System login
- File system — Path names
- Navigation of the file system
- File management
- File attributes
- I/O redirection
- Multiprogramming in Unix

---

## Exam Tip: Key Distinctions for the Exam

1. **Kernel vs OS:** The kernel is the only program that always runs — it is not identical to the entire OS.

2. **Uniprogramming vs Multiprogramming:** The key is CPU usage during I/O wait. In uniprogramming the CPU remains idle; in multiprogramming it executes another process.

3. **Multiprogramming vs Time-Sharing:** Multiprogramming = maximization of CPU usage (batch). Time-sharing = minimization of response time (interactive).

4. **Historical milestones:** Serial (1940s) → Batch/Monitor (1960s) → Multiprogramming (1965–1980) → Time-Sharing → LSI/Distributed (1980–1990) → Linux/Internet (1990+) → POSIX/Mobile (2000+).

5. **CPU Utilization calculation:** $\text{CPU Util} = \frac{t_{\text{CPU}}}{t_{\text{total}}}$ — in the slide example: $\frac{0.0001}{0.0031} \approx 3.2\%$ for uniprogramming with an I/O-bound job.
