---
# OS_Lec01_NOTES.md
---

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

---
# OS_Lec02_NOTES.md
---

# Operating Systems — Chapter 2: Purposes and Evolution of OS

This chapter covers the four basic purposes of an Operating System (OS): hardware protection, communication with the user, resource management, and evolvability. It additionally examines the important evolution points of OS (processes, memory, security, scheduling, structure) and the features of modern OS. The material belongs to the Department of Informatics & Telecommunications Technology, TEI of Epirus.

---

## 1. Purposes and Functions of OS

OS implement four central purposes:

| #   | Purpose                                 | Summary                                                              |
| :-- | :-------------------------------------- | :------------------------------------------------------------------ |
| I   | Hardware protection                     | dual-mode, I/O, memory, CPU                                         |
| II  | Communication with the user             | abstraction of complexity, provision of services                    |
| III | Management, utilization and control of resources | controlled allocation of CPU, memory, I/O                  |
| IV  | Evolvability and ease of evolution      | support for new hardware, new services, fixes                       |

---

## 2. I. Hardware Protection

### 2.1 Dual-Mode Operation

Shared resources require the OS to ensure that an erroneous program will not affect other programs.

The OS supports **two modes of operation**:

- **User mode** — execution on behalf of the user.
- **Monitor mode** (= supervisor mode = system mode) — execution on behalf of the OS.

**Mode bit mechanism:**

- A bit in hardware indicates the current state: `0` = monitor, `1` = user.
- At every interrupt or fault the hardware automatically switches to **monitor mode**.
- **Privileged instructions** are executed **only** in monitor mode.

```
      Interrupt / fault
monitor ←────────────── user
        ──────────────→
         set user mode
```

> **[Key Insight]** The user/monitor mode distinction is the fundamental mechanism on which every other form of protection (I/O, memory, CPU) is based.

### 2.2 Kernel Protection

- The **mode register bit** indicates whether the CPU is executing a user program or is in **kernel mode**.
- Certain instructions and data accesses are possible **only in kernel mode**.
- Main memory is divided into regions: OS code, OS data, Program A, Program B, code library.

### 2.3 I/O Protection

- **All** I/O instructions are privileged.
- It is ensured that a user program cannot gain control of the computer in monitor mode (e.g., it cannot modify the **interrupt vector table**).

**Execution of I/O operations by a user program (System Call flow):**

1. The user program issues a **system call** — usually through a **trap** to a designated location of the interrupt vector.
2. Control passes through the interrupt vector to an OS **service routine**; the mode bit is set to monitor mode.
3. The monitor verifies the parameters, performs the request.
4. It returns control to the instruction after the system call (user mode).

### 2.4 Memory Protection

Two registers are used that define the acceptable address range for each program:

| Register            | Content                                  |
| :------------------ | :--------------------------------------- |
| **base register**   | Smallest acceptable physical memory address |
| **limit register**  | Size of the acceptable memory region     |

- Memory outside `[base, base + limit)` is **protected**.
- In monitor mode the OS has **unrestricted** access to the entire memory.
- The `load` instructions for the base & limit registers are **privileged**.

**Conversion of logical → physical address:**

```
CPU address → [base ≤ address ≤ base+limit] → YES → memory access
                                             → NO  → trap to OS (addressing error)
```

### 2.5 CPU Protection

- **Timer:** interrupts the computer after a specified period, ensuring that the OS retains control.
  - Decremented by 1 at every **clock tick**.
  - When it reaches **0** → an interrupt is generated.
- Used in **time-sharing** systems and for computing the current time.
- Loading the timer is a **privileged instruction**.

> **[Exam Tip: Privileged Instructions]** In exams the question "which instructions are privileged?" is common. Answer: **I/O instructions**, **load base/limit**, **load timer**, **switching the mode bit**. No user program can execute them directly.

---

## 3. II. Communication with the User

### 3.1 Abstraction Layers

The OS intervenes between hardware and user hiding complexity:

```
End User / Programmer
     ↕
Application Programs
     ↕
Utilities (compilers, editors, interpreters)
     ↕
Operating System
     ↕
Computer Hardware
```

- **Hardware level:** Machine language, Microprogramming, Physical devices.
- **OS:** Runs in **kernel mode**. Hides hardware details from the programmer.
- **Compilers/Interpreters/Shell:** Run in **user mode**.

### 3.2 Microprogramming

- **Microprogram:** an interpreter that receives machine language instructions (`ADD`, `MOVE`, `JUMP`) and translates them into small steps.
- Stored in **ROM memory**.
- The instruction set it interprets = **Machine Language** (not part of the hardware).
- Typical size of a machine language: **50–300 instructions**.

### 3.3 OS Kernel

The part of the OS that contains the **most frequently used functions** and other OS parts currently in use, all in **main memory**.

### 3.4 Provided Services

The OS provides users with:

- Program development
- Program execution
- Access to I/O devices
- Controlled access to files
- Access system
- Error detection and concealment
- Accounting (usage statistics)

---

## 4. III. Resource Management

The OS provides **controlled allocation** of processors, memories, and I/O devices among competing programs.

**Control Mechanism:**

- The OS operates as ordinary software but with a different purpose.
- Directs the processor in the use of other resources.
- Allocates and **reclaims** control of the processor.

---

## 5. IV. Evolvability and Ease of OS Evolution

| Category              | Examples                                                   |
| :-------------------- | :--------------------------------------------------------- |
| Hardware upgrades     | Paging of memory segments, graphics terminals              |
| New services          | Use of windows, statistical tools                          |
| Fixes                 | Bug fixes, updates                                         |

---

## 6. Important Evolution Points of OS

Five central evolution axes:

1. Processes
2. Memory management
3. Protection and security of information
4. Scheduling and resource management
5. System structure

---

## 7. I. Processes

### 7.1 Definitions

- **Process:** A program or instance of a program executing on a computer.
- **Alternative definition:** The entity that can be assigned to and executed on a processor.

### 7.2 Process Table

- Information about each process is stored in a **process table** — a **linked list** structure with the processes as nodes.
- A **suspended process** consists of:
  - **Its address space** — the memory image.
  - **Its information** — an entry in the process table.

### 7.3 Process Memory Organization

Each memory block of a process contains:

- The executable program (code)
- The data required (data)
- The **execution context** (process state)
- Management information from the OS (e.g., priority)
- Processor information (e.g., register contents, program counter)

### 7.4 Process Management

- Each process is registered in a **process list** maintained by the OS.
- The **process index register** points to the process that has control at that moment.
- Interrupted processes store their register contents in their own execution context.
- **Context switch:** saving the information of the current process + loading the next process.
- A process is either **running** or **waiting**.

### 7.5 Causes of Fault Creation

| Cause                              | Description                                                                               |
| :--------------------------------- | :---------------------------------------------------------------------------------------- |
| Inaccurate synchronization         | Interrupt signals are not handled correctly by the signaling mechanism                   |
| Failed mutual exclusion            | Simultaneous access to a shared resource by many users / programs                         |
| Undefined program behavior         | Programs interfere by rewriting common memory regions · dependence on scheduling order   |
| Deadlocks                          | Two or more programs mutually wait for each other to release a resource                  |

> **[Key Insight]** Process faults appear only after **rare and specific sequences of actions**, which makes them extremely difficult to locate. Detecting a fault **does not** automatically define its cause.

---

## 8. II. Memory Management

### 8.1 Five Basic OS Responsibilities

| Responsibility                             | Summary                                                          |
| :------------------------------------------ | :-------------------------------------------------------------- |
| Process isolation                           | Each process in a separate, protected space                    |
| Automatic placement & management            | Memory bounds, memory map                                      |
| Support for modular programming             | Dynamic memory allocation / management                         |
| Access protection & control                 | Prohibition of unauthorized access                            |
| Long-term storage                           | Retention of data beyond the lifetime of a process             |

Implemented through: **Virtual Memory** and **File System**.

### 8.2 Virtual Memory

- Allows programs to address physical memory **logically**, independently of the available size.
- Addresses the requirement of multiple jobs to reside **simultaneously** in main memory.

### 8.3 Paging

- Memory is divided into **pages** of fixed size (e.g., 4 KB).
- Each page can be placed **anywhere** in main memory.
- Each program references a **virtual address** → the paging system converts it into a **real address**.
- Pages that are not in main memory are brought from **secondary** storage (disk) — all pages are kept on disk.

**Addressing flow:**

```
Processor → Virtual Address → Memory Management Unit (MMU)
                                    ↓
                          Real Address → Main Memory
                                    ↓ (page fault)
                          Disk Address → Secondary Memory
```

- Each process acquires **unique, non-overlapping** virtual memory → **isolation**.
- Partial page loading **minimizes** the holding of main memory.

> **[Exam Tip: Virtual vs Physical Address]** The processor always issues **virtual** addresses. The conversion to physical addresses is done by the **MMU** (Memory Management Unit) in cooperation with the OS. If the page is not loaded → **page fault** → the OS loads it from disk.

---

## 9. III. Protection and Security of Information

| Mechanism                       | Purpose                                                                            |
| :------------------------------ | :--------------------------------------------------------------------------------- |
| **Access control**              | Regulating user access to the system                                              |
| **Information flow control**    | Regulating the flow of data in the system                                         |
| **Authentication**              | Verifying that security mechanisms are executed according to security policies    |

---

## 10. IV. Scheduling and Resource Management

### 10.1 Scheduling Criteria

- **Fairness** — priority classes.
- **Differential response** — dynamic scheduling decisions.
- **Efficiency:**
  - Maximization of throughput
  - Minimization of response time
  - Service of many users

### 10.2 Multiprogramming

The OS maintains multiple **queues**:

| Queue                      | Content                                                            |
| :------------------------- | :----------------------------------------------------------------- |
| **Short-term queue**       | Processes in main memory, ready to be executed                    |
| **Long-term queue**        | New processes waiting to use the processor                        |
| **I/O device queues**      | Processes waiting for an I/O device                               |

**Short-term scheduler (dispatcher)** — selection strategies:
- **Round-robin**
- **Priority levels**

---

## 11. V. System Structure

### 11.1 Problems from OS Size Increase

- Delayed delivery
- Non-obvious programming errors
- Reduced performance

### 11.2 Design Trends

- **Modular design**
- Minimization of the interface between parts
- Use of **layered architecture**

### 11.3 OS Design Hierarchy

Each level:
- Performs a **subset** of functions.
- Relies on the previous one for primitive operations.
- Provides services to the higher level.

The **lowest** levels operate on a smaller time scale, interacting directly with the hardware.

**Hierarchy (from lowest to highest):**

| Level | Name                  | Objects                                           | Example Operations                              |
| :---- | :-------------------- | :------------------------------------------------ | :---------------------------------------------- |
| 1     | Electronic circuits   | Registers, gates, buses, etc.                     | Clear, transfer, activate, complement           |
| 2     | Instruction set       | Evaluation stack, microprogram interpreter, scalar/array data | Load, store, add, subtract, branch   |
| 3     | Procedures            | Procedure call stack, display                     | Mark stack, call, return                        |
| 4     | Interrupts            | Interrupt-handling programs                       | Initiate, mask, unmask, retry                   |
| 5     | Primitive processes   | Primitive processes, semaphores, ready list       | Suspend, resume, wait, signal                   |
| 6     | Local secondary store | Blocks of data, device channels                   | Read, write, allocate, free                     |
| 7     | Virtual memory        | Segments, pages                                   | Read, write, fetch                              |
| 8     | Communications        | Pipes                                             | Create, destroy, open, close, read, write       |
| 9     | File system           | Files                                             | Create, destroy, open, close, read, write       |
| 10    | Devices               | External devices (printers, displays, keyboards)  | Open, close, read, write                        |
| 11    | Directories           | Directories                                       | Create, destroy, attach, detach, search, list   |
| 12    | User processes        | User processes                                    | Quit, kill, suspend, resume                     |
| 13    | Shell                 | User programming environment                      | Statements in shell language                    |

---

## 12. Features of Modern OS

### 12.1 Hardware Evolution

- Many processors (multi-processor)
- High-speed network connections
- Many and large-capacity storage devices

### 12.2 Software Evolution

- Multimedia applications
- Internet access
- Client/server model

### 12.3 OS Architecture Evolution

| Feature                                  | Summary                                                          |
| :--------------------------------------- | :--------------------------------------------------------------- |
| Microkernel architecture                 | Minimal kernel · services in user space                        |
| Multithreading                           | Many threads within a single process                            |
| Multiprocessing systems                  | Many processors in a common system                              |
| Parallel systems                         | Simultaneous execution of computations                           |
| Real-time systems                        | Guaranteed response times                                       |
| Distributed systems                      | Many nodes that appear as a single system                       |

---

## Solved Exercises

### Exercise 1: Dual-Mode Operation — What happens on an interrupt

**Problem:** A user program is executing (mode bit = 1). A hardware interrupt occurs. Describe step by step what happens.

**Solution:**
1. The hardware detects the interrupt.
2. The hardware automatically sets the mode bit to `0` (monitor mode).
3. Control is transferred through the **interrupt vector table** to the relevant OS service routine (ISR).
4. The OS (monitor mode) executes the ISR.
5. Upon completion, the OS sets the mode bit = `1` (user mode) and returns control to the program.

---

### Exercise 2: Memory Protection — Bounds Checking Example

**Problem:** base register = 300040, limit register = 120900. Is access to address 400000 acceptable? And to address 250000?

**Solution:**
- Acceptable range: `[300040, 300040 + 120900)` = `[300040, 420940)`.
- Address 400000: `300040 ≤ 400000 < 420940` → **ACCEPTABLE**.
- Address 250000: `250000 < 300040` → **NOT ACCEPTABLE** → trap to the OS (addressing error).

---

### Exercise 3: System Call for I/O

**Problem:** A user program wants to read data from disk. Why can it not execute an I/O instruction directly and how does it achieve it?

**Solution:**
1. I/O instructions are **privileged** → they are executed only in monitor mode.
2. The user program executes a **system call** (trap) with the appropriate parameters.
3. The trap redirects control to the OS (monitor mode) through the interrupt vector.
4. The OS verifies the parameters and executes the I/O instruction.
5. The result is returned to the program · mode bit → user mode.

---

### Exercise 4: Paging — Virtual to Physical Conversion

**Problem:** Page size 4 KB. A process references virtual address 0x00005A00. How are the page number and the offset computed?

**Solution:**
- Page size: $4096 = 2^{12}$ bytes → the **12 LSB** of the address are the offset.
- Virtual address: `0x00005A00` = `0b 0000 0000 0000 0000 0101 1010 0000 0000`
- Page number: the bits 12 and above = `0x5` = page 5.
- Offset: the 12 LSB = `0xA00` = 2560 (bytes within the page).
- The MMU consults the page table for page 5 → finds the physical page → adds the offset → physical address.

---

### Exercise 5: Deadlock — Scenario Recognition

**Problem:** Process A holds resource R1 and waits for R2. Process B holds R2 and waits for R1. What happens?

**Solution:**
1. A holds R1, waits for R2.
2. B holds R2, waits for R1.
3. No process can proceed without the other releasing the resource.
4. **Deadlock** — the system needs intervention (e.g., termination of a process or resource preemption).

---

### Exercise 6: OS Hierarchy — Classification of Functions

**Problem:** At which hierarchy level do the following functions belong: (a) file storage, (b) interrupt handling, (c) user process creation, (d) shell command invocation?

**Solution:**

| Function              | Level | Name          |
| :-------------------- | :---- | :------------ |
| (a) File storage      | 9     | File system   |
| (b) Interrupt handling | 4    | Interrupts    |
| (c) Process creation  | 12    | User processes |
| (d) Shell command     | 13    | Shell         |

---

## Exam Tip: Key Concepts for Exams

**1. Dual-mode & Privileged Instructions:**
Privileged instructions are: I/O instructions, loading base/limit registers, loading the timer, modifying the mode bit. None is executed in user mode.

**2. System Call vs Interrupt:**
- **Interrupt:** asynchronous event from hardware.
- **System Call (trap):** synchronous request from software for an OS service.
Both lead to a transition from user → monitor mode.

**3. Base/Limit Registers:**
If `address < base` or `address ≥ base + limit` → **addressing error** → trap to the OS.

**4. Context Switch:**
Save: PC, registers, process state in the process table. Load: the corresponding items of the next process.

**5. Paging:**
`virtual address = (page number, offset)`. The MMU converts the page number to a physical frame number through the page table. Page fault = the page is not in main memory.

**6. Deadlock — 4 Coffman Conditions (Supplementary):**

> **[Supplementary]**
> A deadlock occurs only when the 4 Coffman conditions hold **simultaneously**:
> 1. **Mutual Exclusion** — the resource is used exclusively.
> 2. **Hold and Wait** — the holder holds a resource and waits for another.
> 3. **No Preemption** — resources cannot be forcibly removed.
> 4. **Circular Wait** — a circular chain of waiting among processes.

---
# OS_Lec03_NOTES.md
---

# Operating Systems — Chapter 3: Processes

## What is a process
- A process = a program in execution.
- It is also an asynchronous activity monitored by the operating system.
- The operating system associates each process with a data structure, the process descriptor or Process Control Block (PCB).
- Analogy: the program is like a musical score, while the process is the actual performance of the "piece".

## Process address space
Each process has its own address space, which includes:
- **Text region**: the executable code.
- **Data region**: variables and dynamically allocated memory.
- **Stack region**: local variables and information of active procedure calls.

## Why process management is critical
- It is a core subject of every operating system.
- The OS maintains for each process information about:
  - its state,
  - the resources it holds,
  - the way in which it can control it.
- The OS must:
  - interleave the execution of many processes,
  - maximize CPU utilization,
  - minimize response time,
  - allocate resources with a policy that avoids deadlocks,
  - support communication and creation of processes.

## Basic process states
### 3 basic states
- **Running**: the process is executing on the CPU.
- **Ready**: it is ready to execute, but waiting for the CPU.
- **Blocked**: it cannot continue until some external event occurs.

### Extended model
- **New**: just created.
- **Exit**: completed and released by the OS.

## State transitions
Important transitions:
- **New → Ready**: the process is admitted into the system when allowed by the system limits.
- **Running → Ready**: it exhausts the allowed execution time limit.
- **Running → Blocked**: it requests a service/I/O that cannot be performed immediately.
- **Blocked → Ready**: the event it was waiting for completes, e.g., I/O.
- **Running → Exit**: process termination.

## Dispatcher and time quantum
- New processes enter the ready list.
- When the CPU becomes available, the **dispatcher** assigns the first suitable process for execution.
- So that the CPU is not monopolized, the OS uses a timer interrupt.
- The predefined execution time interval is called the **time quantum**.
- If the quantum expires without the process surrendering the CPU on its own, the OS moves it from Running to Ready and gives the CPU to another process.
- If it requests I/O before the quantum expires, it transitions to Blocked.

## Suspended processes
When main memory is insufficient or when better resource utilization is required:
- some processes are moved to disk,
- two additional states are created:
  - **Blocked/Suspend**
  - **Ready/Suspend**

This is used because the processor is much faster than the I/O devices and a situation can arise where many processes wait for I/O.

## Schedulers
The OS uses different schedulers:
- **Long-term scheduler (job scheduler)**:
  - selects which processes will enter the ready queue,
  - controls the degree of multiprogramming.
- **Short-term scheduler (CPU scheduler)**:
  - selects which process will be executed next on the CPU.
- **Medium-term scheduler**:
  - used particularly in time-sharing systems,
  - periodically moves processes to/from memory.

## Process queues
Processes are organized into queues such as:
- **Ready queue**: processes ready for the CPU.
- **Blocked queue**: processes waiting for an event or completion of I/O.

The scheduler selects processes from these queues.

## PCB — Process Control Block
### Role
- When a new process is created, the OS assigns it a unique **PID**.
- It then creates the **PCB**.
- The PCB contains all the necessary information for managing and controlling the process.
- It is a basic part of the process image together with the program, data, and stack.

### Important idea
- The process image is not necessarily stored in contiguous memory locations.
- At a given moment, part of it may reside in main memory and another part in secondary storage.

## Process table
- The OS implements a **process table**.
- There is one entry for each process.
- The entries store its state so that it can continue after an interrupt or a switch.

## Fields stored for a process
### 1. Process management
- Registers
- Program Counter
- Program status word
- Stack pointer
- Process state
- Process start time
- CPU time used
- CPU time of child processes
- Time of next wakeup
- Message queue pointer

### 2. Memory management / identity
- Pointer to text segment
- Pointer to data segment
- Exit status
- Signal status
- Process identity
- Parent process
- Process group
- Real and effective user/group identity
- Bitmap for signals

### 3. File management
- Permission mask
- Root path
- Working path
- File descriptors
- Effective user and group identity
- System call parameters
- Various indicators

## Process change and context switch
### Reasons for switching the executing process
- Clock interrupt: exhaustion of the time quantum.
- I/O interrupt.
- Memory fault.
- Trap.
- System call, e.g., opening a file.

### What the OS does on a state change
When a process leaves the Running state:
1. It saves the processor context in the PCB (PC and other registers).
2. It moves the PCB to the appropriate queue.
3. It selects a new process for execution.
4. It updates the PCB of the new process.
5. It updates memory management structures.
6. It restores the saved context of the new process.

### Context switch
- The CPU saves the state of the old process and loads that of the new one.
- This time is **overhead**: no useful work is produced.
- The cost depends on the hardware support.

## OS services for processes
- Multiprogrammed OS provide system calls for process management.
- These services can be activated:
  - directly, through supervisor calls within the code,
  - indirectly, through terminal commands that are translated into system calls.
- Although OS differ in design, they provide a similar basic set of functions for processes.

## Process creation
When the OS creates a new process:
- it creates the necessary data structures,
- allocates memory to it,
- admits it into the system.

### Common causes of creation
- Submission of a new job.
- Login of a new user.
- Service request from an application.
- Creation by an existing process.

## Unix: fork, exec, exit, wait
### fork()
- Creates a new child process as a clone of the parent.
- The child:
  - has a virtual copy of the parent's virtual memory,
  - initially executes the same program,
  - starts with the same register values.

### exec()
- Replaces the memory image of the calling process with a new program.
- Transfers control to the new program.

### exit(status)
- Terminates the process.

### wait(&status)
- The parent process waits for the termination or another state change of a descendant.

## Possible exam questions
1. What is a process and how does it differ from a program?
2. What are the basic process states?
3. What causes the Running → Ready and Running → Blocked transitions?
4. What is the role of the dispatcher?
5. What is the PCB and what data does it contain?
6. What is a context switch and why is it considered overhead?
7. What is the difference between the long-term, short-term, and medium-term scheduler?
8. What is the relationship of fork(), exec(), exit(), wait() in Unix?

## Short summary for revision
- Process = a program in execution with its own address space and PCB.
- Basic states: New, Ready, Running, Blocked, Exit, and in some models Suspend states.
- The OS uses a scheduler, dispatcher, queues, and time quanta to share the CPU.
- The PCB and the process table hold all the necessary information for restarting/continuing a process.
- Process switching requires a context switch, which has a cost.
- In Unix, the creation/execution/termination cycle is closely linked with fork(), exec(), wait(), exit().

---
# OS_Lec04_NOTES.md
---

# Operating Systems Architectures (Chapter 4)

This chapter covers the main architectures with which modern Operating Systems (OS) are designed and implemented. Eight architectural categories are examined — from monolithic systems to distributed ones — with emphasis on the features, advantages, and weaknesses of each approach. Understanding them is fundamental for the study of systems software design and the management of computing resources.

---

## 1. Monolithic Systems

### Definition and Features

Monolithic systems constitute the simplest OS architecture: **there is no internal structure or separation**. The entire OS is a collection of procedures where each one can call any other directly.

- Communication between procedures is done through **parameters**.
- Each procedure is **visible** to any other (there is no information hiding).

### Structure of Monolithic Organization

| Component | Role |
| :--- | :--- |
| Main program | Requests the invocation of service procedures |
| Service procedures | Implement the system calls |
| Utility programs | Support the service procedures |

### System Call Implementation

In monolithic systems, the system call follows the following steps:

1. The user program creates a **trap** to the kernel — a special instruction or kernel call is executed.
2. The OS determines the **service number** requested.
3. The OS locates and calls the **service procedure**.
4. Control is **returned** to the user program.

> **[Key Insight]** The absence of structure makes monolithic systems fast (no additional layers), but difficult to maintain and vulnerable: a fault anywhere can bring down the entire system.

---

## 2. Layered Architecture

### Definition and Operating Principle

Layered architecture improves design by grouping components that implement **similar functions** into layers. Each layer communicates **only with its neighbors** (above and below).

### Layer Structure

| Layer | Function | Space |
| :--- | :--- | :--- |
| Layer 4 | User Applications | User space |
| Layer 3 | I/O Management | Kernel space |
| Layer 2 | Message Interpreter | Kernel space |
| Layer 1 | Memory Management | Kernel space |
| Layer 0 | Processor Allocation & Process Scheduling | Kernel space |

### Advantages and Disadvantages

**Advantages:**
- Clear organization and modular design.
- Ease of error detection — each layer is tested independently.

**Disadvantages:**
- The requirements of processes **cross many layers** before completing → increased delay.
- **Throughput** can be lower compared to monolithic systems.
- Additional methods are required for **data transfer and control**.

---

## 3. Microkernel Architecture

### Definition

The **microkernel** assigns minimal functions to the kernel and moves the rest to **servers** running in user mode.

| Component | Location | Example |
| :--- | :--- | :--- |
| IPC, Memory management, Synchronization | Kernel space | Kernel |
| File system, Process scheduler, Device manager | User space | Servers |
| Applications | User space | User applications |

### Operating Mechanism

1. The user process (**client process**) sends a request to the server process.
2. The server performs the function and returns a response.
3. The **microkernel** manages the communication through **IPC (Inter-Process Communication)**.

### Ways of Resolving Limitations

- **Solution 1:** Critical servers run in kernel mode with full access to the hardware, but continue to communicate with the other processes.
- **Solution 2:** A basic mechanism is added to the kernel, but the **decision policy** remains with the servers.

### Microkernel Advantages

| Advantage | Explanation |
| :--- | :--- |
| Extensibility | Addition/removal of services without recompiling the kernel |
| Portability | Changes for a new processor are made only in the microkernel |
| Object-oriented design | The components are objects with clear interfaces |
| Reliability | Small kernel size → possibility of accurate testing |

> **[Key Insight]** The Linux kernel is **monolithic** (but modular), while MINIX and QNX use a microkernel architecture. The choice directly affects performance and security.

---

## 4. Threads — Multithreading

### Definition of a Thread

A **thread** is the smallest unit of instruction execution on the processor. It includes:
- **Program Counter**
- **Stack Pointer**
- **Its own data region**

A **process** is a collection of threads together with the associated system resources.

### Threads vs Processes

| Feature | Process | Thread |
| :--- | :--- | :--- |
| Address space | Private | Shared (within a process) |
| Data / Code / Files | Private | Shared |
| Creation cost | High (kernel call) | Low (user space) |
| Context switch cost | High | Low |
| Communication/Synchronization | Kernel call | Variable monitoring |

### User-Level Threads vs Kernel-Level Threads

**User-Level Threads:**
- Managed by a **user library** (e.g., POSIX Pthreads, Win32 threads, Solaris threads).
- The kernel **does not know** about user threads — it schedules only processes.
- The programmer handles creation, deletion, synchronization, scheduling.

**Kernel-Level Threads:**
- Supported **directly by the kernel** (e.g., Linux, Windows XP/2000, Solaris lightweight processes).
- Switching between kernel threads of the same process: register values, PC, stack pointers change — **not** the memory management information.
- The kernel uses process scheduling algorithms to manage them.

### Hyper-Threading (Intel)

Intel implements the **hyper-threading** technology which increases the rate of switching between threads on a system with one physical core, making it appear as if it had multiple processors. Goal: enhancement of the multiprocessing character.

### Thread Examples

| Type | Example | Note |
| :--- | :--- | :--- |
| POSIX Pthreads | `pthread_create()`, `pthread_join()` | IEEE standard, mainly UNIX/Linux |
| Java threads | `Thread` class / `Runnable` | Supported by the JVM |

### Thread Advantages

- Creation without replacing the entire process.
- Most of the creation work is done in **user space**.
- Synchronization through variable monitoring (without a kernel call).
- Useful in applications with **independent, non-sequential tasks** (e.g., web servers, browsers).

> **[Key Insight]** Web browser example: one thread retrieves HTML, a second loads images/video, a third displays the page — all in shared memory.

---

## 5. Multiprocessing Systems

### Definition

**Multiprocessing** is the use of multiple concurrent processors/processes in a system.

### Categories of Multiprocessing Systems

| Category | Features | Interconnection example |
| :--- | :--- | :--- |
| Tightly coupled | Multiple CPUs on the same bus, shared or hierarchical memory | Shared memory bus |
| Loosely coupled | Each CPU has local memory, they communicate through a network | Gigabit Ethernet, telephone lines |

### Interconnection Topologies

- **Shared Bus:** All CPUs and memory are connected to one bus — simple but a bottleneck under high load.
- **Grid:** Each processor connects to its neighbors in a 2D grid.
- **Hypercube:** Each processor connects to $\log_2 N$ neighbors — high connectivity, low diameter.

---

## 6. Parallel Systems

### Definition

Parallel systems are **multiprocessing** systems with more than one processor that communicate with each other for a common computing goal.

### Categories

| Category | Acronym | Description |
| :--- | :--- | :--- |
| Symmetric Multiprocessing | SMP | All CPUs equal, shared memory, same OS |
| SMP Clusters | SMP Clusters | Groups of SMPs interconnected |
| Massively Parallel | MPP | A large number of processors, each with local memory |

**Distinguishing criteria:**
- Type of processor interconnection.
- Type of interconnection between processors and memories.

### Symmetric Multiprocessing (SMP) — Details

- Two or more processors **on the same motherboard**.
- Coordinated through the **system bus**.
- Each CPU runs an **identical copy** of the OS.
- **Automatic load balancing** among the CPUs.
- Main limitations: software and OS support.

### Asymmetric Multiprocessing

- The **master processor** schedules and assigns processes to the **slave** processors.
- Each slave undertakes a specific process.
- Common in **very large systems**.

### Parallel System Advantages

- High performance
- Economy of scale
- Increased reliability
- Availability
- Extensibility
- Scalability

---

## 7. Real-Time Systems

### Definition

Systems with **strict timing constraints** used as control devices in specialized applications (industrial control, medicine, scientific experiments).

### Categories

| Category | Features | Use |
| :--- | :--- | :--- |
| Hard Real-Time | Strict deadlines, limited secondary storage, data in RAM/ROM | Industrial control, robotics |
| Soft Real-Time | Flexible deadlines, does not require exhaustive real-time guarantee | Multimedia, Virtual Reality |

> **[Key Insight]** In **Hard Real-Time** systems, missing a deadline is considered a system failure. In **Soft Real-Time**, a small delay is tolerable (e.g., a dropped frame in video).

---

## 8. Distributed Systems

### Definition

Systems that distribute the computation process across **many physical processors — computers**, each with its own main and secondary memory and I/O components. They provide the user with the illusion of **a single memory space**.

### What Distributed Systems Hide

- The **way of accessing** a resource.
- **The location** where the resource resides.
- The **sharing** of resources by competing users.
- The **migration** of a resource during its use.
- The **differences** in data representation.

### Features of Distributed Systems

**Advantages:**
- Resource sharing
- Increase of computation speed
- Reliability
- Communication capabilities

**Disadvantages:**
- Security and protection (main issue)

---

## Comparative Analysis of Architectures

| Architecture | Structure | Performance | Reliability | Complexity |
| :--- | :--- | :--- | :--- | :--- |
| Monolithic | None | High | Low | Low |
| Layered | Layers | Moderate | Moderate | Moderate |
| Microkernel | Client-Server (user mode) | Lower (IPC overhead) | High | High |
| Threads / Multithreading | Within a process | High | Moderate | Moderate |
| SMP | Multiple CPUs, shared memory | Very high | High | High |
| Parallel (MPP) | Distributed memory | Very high | Very high | Very high |
| Real-Time | Specialized scheduling | Deterministic | Critical | High |
| Distributed | Many independent nodes | Scalable | Very high | Very high |

---

## Solved Exercises

### Exercise 1: Architecture Recognition

**Problem:** An OS consists of a collection of procedures where each one can directly call any other through parameters. Which architecture is described?

**Solution:**
1. There is no internal structure or separation → we rule out layered and microkernel.
2. Each procedure is visible to any other → a characteristic of monolithic.
3. **Answer: Monolithic architecture.**

---

### Exercise 2: System Call Steps

**Problem:** Describe in order the steps that a system call follows in a monolithic OS when a user program requests a file read.

**Solution:**
1. The program executes a special instruction → **trap** to the kernel.
2. The OS receives the service number (e.g., `read = 0`).
3. The OS locates the corresponding service procedure.
4. The procedure executes, reads the data.
5. Control is returned to the user program with the result.

---

### Exercise 3: Layered Architecture Levels

**Problem:** In a 5-level layered architecture (Layer 0–4), which levels are in kernel space and which in user space?

**Solution:**
1. Layer 4: **User space** (User applications — direct user interaction).
2. Layer 0–3: **Kernel space** (Processor scheduling, Memory management, Message interpreter, I/O management).
3. The user/kernel dividing line is between Layer 3 and Layer 4.

---

### Exercise 4: Microkernel — Communication Flow

**Problem:** In a microkernel architecture, an application requests access to the file system. Describe the flow.

**Solution:**
1. The application (client process) sends a request through the **System Call Interface**.
2. The request reaches the **File System server** (user space).
3. The server communicates with the microkernel through **IPC**.
4. The microkernel uses **Memory Management** or **Synchronization** if required.
5. The response is returned in reverse: microkernel → File System server → application.

---

### Exercise 5: Thread vs Process Comparison

**Problem:** Why is a context switch between threads cheaper than a switch between processes?

**Solution:**
1. During **process** switching: the **entire address space**, memory tables, open files change.
2. During **thread** switching within the same process: only the **registers, the PC, and the stack pointer** change.
3. The address space, data, code, files **remain shared** → no reload is needed.
4. **Conclusion:** Thread switching has much lower overhead.

---

### Exercise 6: Hard vs Soft Real-Time

**Problem:** An aircraft control application and a video playback system run on a real-time OS. Which is Hard and which is Soft? Justify.

**Solution:**
1. **Aircraft control → Hard Real-Time.** Failure to meet the deadline (e.g., delay in a maneuver command) can lead to disaster. Zero tolerance for delay.
2. **Video playback → Soft Real-Time.** A dropped frame is not a critical failure — it merely degrades the user experience.

---

### Exercise 7: SMP vs Asymmetric Multiprocessing

**Problem:** In which scenario is asymmetric multiprocessing preferred over SMP?

**Solution:**
1. **SMP:** All CPUs are equal, share the load automatically → suitable for general-purpose systems.
2. **Asymmetric:** The master CPU assigns jobs to slaves → suitable for **very large systems** where coordination is critical and processes can be specialized.
3. **Answer:** In very large installations (mainframes, high-performance computing) where CPU specialization increases efficiency.

---

### Exercise 8: Distributed vs Parallel Systems

**Problem:** What is the essential difference between distributed and parallel systems?

**Solution:**
1. **Parallel systems:** Many **tightly coupled** processors, usually shared or hierarchical memory, goal of simultaneous execution for high performance.
2. **Distributed systems:** Many **independent computers** with their own memory, communicating through a network. The user sees a single system.
3. **Key:** In distributed systems, the system **hides** heterogeneity (resource location, data format, etc.). In parallel systems, the focus is on the **speed** of execution.

---

## Exam Tip: Classification of Architectures in Questions

**Common exam mistakes:**

1. **Confusing Multithreading with Multiprocessing:** Threads share an address space within **one** process. Multiprocessing uses **multiple CPUs**.

2. **Hard vs Soft Real-Time:** The criterion is the **severity** of a deadline failure — critical (hard) or tolerable (soft).

3. **Monolithic vs Microkernel:** In monolithic **ALL** run in kernel mode. In microkernel **only** IPC, memory management, synchronization reside in the kernel.

4. **Distributed vs Parallel:** In distributed systems each node has **separate memory** and communicates through a network. In parallel SMP systems the memory is **shared**.

**Mnemonic for the layered architecture (Layer 0→4):**
> **P**rocessor → **M**emory → **M**essage → **I**/O → **U**ser
> (**P**rocessors **M**anage **M**essages **I**n **U**nison)

---
# OS_Lec05_NOTES.md
---

# Mutual Exclusion

## Introduction
Mutual exclusion is the prevention of a process from executing an action that some other process is simultaneously performing. It is required for the protection of shared resources so that side effects due to competition are prevented.

---

## Critical Sections
A critical section is a sequence of instructions that requires access to shared resources. The effectiveness of multiprocessing depends on the length of the critical section, which must be as short as possible.

### Conditions for Mutual Exclusion
For the correct cooperation of parallel processes, the following conditions are required:
1. Two processes cannot be simultaneously in their critical sections.
2. No assumption is allowed about the speed or the number of processors.
3. A process outside a critical section cannot suspend another process.
4. Avoidance of deadlock.
5. Progress: Only one process must succeed in entering if many are trying.
6. Avoidance of starvation: No indefinite waiting.
7. Minimal overhead upon entry when there is no competition.
8. Staying in the critical section only for a certain time period.

---

## Implementation: Software Approaches

Software solutions (e.g., Dekker's Algorithm) place the responsibility on the programmer, ordering the accesses serially. There is no hardware support.

### Dekker's Algorithm
It relies on the fact that only one access at a time is allowed to a memory location.

**1st Attempt (Strict Alternation)**
It implements mutual exclusion but causes busy waiting.

```c
/* Process 0 */
while (turn != 0) do
    nothing;
<critical section>
turn = 1;
```

**2nd Attempt (Flag Array - Flags)**
It fails because a process can change its state after being checked by the other, leading both simultaneously into the critical section.

---

## Implementation: Hardware Support

The problems of software (busy waiting, complexity) are solved through special-purpose hardware instructions.

### A. Disabling Interrupts
Prevents process switching.

```c
while (true) {
    /* disable interrupts */;
    /* critical section */;
    /* enable interrupts */;
    /* remainder */;
}
```
*   **Advantage:** Useful for the system kernel.
*   **Disadvantage:** High cost, does not guarantee mutual exclusion in multiprocessor systems (only one processor is affected).

### B. Special Machine Instructions (Test and Set)
Modern processors provide atomic instructions (`TAS`, `xchg`) that read and modify a memory location in a single indivisible machine cycle.

```c
int TAS(int* lock) {
    int tmp;
    tmp = *lock;
    *lock = true;
    return tmp;
}
```

```c
/* Use of TAS for mutual exclusion */
var lock = false; /* shared */
while (TAS(&lock) == true) do
    nothing;
<critical section>
lock = false;
<remainder>
```

| Advantages | Disadvantages |
| :--- | :--- |
| Applicable to multiple processes and processors | Busy waiting |
| Simple verification | Possibility of starvation |
| Support for multiple critical sections | Possibility of deadlock (Priority Inversion) |

> **[Key Insight]** The deadlock (Priority Inversion) occurs when a low-priority process in the critical section is interrupted by a high-priority process. The high-priority one enters busy waiting waiting for the resource, preventing the low-priority one from completing and releasing it.

---

## Semaphores

Semaphores eliminate busy waiting through execution suspension mechanisms (`sleep` / `wakeup`).
They are special synchronization variables that take non-negative integer values and have a waiting queue.

### Atomic Operations
*   **P (wait):** Waits for the semaphore to become $>0$ and decrements it by $1$. If it is $0$, the process blocks in the queue. It is called *before* the critical section.
*   **V (signal):** Increments the semaphore by $1$. It unblocks one process from the semaphore's queue. It is called *after* the critical section.

### Types of Semaphores
1. **Binary Semaphores:** Values $0$ and $1$. Ideal for mutual exclusion.
2. **Counting Semaphores:** Any non-negative value. Used for the management of limited resources.

> **[Exam Tip]** When designing mutual exclusion solutions, a binary semaphore is always initialized to $1$. When a semaphore is used for *execution synchronization* between two processes, it is initialized to $0$.

### Example: Mutual Exclusion
```c
Semaphore Q = 1; /* shared */

wait(Q);
<critical section>
signal(Q);
<remainder>
```

### Example: Execution Synchronization
Process 2 must execute after Process 1.
```c
Semaphore flag = 0;
```

**Process 1 (P1):**
```c
A;
signal(flag);
```

**Process 2 (P2):**
```c
wait(flag);
B;
```

> **[Key Insight]** Incorrect use of semaphores (e.g., calling the `wait` operations in reverse order) can cause a Deadlock, where two processes wait indefinitely for each other's `signal`.

---
# OS_Lec06_NOTES.md
---

# Operating Systems — Chapter 6: Deadlock

Deadlock is one of the fundamental concepts in operating systems and concerns the indefinite waiting of a set of processes due to competition for resources. The chapter covers definitions, resource categories, resource allocation graphs, the 4 necessary conditions for deadlock, the basic handling strategies, and the classic dining philosophers problem.

---

## 1. Basic concepts

### Definition of deadlock

Deadlock is the permanent or indefinite waiting of a set of processes that either compete for system resources or communicate with each other.

### Why it occurs

In a multiprogramming system, the total demands of active processes usually exceed the available resources. Deadlock occurs when two or more processes have conflicting needs for resources and none can continue.

### Design goal

The basic goal is to design systems where deadlock cannot happen or where it can be detected and recovered from in a controlled manner.

> **[Key Insight]**
> The problem is not simply the lack of resources, but the specific sequence of resource acquisition and waiting by many processes.

---

## 2. Types of resources

### Preemptable resources

Preemptable resources are those that can be taken away from a process without causing failure.

Examples:

- Memory space in certain management models.
- CPU registers in environments where state is saved and restored.

### Nonpreemptable resources

Nonpreemptable resources are those that cannot be taken away without undesirable consequences or failure of the process.

Examples:

- Printers.
- Tape drives.
- CD recorders.
- Input/output devices with critical state.

Nonpreemptable resources are the main cause of deadlock occurrence.

### Resource usage cycle

The use of a resource by a process usually follows the sequence:

1. Request.
2. Use.
3. Release.

If the request is not satisfied, the process is either suspended or fails with an error message.

### Reusable resources

Reusable resources can be safely used by one process at a time and then returned for use by other processes.

Examples:

- Processors.
- I/O channels.
- Main memory.
- Secondary storage.
- Files.
- Databases.
- Semaphores.

Deadlock here arises when a process holds a resource and requests another.

### Consumable resources

Consumable resources are produced and destroyed during their use. Once consumed, they cease to exist as available resources.

Examples:

- Interrupts.
- Signals.
- Messages.
- Information in I/O buffers.

In this category, deadlock can occur, for example, when a message sent by one process is not received by another.

---

## 3. Examples of deadlock

### Classic pattern

If process $P$ first acquires resource $A$ and then requests $B$, while process $Q$ first acquires $B$ and then requests $A$, a deadlock can arise.

This happens because:

- $P$ waits for a resource held by $Q$.
- $Q$ waits for a resource held by $P$.
- Neither can proceed to release the resource it holds.

### Example with memory

Assume available main memory of $200\text{KB}$ and two processes:

- $P_1$: requests $80\text{KB}$ and then $60\text{KB}$.
- $P_2$: requests $70\text{KB}$ and then $80\text{KB}$.

If the first requests are satisfied first, $150\text{KB}$ are allocated and $50\text{KB}$ remain. Then none of the second requests can be satisfied, so the processes block.

This case is solved more easily because memory is considered a preemptable resource.

---

## 4. Resource allocation graphs

Resource allocation graphs are a tool for modeling the state of resources and processes.

### Notation

- Process node: $P_i$.
- Resource type node: $R_j$.
- Request edge: $P_i \rightarrow R_j$.
- Assignment edge: $R_j \rightarrow P_i$.

### Interpretation

- If there is an edge from a process to a resource, the process requests an instance of the resource.
- If there is an edge from a resource to a process, an instance of the resource has been assigned to the process.

### Relationship between cycles and deadlock

- If the graph **does not** contain a cycle, then there is **no** deadlock.
- If the graph contains a cycle and there is only one instance per resource type, then there is a deadlock.
- If the graph contains a cycle and there are multiple instances per resource type, then there is only a possibility of deadlock, not a certainty.

> **[Key Insight]**
> A cycle in a resource allocation graph does not always mean deadlock. The critical detail is whether each resource type has one or more instances.

---

## 5. The 4 necessary conditions for deadlock

Deadlock can occur only if the following four conditions hold **simultaneously**.

### 5.1 Mutual exclusion

Each resource is either available or belongs exclusively to only one process.

### 5.2 Hold and wait

A process can already hold some resources and simultaneously wait for additional resources.

### 5.3 No preemption

Resources cannot be forcibly taken away from the process holding them.

### 5.4 Circular wait

There is a closed chain of processes where each process waits for a resource held by the next.

### Basic conclusion

To prevent deadlock, it suffices to violate at least **one** of the four necessary conditions.

---

## 6. Handling approaches

There are four basic approaches:

1. Prevention.
2. Avoidance.
3. Detection & recovery.
4. Manual intervention.

### 6.1 Prevention

In prevention we design the system so that at least one of the four necessary conditions is violated.

#### Violating mutual exclusion

The goal is to reduce the cases of exclusive resource use.

Example:

- For a printer, instead of many processes using it directly, a `printer daemon` and a print queue are used.

Limitation: not all resources can be practically converted into shared ones.

#### Violating hold and wait

Two basic techniques:

- The process requests **all** its resources before it starts.
- If it needs new resources later, it first releases those it already holds and re-requests the full set.

Disadvantages:

- Usually not all requirements are known in advance.
- Prolonged deprivation can arise.
- Resources remain allocated without being used continuously.

#### Violating no preemption

If possible, a resource is temporarily taken from a process and given elsewhere.

It applies only to resources whose state can be saved and restored later.

Examples where it is **not** practical:

- Writing to a CD.
- Many physical I/O devices.

#### Violating circular wait

A linear ordering of resources is defined and processes are required to request resources only in increasing order.

Example:

- If $R_1 < R_2 < R_3$, a process may request $R_1$ and then $R_3$, but not $R_3$ and then $R_1$.

### 6.2 Avoidance

In avoidance the system allows the first three conditions, but decides dynamically whether a new allocation could later lead to a deadlock.

Additional advance information is required, mainly the maximum number of resources each process may request.

Main idea:

- Allocate resources only if the system remains in a **safe state**.

### 6.3 Detection and recovery

In this approach the system allocates resources whenever it can and periodically checks whether a deadlock has formed.

If a deadlock is detected, recovery is applied through:

- Termination of processes.
- Preemption of resources.
- Rolling back to previous checkpoints.

### 6.4 Manual intervention

In some practical systems, the administrator simply restarts the system when the situation seems out of control or excessively slow.

---

## 7. Banker's algorithm

The banker's algorithm is the classic deadlock avoidance technique for systems with multiple resource instances.

### Basic concepts

- **System state:** the current allocation of resources to processes.
- **Safe state:** there is at least one completion sequence of processes without deadlock.
- **Unsafe state:** there is no guaranteed safe sequence. This does not mean certain deadlock, but a real possibility.

### Assumptions

The algorithm assumes that:

- There are multiple resource instances.
- Each process declares its maximum demand in advance.
- A process that receives all its resources will return them in finite time.
- The number of resources is fixed.
- The significant processes are independent.
- No process terminates while holding resources.

### Data structures

Let $n$ processes and $m$ resource types.

- `Available[j]`: available instances of resource $R_j$.
- `Max[i,j]`: maximum demand of process $P_i$ for resource $R_j$.
- `Allocation[i,j]`: instances of resource $R_j$ already assigned to $P_i$.
- `Need[i,j]`: additional instances of $R_j$ that $P_i$ may need.

It is defined:

$$
Need[i,j] = Max[i,j] - Allocation[i,j]
$$

### Criterion of a safe sequence

A sequence $\langle P_1, P_2, \dots, P_n \rangle$ is safe if for every process in the sequence, its remaining needs can be satisfied from the currently available resources together with the resources that will be returned by the preceding processes.

### Steps of the safety algorithm

1. Find a process $P_i$ with $Need[i,j] \leq Available[j]$ for every $j$.
2. Assume that the process completes.
3. Return its resources:
   $$
   Available[j] = Available[j] + Allocation[i,j]
   $$
4. Mark it as completed.
5. Repeat until either all processes complete or no other suitable process can be found.

If all complete, the state is safe.

---

## 8. Deadlock detection

Detection is algorithmically similar to the safety check, but the logic is different: here the system **does not** reject allocations in advance, but checks whether deadlock has already occurred.

### Data structures

Used:

- `Available`
- `Allocation`
- `Need`

### Steps

1. Find a row $i$ where $Need[i,j] \leq Available[j]$ for all $j$.
2. If no such row exists, the unmarked processes are in deadlock.
3. Otherwise, consider that the process completes and returns its resources.
4. Repeat.

### Cost and practice

Detection avoids the continuous restriction of resource access, but requires periodic checks and a recovery strategy.

In practice, many operating systems do not apply strict global detection, but use combinations of techniques such as:

- Quotas.
- Design constraints.
- Conventions for the use of semaphores and resources.
- Process failure when it cannot acquire a critical resource.

### Recovery strategies

When a deadlock is detected, the following can be applied:

- Termination of all processes in deadlock.
- Successive termination until the cycle is broken.
- Checkpoint/rollback.
- Successive resource preemption.

### Criteria for selecting a process for termination

Common criteria:

- Smaller CPU time already consumed.
- Smaller number of output lines produced.
- Larger estimated remaining time.
- Smaller number of allocated resources.
- Lower priority.

---

## 9. Dining philosophers problem

### Description

Five philosophers sit around a circular table. Each philosopher alternates between thinking and eating. To eat, he needs two forks: his left and his right one.

The problem models:

- Each philosopher as a process.
- Each fork as a shared resource.

### What it shows

The problem is used to highlight the difficulty of resource allocation without:

- Deadlock.
- Prolonged starvation.
- Pointless reduction of parallelism.

### Naive solution that fails

If each philosopher executes:

```c
wait(fork[i]);
wait(fork[(i+1) mod 5]);
eat();
signal(fork[(i+1) mod 5]);
signal(fork[i]);
```

all of them can pick up one fork and wait forever for the second one.

### Avoidance techniques

The following solutions emerge from the material:

- Adding one more fork.
- At most 4 philosophers at the table simultaneously.
- Different fork acquisition order for even and odd philosophers.
- Acquiring forks only when both are available.
- Non-symmetric protocol design.

### Solution with the `room` semaphore

```c
semaphore fork[5] = {1};
semaphore room = {4};

while (true) {
    think();
    wait(room);
    wait(fork[i]);
    wait(fork[(i+1) mod 5]);
    eat();
    signal(fork[(i+1) mod 5]);
    signal(fork[i]);
    signal(room);
}
```

The idea is that at most 4 philosophers are allowed to attempt eating simultaneously, so the possibility of a full circular wait is broken.

---

## 10. Connection of concepts

| Concept | Role |
| :--- | :--- |
| Mutual exclusion | A resource is not shared simultaneously |
| Hold and wait | A process holds resources while requesting others |
| No preemption | Resources are not forcibly taken away |
| Circular wait | Closed cycle of process dependency |
| Prevention | Breaks one of the 4 conditions |
| Avoidance | Allows allocations only if the state remains safe |
| Detection | Checks whether the deadlock already exists |
| Recovery | Termination, rollback, or preemption for release |
| Dining philosophers | Classic model of deadlock and starvation |

---

## Solved Exercises

### Exercise 1: Checking deadlock conditions

**Problem:** A process holds a printer and waits for access to a file held by a second process, while the second waits for the printer. Which deadlock conditions hold?

**Solution:**

1. The printer and the file are considered exclusive resources, so mutual exclusion holds.
2. Each process holds a resource and waits for another, so hold and wait holds.
3. The resources are not forcibly taken away, so no preemption holds.
4. The first waits for a resource of the second and the second for a resource of the first, so there is circular wait.
5. Since all 4 conditions hold, the system is in a deadlock.

### Exercise 2: Allocation graph from a description

**Problem:** Given the following: process $P_1$ requests resource $R_1$, process $P_2$ requests resource $R_3$, resource $R_1$ is assigned to $P_2$, $R_2$ is assigned to $P_1$, and $R_3$ is assigned to $P_1$. Describe the graph and check whether there is a deadlock.

**Solution:**

1. The request edges are $P_1 \rightarrow R_1$ and $P_2 \rightarrow R_3$.
2. The assignment edges are $R_1 \rightarrow P_2$, $R_2 \rightarrow P_1$, $R_3 \rightarrow P_1$.
3. $P_1$ waits for $R_1$, which belongs to $P_2$.
4. $P_2$ waits for $R_3$, which belongs to $P_1$.
5. A cycle is formed: $P_1 \rightarrow R_1 \rightarrow P_2 \rightarrow R_3 \rightarrow P_1$.
6. If there is one instance per resource, then there is a deadlock.

### Exercise 3: Tape drives

**Problem:** The system has 6 identical tape drives and $n$ processes. Each process may request up to 2 tape drives. For which value of $n$ is the system deadlock-free?

**Solution:**

1. For a guarantee of deadlock absence, there must always be the possibility of at least one process getting the second tape drive it may need.
2. In the worst case, each process holds 1 tape drive and waits for another 1.
3. If there are $n$ processes, then in the worst case $n$ drives are allocated.
4. For some process to complete, at least 1 drive must be free.
5. Therefore $n \leq 5$ is required.
6. For $n = 6$, all processes can hold 1 drive each and wait for another 1, so circular wait is possible.

### Exercise 4: Memory example

**Problem:** $P_1$ requests $80\text{KB}$ and then $60\text{KB}$, while $P_2$ requests $70\text{KB}$ and then $80\text{KB}$. The total available memory is $200\text{KB}$. Examine whether a deadlock can be created.

**Solution:**

1. We satisfy the first request of $P_1$: $120\text{KB}$ remain.
2. We satisfy the first request of $P_2$: $50\text{KB}$ remain.
3. $P_1$ requests an additional $60\text{KB}$, but there are not enough available.
4. $P_2$ requests an additional $80\text{KB}$, but again there are not enough available.
5. Both block on the second request.
6. The problem is solved with memory preemption, because memory can be recalled/reallocated more easily than other resources.

### Exercise 5: Computing the Need matrix

**Problem:** If for a process $Max = (6,1,2)$ and $Allocation = (2,1,1)$, find $Need$.

**Solution:**

1. We use the formula:
   $$
   Need = Max - Allocation
   $$
2. We compute per component:
   $$
   Need = (6-2, 1-1, 2-1)
   $$
3. Hence:
   $$
   Need = (4,0,1)
   $$
4. The process still needs 4 units of the first resource, 0 of the second, and 1 of the third to complete.

### Exercise 6: Checking a safe sequence

**Problem:** Let $Available = (0,1,1)$ and from the chapter example a safe sequence is $P_2 \rightarrow P_1 \rightarrow P_3 \rightarrow P_4$. What does this mean?

**Solution:**

1. The existence of this sequence means that the system is in a safe state.
2. First, $P_2$ can complete with the available resources.
3. After its completion, it returns its resources and increases `Available`.
4. This makes the completion of $P_1$, then $P_3$, and finally $P_4$ feasible.
5. Therefore, although the initially available resources are few, there is an execution order that avoids deadlock.

### Exercise 7: Prevention through resource ordering

**Problem:** Suppose there are resources $R_1 < R_2 < R_3$. Can a process request $R_2$ first and then $R_1$?

**Solution:**

1. If a linear resource numbering policy is applied, requests must follow increasing order.
2. Requesting $R_2$ first and then $R_1$ violates this policy.
3. The violation could allow the creation of a waiting cycle with other processes.
4. Therefore the request is not allowed.
5. The goal is to preclude the circular wait condition.

### Exercise 8: Dining philosophers with room = 4

**Problem:** Why does the use of the `room = 4` semaphore prevent deadlock in the philosophers problem?

**Solution:**

1. Without restriction, all 5 philosophers can simultaneously pick up one fork.
2. Then each waits for the second and a full waiting cycle is created.
3. With `room = 4`, at most 4 philosophers attempt to acquire forks simultaneously.
4. So at least one always remains outside the acquisition process, which breaks the possibility of forming a 5-member cycle.
5. Thus deadlock is avoided.

---

## Exam Tip: Quick recognition method

In theory questions, the fastest check is the following:

1. Ask whether there is exclusive resource use.
2. Check whether some process holds resources while requesting others.
3. Check whether resources are forcibly taken away or not.
4. Look for a waiting cycle.

If the answer is **yes** to all 4, then you have a deadlock or the exact preconditions for it to occur.

> **[Key Insight]**
> In graph exercises, first check for a cycle and immediately after for the number of instances per resource type. These two steps solve almost the entire question.

---
# OS_Lec07_NOTES.md
---

# Chapter 7 — Memory Management

This file covers the core concepts of main memory management as presented in Chapter 7 of the Operating Systems course. Topics include memory manager design, management strategies, fixed and dynamic partitioning, fragmentation, placement algorithms, and swapping. The material falls under **Type C — Engineering and Applied Science Topics**.

---

## 1. Conceptual Foundation

Memory management is the OS function responsible for subdividing main memory dynamically so that as many processes as possible can be serviced efficiently. Without it:
- Programs larger than physical memory could not run.
- Multiple processes could not coexist in memory simultaneously (no multiprogramming).
- There would be no protection or isolation between processes.

**Key goals (from the programmer's and OS perspective):**

| Goal | Description |
| :--- | :--- |
| Minimize access time | Reduce latency to fetch instructions/data |
| Maximize addressable space | Allow programs to use as much memory as needed |
| Enable multiprogramming | Keep multiple processes resident simultaneously |
| Provide protection | Prevent one process from corrupting another |
| Ease of programming | Hide physical memory constraints from the programmer |

---

## 2. The Memory Manager

The **memory manager** is the OS component responsible for organizing and applying memory management strategies.

**Responsibilities:**
- Allocate primary (main) memory to processes.
- Map each process's address space onto physical memory.
- Minimize access time using cost-effective static or dynamic techniques.
- Interact with dedicated hardware — the **Memory Management Unit (MMU)** — to improve performance.

---

## 3. Memory Management Strategies

Three orthogonal strategy categories govern when, where, and which data occupies main memory:

| Strategy Class | Purpose |
| :--- | :--- |
| **Fetch strategy** | Decides *when* the next program/data segment is moved from secondary to primary memory |
| **Placement strategy** | Decides *where* in main memory the incoming segment is placed |
| **Replacement strategy** | Decides *which* segment to evict when main memory is full |

---

## 4. Memory Allocation Types

### 4.1 Contiguous Allocation

The entire program is placed in adjacent memory locations.
- Used in early computing systems.
- If a program is larger than available memory, the system cannot execute it.

### 4.2 Non-Contiguous Allocation

The program is divided into pieces (pages or segments) placed in non-adjacent slots of main memory.
- Enables use of memory regions too small for an entire program.
- Increases system complexity but significantly raises the degree of multiprogramming.
- Realized through **virtual memory**.

---

## 5. Basic Memory Management

### 5.1 Monoprogramming

One user monopolizes all system resources. Three simple physical memory layouts exist:

```
Layout A             Layout B             Layout C
+-----------------+  +-----------------+  +------------------+
| User Program    |  | OS (ROM)        |  | Device Drivers   |
| (RAM)           |  +-----------------+  | (ROM)            |
|                 |  | User Program    |  +------------------+
+-----------------+  | (RAM)           |  | User Program     |
| OS (RAM)        |  +-----------------+  | (RAM)            |
| 0               |                    |  +------------------+
+-----------------+                    |  | OS (RAM)         |
                                        |  | 0                |
                                        |  +------------------+
```

Memory protection is not a concern in monoprogramming — only one process runs at a time.

### 5.2 Overlays

A technique enabling execution of programs larger than the available memory partition.

**Mechanism:**
1. The programmer divides the program into logical modules.
2. A portion of the program and data that must always remain in memory occupies the fixed area.
3. The remaining modules are loaded into an **overlay area** on demand, replacing the previous module.

```
Memory:
+-------------------------+
| OS                      |
+-------------------------+  <-- address a
| Permanent code/data     |
+-------------------------+  <-- address b
| Overlay area            |  <-- modules loaded here sequentially:
|  [1] Initialization     |      (1) Load init phase, run
|  [2] Processing         |      (2) Load processing phase, run
|  [3] Output             |      (3) Load output phase, run
+-------------------------+  <-- address c
```

> **[Key Insight]** Overlays solve the size-fit problem but require the programmer to manually decompose the program. The OS does not manage this automatically.

---

## 6. Memory and Multiprogramming

### 6.1 Motivation

A single process frequently blocks on I/O operations, which are orders of magnitude slower than CPU operations. The CPU sits idle during I/O waits. **Multiprogramming** keeps multiple processes resident in memory so that when one process waits on I/O, another can use the CPU.

### 6.2 CPU Utilization Formula

Let:
- $p$ = probability that a process is waiting on I/O at any given moment
- $v$ = number of processes (degree of multiprogramming)

$$
\text{CPU utilization} = 1 - p^v
$$

**Interpretation:** As $v$ increases, CPU utilization approaches 1 (100%). Higher I/O wait probability $p$ requires more concurrent processes to achieve the same utilization.

> **[Key Insight]** This formula assumes processes are independent and I/O waits are statistically independent. It is a probabilistic approximation, not an exact model.

**Example values:**

| $p$ (I/O wait) | $v = 1$ | $v = 2$ | $v = 4$ | $v = 8$ |
| :--- | :--- | :--- | :--- | :--- |
| 20% | 80% | 96% | 99.8% | ~100% |
| 50% | 50% | 75% | 93.8% | 99.6% |
| 80% | 20% | 36% | 59.0% | 83.2% |

### 6.3 Trade-offs in Degree of Multiprogramming

- More processes → better CPU utilization, but requires better memory management and protection.
- Fewer processes → less memory consumed, but CPU may be underutilized.
- Higher I/O wait → more processes required to maintain CPU utilization.

> **[Key Insight]** For the remainder of this chapter, **contiguous allocation** is assumed: each process is assigned one contiguous memory block.

---

## 7. Fixed Partitioning

Memory is divided into a fixed number of partitions at system boot time. The number and sizes of partitions do not change during operation.

- Each process occupies exactly **one partition**.
- Maximum degree of multiprogramming = number of partitions.

### 7.1 Equal-Size Partitions

All partitions have the same size.

**Operation:**
- Any process with size $\leq$ partition size can be loaded.
- If all partitions are occupied, the OS swaps out one process.
- A program larger than one partition requires **overlays**.

**Problem — Internal Fragmentation:**

$$
\text{Internal Fragmentation} = \text{Partition Size} - \text{Process Size}
$$

Even the smallest process occupies an entire partition, wasting the remainder.

```
Before loading:         After loading Process 1 (small):
+-----------+           +-----------+
| 8 MB      | (free)    | Process 1 | (used by process)
|           |           +-----------+
|           |           | Unused    | <-- internal fragmentation
+-----------+           +-----------+
```

**Advantages:**
- Very low OS overhead.

**Disadvantages:**
- Extremely inefficient memory use due to internal fragmentation.
- Small processes waste large partition space.

### 7.2 Unequal-Size Partitions

Partitions have different sizes (e.g., 2 MB, 6 MB, 8 MB, 12 MB). This reduces internal fragmentation compared to equal-size partitions.

**Placement options:**

| Approach | Description | Drawback |
| :--- | :--- | :--- |
| **Queue per partition** | Each process is assigned to the queue of the smallest partition it fits in | A partition's queue may be empty while others are full; free memory exists but processes wait |
| **Single global queue** | When a process must be loaded, select the smallest available partition that fits | Better CPU utilization; reduces idle partitions |

**Advantages over equal-size:**
- Reduced internal fragmentation.
- More efficient use of main memory.

---

## 8. Fragmentation

| Type | Definition | Cause | Visibility |
| :--- | :--- | :--- | :--- |
| **Internal** | Allocated memory inside a partition that is not used by the process | Allocated block must be $\geq$ requested size | Visible only to the process holding the partition |
| **External** | Free memory outside all partitions that cannot satisfy any pending request despite sufficient total free space | Memory requests vary in size; free blocks become scattered | Visible to the OS / system-wide |

---

## 9. Dynamic Partitioning

Partitions are created at runtime with exactly the size required by each process. The number and sizes of partitions vary throughout system operation.

**Key property:** A process is allocated exactly the memory it requests — no internal fragmentation.

**Problem — External Fragmentation:**
Over time, as processes enter and leave, gaps (holes) appear in memory. These gaps may individually be too small to satisfy new requests, even though their sum could.

```
Initial:                After P2 exits:        After P4 exits:
+----------+            +----------+           +----------+
| OS       |            | OS       |           | OS       |
+----------+            +----------+           +----------+
| P1       |            | P1       |           | P1       |
+----------+            +----------+           +----------+
| P2       |  P2 exits  | Hole     |           | Hole     |
+----------+  ------->  +----------+  ------>  +----------+
| P3       |            | P3       |           | P3       |
+----------+            +----------+           +----------+
| P4       |            | P4       |  P4 exits | Hole     |
+----------+            +----------+           +----------+
| P5       |            | P5       |           | P5       |
+----------+            +----------+           +----------+
| Hole     |            | Hole     |           | Hole     |
+----------+            +----------+           +----------+
```

**Solution — Compaction:**
Shift all processes toward one end of memory so all free space coalesces into one contiguous block.

**Compaction costs:**
- Consumes CPU time.
- Requires **dynamic relocation** capability: the ability to move a running program to a different memory area without invalidating its memory references (typically handled by the MMU via a relocation register).

---

## 10. Placement Algorithms

When a process requests memory, the OS must select which free block to allocate. The three standard algorithms apply to dynamic partitioning.

### 10.1 First-Fit

Scan memory **from the beginning**; allocate the **first** free block large enough.

- Fastest algorithm.
- Tends to cluster allocations at the low end of memory, creating many small holes there.

### 10.2 Best-Fit

Scan **all** free blocks; allocate the **smallest** free block that is large enough.

- Minimizes wasted space within the chosen block.
- Worst overall performance: leaves very small residual fragments that are too small for future allocations, causing frequent compaction.
- Typically requires sorting or full scan of the free list.

### 10.3 Next-Fit

Scan memory **from the point of the last allocation**; allocate the **next** free block large enough.

- Distributes allocations more uniformly across memory.
- Tends to fragment the large free block at the high end of memory.
- Requires compaction to recover large free blocks at the end.
- Performance similar to first-fit.

**Algorithm comparison:**

| Algorithm | Scan Start | Selection Criterion | Speed | Fragmentation Behavior |
| :--- | :--- | :--- | :--- | :--- |
| First-Fit | Beginning | First sufficient block | Fastest | Small holes accumulate at low addresses |
| Best-Fit | Full scan | Smallest sufficient block | Slowest | Tiny residual fragments everywhere |
| Next-Fit | Last placement point | First sufficient block from that point | Moderate | Large end-block eroded |

---

## 11. Swapping

Swapping is the technique of temporarily moving an entire process from main memory to a **backing store** (secondary storage, typically a disk partition or swap file), freeing its memory for other processes.

**Swap-out:** Process is written from RAM to backing store.
**Swap-in:** Process is read back from backing store into RAM.

```
Main Memory         Backing Store
+----------+        +----------+
| OS       |        | P1 image |
+----------+  <-->  +----------+
| User     |  swap  | P2 image |
| space    |        +----------+
+----------+
```

**Memory allocation evolves as:**
- New processes arrive and are loaded.
- Processes complete and release memory.
- Blocked processes are swapped out to disk.

Swapping is typically used in conjunction with dynamic partitioning. Memory changes over time as processes move in and out:

```
State 1   State 2   State 3   State 4   State 5   State 6   State 7
+-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+
|     |   |     |   |  C  |   |  C  |   |  C  |   |  C  |   |  C  |
|     |   |  B  |   |  B  |   |  B  |   |  B  |   |     |   |  A  |
|  A  |   |  A  |   |  A  |   |     |   |  D  |   |  D  |   |  D  |
| OS  |   | OS  |   | OS  |   | OS  |   | OS  |   | OS  |   | OS  |
+-----+   +-----+   +-----+   +-----+   +-----+   +-----+   +-----+
```
(Grey/blank areas represent unused memory.)

### 11.1 Limitations of Swapping

| Problem | Description |
| :--- | :--- |
| Size constraint | A process must fit entirely within physical memory (no partial loading under contiguous allocation) |
| Fragmentation | Memory fragments over time; compaction required |
| Dual residence | A process can exist partially in memory and partially on disk simultaneously |

**Overlays** partially solve the size-constraint problem by subdividing a process over time (primarily data), but do **not** solve external fragmentation.

---

## Solved Exercises

### Exercise 1: CPU Utilization with Multiprogramming

**Problem:**
A system has $p = 0.80$ (80% I/O wait). How many concurrent processes ($v$) are needed to achieve at least 90% CPU utilization?

**Solution:**

$$
\text{CPU} = 1 - p^v \geq 0.90
$$

$$
p^v \leq 0.10
$$

$$
0.80^v \leq 0.10
$$

Taking logarithms:

$$
v \cdot \ln(0.80) \leq \ln(0.10)
$$

$$
v \geq \frac{\ln(0.10)}{\ln(0.80)} = \frac{-2.3026}{-0.2231} \approx 10.32
$$

Therefore, $v \geq 11$ processes are needed to achieve $\geq 90\%$ CPU utilization when $p = 0.80$.

---

### Exercise 2: Internal Fragmentation in Equal-Size Partitions

**Problem:**
A system uses fixed equal-size partitions of 8 MB each (5 partitions). Process sizes are: 2 MB, 7 MB, 5 MB, 3 MB, 8 MB. Calculate total internal fragmentation.

**Solution:**

| Process | Size | Partition Size | Internal Fragmentation |
| :--- | :--- | :--- | :--- |
| P1 | 2 MB | 8 MB | 6 MB |
| P2 | 7 MB | 8 MB | 1 MB |
| P3 | 5 MB | 8 MB | 3 MB |
| P4 | 3 MB | 8 MB | 5 MB |
| P5 | 8 MB | 8 MB | 0 MB |

$$
\text{Total internal fragmentation} = 6 + 1 + 3 + 5 + 0 = 15 \text{ MB}
$$

Out of $5 \times 8 = 40$ MB total memory (excluding OS), 15 MB (37.5%) is wasted.

---

### Exercise 3: Placement Algorithms — Worked Example (from slides)

**Problem:**
Free memory blocks (in order): 8K, 12K, 22K, 18K, 8K, 6K, 14K, 36K.
The **last allocation** was in the 18K block (14K was allocated there, leaving a small used portion).
Allocate a new block of **16K**. Show the result for First-Fit, Best-Fit, and Next-Fit.

**Solution:**

Free blocks that can satisfy 16K: 22K, 18K (partially — but the slide shows 18K as occupied after 14K allocation, so it is not free), 36K.

Examining only **free** blocks $\geq 16K$: 22K (position 3), 36K (last position).

**First-Fit:**
Scan from the beginning. First free block $\geq 16K$ is **22K**.
Allocate 16K there. Remaining fragment: $22 - 16 = 6K$.

**Best-Fit:**
Scan all free blocks. Smallest block $\geq 16K$: **18K** (if available) → from the slide the 18K block is shown as occupied; next candidate is **22K** (residual 6K). The slide confirms Best-Fit selects 18K and produces a **2K** residual.

> **[Key Insight]** The slide example shows the 18K block as still containing a free portion. Best-Fit selected 18K (16K allocated, 2K residual) — this is the smallest block that fits, confirming it leaves the smallest fragment of all three algorithms but contributes to fine-grained fragmentation over time.

**Next-Fit:**
Scan from the **last allocation point** (after the 18K block → the 8K, 6K, 14K, 36K region). First free block $\geq 16K$ from that point: **36K**.
Allocate 16K there. Remaining fragment: $36 - 16 = 20K$.

**Summary:**

| Algorithm | Block Used | Residual Fragment |
| :--- | :--- | :--- |
| First-Fit | 22K | 6K |
| Best-Fit | 18K | 2K |
| Next-Fit | 36K | 20K |

---

### Exercise 4: Dynamic Partitioning — First-Fit (Exercise 2 from slides)

**Problem:**
Free memory blocks (in order): 100KB, 500KB, 200KB, 300KB, 600KB.
Process requests arrive in order: 212KB, 417KB, 112KB, 426KB.
Apply **First-Fit**. Show the state of free blocks after each allocation.

**Solution:**

Initial free list: [100, 500, 200, 300, 600]

**Request 212KB:**
First-Fit scans: 100 (too small), 500 ($\geq$ 212). Allocate from 500KB block.
Residual: $500 - 212 = 288KB$.
Free list: [100, 288, 200, 300, 600]

**Request 417KB:**
First-Fit scans: 100 (no), 288 (no), 200 (no), 300 (no), 600 ($\geq$ 417). Allocate from 600KB.
Residual: $600 - 417 = 183KB$.
Free list: [100, 288, 200, 300, 183]

**Request 112KB:**
First-Fit scans: 100 (no), 288 ($\geq$ 112). Allocate from 288KB.
Residual: $288 - 112 = 176KB$.
Free list: [100, 176, 200, 300, 183]

**Request 426KB:**
First-Fit scans: 100, 176, 200, 300 — all $< 426$. 183 also $< 426$. **Cannot satisfy.** Request fails (or process waits).
Free list: [100, 176, 200, 300, 183] (unchanged)

---

### Exercise 5: Dynamic Partitioning — Best-Fit (Exercise 2 from slides)

**Problem:** Same initial free list and requests as Exercise 4. Apply **Best-Fit**.

**Solution:**

Initial free list: [100, 500, 200, 300, 600]

**Request 212KB:**
Blocks $\geq 212$: 500, 300, 600. Smallest is **300KB**.
Residual: $300 - 212 = 88KB$.
Free list: [100, 500, 200, 88, 600]

**Request 417KB:**
Blocks $\geq 417$: 500, 600. Smallest is **500KB**.
Residual: $500 - 417 = 83KB$.
Free list: [100, 83, 200, 88, 600]

**Request 112KB:**
Blocks $\geq 112$: 200, 600. Smallest is **200KB**.
Residual: $200 - 112 = 88KB$.
Free list: [100, 83, 88, 88, 600]

**Request 426KB:**
Blocks $\geq 426$: 600. Allocate from **600KB**.
Residual: $600 - 426 = 174KB$.
Free list: [100, 83, 88, 88, 174]

All requests satisfied.

---

### Exercise 6: Dynamic Partitioning — Next-Fit (Exercise 2 from slides)

**Problem:** Same initial free list [100, 500, 200, 300, 600]. Last allocation was before the **200KB block**. Apply **Next-Fit**.

**Solution:**

Scan starts **at** the 200KB block (the block after the last placement point).

**Request 212KB:**
Start at 200KB: 200 (no), 300 ($\geq 212$). Allocate from **300KB**.
Residual: $300 - 212 = 88KB$. Last pointer → after 300KB block.
Free list: [100, 500, 200, 88, 600]

**Request 417KB:**
Start after 300KB block: scan 88 (no), 600 ($\geq 417$). Allocate from **600KB**.
Residual: $600 - 417 = 183KB$. Last pointer → after 600KB block.
Free list: [100, 500, 200, 88, 183]

**Request 112KB:**
Wrap around from end: scan 100 (no), 500 ($\geq 112$). Allocate from **500KB**.
Residual: $500 - 112 = 388KB$. Last pointer → after 500KB block.
Free list: [100, 388, 200, 88, 183]

**Request 426KB:**
Start after 500KB block: scan 200 (no), 88 (no), 183 (no); wrap: 100 (no), 388 (no). **Cannot satisfy.**
Free list: [100, 388, 200, 88, 183] (unchanged)

---

### Exercise 7: Placement Algorithm 1 (Exercise 1 from slides)

**Problem:**
Memory image (left to right = low to high address). Shaded = occupied, white = free, black = last allocation point (12KB was last placed there).

| 20KB | [occ] | 30KB | [occ] | 12KB | [last] | 32KB | [occ] | 24KB | [occ] | 48KB |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

Free blocks: **20KB**, **30KB**, **32KB**, **48KB** (the 12KB block is the last-used region; 24KB is occupied).
Allocate **22KB**. Show result for First-Fit, Best-Fit, Next-Fit.

**Solution:**

Free blocks $\geq$ 22KB: 30KB, 32KB, 48KB.

**First-Fit:** Scan from start → first free block $\geq$ 22 is **30KB**.
Allocate 22KB; residual = **8KB**.

**Best-Fit:** Smallest free block $\geq$ 22 is **30KB** (residual 8K) — 30 is closer to 22 than 32 or 48.
Allocate 22KB; residual = **8KB**.

> **[Key Insight]** In this particular instance First-Fit and Best-Fit select the same block. Best-Fit is not always distinguishable from First-Fit in small examples.

**Next-Fit:** Last placement was in the 12KB region (between the two occupied blocks at position 5). Scan forward: next free block from that point = **32KB**.
Allocate 22KB; residual = **10KB**.

---

## Exam Tips

> **[Exam Tip — CPU Utilization Formula]**
> When asked to find the minimum number of processes $v$ for a target CPU utilization $u$, rearrange $1 - p^v \geq u$ to $p^v \leq 1 - u$ and apply logarithms: $v \geq \dfrac{\ln(1-u)}{\ln(p)}$. Always round **up** to the nearest integer. Do not forget to verify with the original formula.

> **[Exam Tip — Fragmentation Identification]**
> - **Internal** fragmentation: the wasted space is *inside* an allocated block — it belongs to a process that does not use it. Associated with **fixed partitioning**.
> - **External** fragmentation: the wasted space is *between* allocated blocks — it is free, but split into pieces too small to use. Associated with **dynamic partitioning**.
> These are mutually exclusive by definition.

> **[Exam Tip — Placement Algorithm Comparison]**
> The most common exam question asks you to apply all three algorithms to the same request and compare residual fragments. Remember:
> - **Best-Fit** always selects the *tightest* block but produces the most useless tiny fragments.
> - **Next-Fit** tends to destroy the largest block at the high end of memory.
> - **First-Fit** is empirically as good as or better than Best-Fit overall, and is faster.

> **[Exam Tip — Overlay vs. Swapping]**
> Overlays divide a **single process** over time (programmer-managed). Swapping moves **entire processes** in and out of memory (OS-managed). Overlays solve the size problem; neither technique eliminates external fragmentation.

---
# OS_Lec08_NOTES.md
---

# Virtual Memory — Operating Systems (Chapter 8)

Virtual memory is a memory management technique that creates the illusion of a larger address space than physically exists, using secondary storage as an extension of main memory. This chapter covers the conceptual foundation, address translation mechanisms, partitioning schemes (paging and segmentation), and the principal page replacement algorithms (FIFO, OPT, LRU).

---

## 1. Introduction and Motivation

### 1.1 Why Virtual Memory Exists

Main memory (RAM) is the second most critical resource in a computer system after CPU time. Even when physically large, available RAM is frequently insufficient because:

- Multiple processes must coexist in memory simultaneously (multiprogramming).
- Fetching data from disk instead of RAM introduces severe latency:
  - RAM access time: ~60 ns
  - Average HDD access time: ~10 ms = $10 \times 10^6$ ns

The ratio of disk-to-RAM access latency is approximately $1.67 \times 10^5$, making disk access roughly 167,000 times slower than RAM. Loading every byte of every process into RAM before execution is therefore both impractical and unnecessary.

### 1.2 Core Idea

Virtual memory creates the **illusion** that a process has access to more memory than is physically installed. The OS and hardware cooperate to:

1. Keep only the **actively used portions** of a process in RAM.
2. Store the remainder on **secondary storage** (swap space on disk).
3. Transparently move data between disk and RAM as needed.

---

## 2. Virtual and Physical Addresses

### 2.1 Definitions

| Term | Definition |
| :--- | :--- |
| **Virtual address** (logical address) | An address generated by the CPU and used by a process. Exists in the process's virtual address space. |
| **Physical address** (real address) | An address in actual RAM, used by the memory hardware. |
| **Virtual address space** | The set of all addresses a process may legally reference. Each process has its own independent virtual address space. |
| **Physical address space** | The set of all addresses in installed RAM. Shared across all processes. |

### 2.2 Address Translation

The **Memory Management Unit (MMU)** is hardware embedded in the CPU that translates every virtual address into a physical address at runtime. Processes always operate in virtual address space; the MMU performs the mapping transparently.

$$
\text{Virtual Address} \xrightarrow{\text{MMU}} \text{Physical Address}
$$

Because each process has its own virtual address space:
- Process isolation is guaranteed: one process cannot read or write another's memory.
- Processes can be relocated in physical memory without changes to their code.

---

## 3. Logical Organization

### 3.1 Memory as a Linear Space

At the hardware level, both RAM and secondary storage are organized as linear, one-dimensional address spaces (byte-addressable arrays).

### 3.2 Program Modules

Programs are written and compiled as collections of **modules** (functions, libraries, data segments). Key properties:

- Modules are compiled **independently** of one another.
- Different modules can be assigned different **protection levels**:
  - `read-only` — data that must not be modified (e.g., string literals, constants).
  - `execute-only` — code that must not be read as data.
  - `read-write` — standard heap and stack segments.
- Modules can be **shared** between processes (e.g., shared libraries), avoiding duplicate copies in RAM.

---

## 4. Partitioning of Virtual Memory

Two fundamental techniques partition the virtual address space and manage its mapping to physical memory.

---

## 5. Paging

### 5.1 Concept

**Paging** divides both the virtual address space and physical memory into fixed-size blocks:

- **Page** — a fixed-size block of virtual memory belonging to a process.
- **Page frame** (frame) — a fixed-size block of physical RAM.

Page size equals frame size. A virtual page may be placed into **any** free frame; pages need not occupy contiguous frames.

> **[Key Insight]** Because frames are fixed-size and interchangeable, the OS can always find a free frame for any page without worrying about contiguous space — this eliminates external fragmentation entirely.

### 5.2 Page and Frame Sizes

Page (and frame) size is always a **power of 2**, typically between 512 B and 8 KiB (historical range; modern systems commonly use 4 KiB or larger).

**Tradeoffs of page size:**

| Aspect | Small Pages | Large Pages |
| :--- | :--- | :--- |
| Internal fragmentation | Less (last page partially filled) | More |
| Page table size | Larger (more entries needed) | Smaller |
| Disk I/O efficiency | Lower (more transfers) | Higher |
| Memory utilization | Better fit for small structures | May waste space |

> **[Supplementary]** Modern x86-64 systems support multiple page sizes: 4 KiB (standard), 2 MiB (large pages), and 1 GiB (huge pages). The Linux kernel calls these "huge pages" and uses them for performance-sensitive workloads to reduce TLB pressure.

### 5.3 Address Translation in Paging

A virtual address is split into two fields:

$$
\underbrace{p}_{\text{page number}} \;\|\; \underbrace{d}_{\text{offset within page}}
$$

Where:
- $p$ = index into the **page table**.
- $d$ = byte offset within the page (identical in the physical frame).

The page table maps $p \to f$ (page number to frame number). The physical address is:

$$
\text{Physical Address} = f \times \text{PageSize} + d
$$

Or equivalently, the physical address is simply $f \| d$ (frame number concatenated with offset).

### 5.4 Page Table Structure

The **page table** is a per-process data structure maintained by the OS in memory. Each entry contains:

| Field | Description |
| :--- | :--- |
| **Presence bit** (valid bit) | `1` = page is currently in a frame; `0` = page is on disk |
| **Frame number** | Physical frame where the page resides (valid only if presence bit = 1) |

> **[Key Insight]** Because the number of virtual pages far exceeds the number of physical frames, many entries will have presence bit = 0 at any given time.

### 5.5 Page Fault

A **page fault** occurs when a process accesses a virtual page whose presence bit is 0 (the page is not in RAM).

**Page fault handling sequence:**

1. CPU generates a page fault exception.
2. The OS suspends (blocks) the faulting process.
3. The OS locates the required page on disk.
4. If a free frame exists, the page is loaded into it.
5. If **no free frame** exists, the OS selects a **victim frame** using a replacement algorithm, writes it to disk if dirty, and loads the requested page into that frame.
6. The page table is updated (presence bit = 1, frame number set).
7. The faulting process is resumed.

### 5.6 Properties of Paging

- **No external fragmentation** — all frames are the same size; any frame fits any page.
- **Internal fragmentation exists** — the last page of a process may not be fully used. On average, half a page is wasted per process.
- A process may occupy **non-contiguous** frames.
- Each process maintains its own page table; multiple processes coexist in RAM via separate page tables.
- The MMU performs the $p \to f$ lookup on every memory access.

---

## 6. Segmentation

### 6.1 Concept

**Segmentation** divides the virtual address space into **variable-size** logical units called **segments**, each corresponding to a meaningful program structure (code, stack, heap, data, symbol table, etc.).

Unlike paging (invisible to the programmer), segmentation is **programmer-visible**: the programmer (or compiler) explicitly assigns code and data to named segments.

### 6.2 Segment Table

Each process has a **segment table** with one entry per segment:

| Field | Description |
| :--- | :--- |
| `base` | Starting physical address of the segment in RAM |
| `limit` | Length (size) of the segment in bytes |

A virtual address in a segmented system is a pair:

$$
\langle s,\; d \rangle
$$

Where $s$ = segment number, $d$ = byte offset within the segment.

**Translation:**

$$
\text{Physical Address} = \text{base}[s] + d \quad \text{(valid only if } d < \text{limit}[s]\text{)}
$$

If $d \geq \text{limit}[s]$, a **segmentation fault** (protection violation) is raised.

### 6.3 Properties of Segmentation

- Segments have **dynamic size** — they can grow or shrink (useful for stacks and heaps).
- **No internal fragmentation** — a segment is exactly as large as needed.
- **External fragmentation** can occur — variable-size segments leave gaps in physical memory over time.
- Each segment holds one **type** of information, making protection and sharing semantically natural:
  - Code segment: execute-only, shareable across processes running the same program.
  - Data segment: per-process, read-write.
- Multiple programs can share a code segment while maintaining separate data segments.

### 6.4 Paging vs. Segmentation

| Property | Paging | Segmentation |
| :--- | :--- | :--- |
| Programmer visibility | Invisible | Visible |
| Address space per process | 1 linear space | Multiple logical spaces |
| Block sizes | Fixed (all equal) | Variable |
| Internal fragmentation | Yes (last page) | No |
| External fragmentation | No | Yes |
| Total space can exceed physical RAM | Yes | Yes |
| Code/data protection separation | No | Yes |
| Variable-size structures (stack, heap) | Not directly | Yes |
| Sharing between processes | Difficult | Natural |
| Primary purpose | Large linear address space without extra RAM | Logical program organization, protection, sharing |

---

## 7. Page Replacement Algorithms

When a page fault occurs and all frames are occupied, the OS must select a **victim page** to evict. The choice determines performance (number of page faults).

### 7.1 FIFO (First-In, First-Out)

**Policy:** Evict the page that has been in memory the **longest** (the oldest resident page).

**Implementation:** Maintain a queue of pages ordered by arrival time. The page at the head of the queue is the next victim.

**Properties:**
- Simple to implement.
- Does not consider actual usage frequency — an old page may still be heavily used.
- Susceptible to **Belady's anomaly**: adding more frames can **increase** the number of page faults with certain reference strings.

> **[Supplementary]** Belady's anomaly is a counterintuitive result first demonstrated by László Bélády in 1969. It occurs specifically with FIFO (and certain other policies) but **never** with LRU or OPT, which are classified as "stack algorithms."

### 7.2 OPT (Optimal / Belady's Optimal Algorithm)

**Policy:** Evict the page that will **not be used for the longest time in the future** (the page whose next reference is farthest ahead in the reference string).

**Properties:**
- Produces the **minimum possible** number of page faults for any given reference string and frame count.
- **Not implementable** in practice — requires knowledge of the entire future reference string.
- Used as a **theoretical benchmark** to evaluate other algorithms.
- Not susceptible to Belady's anomaly (stack algorithm).

### 7.3 LRU (Least Recently Used)

**Policy:** Evict the page that has **not been used for the longest time in the past** (the page whose most recent reference is furthest back in time).

**Properties:**
- Approximates OPT using past behavior as a predictor of future behavior (principle of temporal locality).
- Not susceptible to Belady's anomaly (stack algorithm).
- More costly to implement exactly than FIFO — requires tracking the time of last access for each frame.
- In practice, approximated using hardware reference bits or software aging counters.

> **[Supplementary]** Common LRU approximation methods include:
> - **Reference bit scheme:** Each page has a 1-bit reference flag set by hardware on access; periodically cleared by the OS. Pages with cleared bits are candidates for eviction.
> - **Aging algorithm:** A software counter shifted right periodically; the reference bit is OR'd into the MSB. The page with the smallest counter value is evicted.
> - **Clock (second-chance) algorithm:** Pages are arranged in a circular list; a pointer advances and evicts the first page with reference bit = 0, giving pages with reference bit = 1 a second chance.

### 7.4 Algorithm Comparison

For reference string `4 3 1 5 1 2 3 6 7 4 2 5 6 1 3 4 7` with 4 frames:

| Algorithm | Page Faults |
| :--- | :--- |
| FIFO | 12 |
| OPT | 10 |
| LRU | 15 |

> **[Key Insight]** LRU performing worse than FIFO on a specific reference string is possible and does not contradict general performance claims. LRU outperforms FIFO on average over realistic workloads, but individual reference strings can favor either algorithm. OPT always achieves the minimum.

---

## Solved Exercises

### Exercise 1: FIFO — Reference String Trace (4 frames)

**Problem:** Given the reference string `4 3 1 5 1 2 3 6 7 4 2 5 6 1 3 4 7` with 4 frames (initially empty), simulate FIFO and count page faults.

**Solution:**

FIFO evicts the page that entered memory earliest. Maintain a queue ordered by insertion time.

| Step | Ref | Frame 1 | Frame 2 | Frame 3 | Frame 4 | Fault | Evicted | Queue (oldest→newest) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 4 | 4 | — | — | — | F | — | 4 |
| 2 | 3 | 4 | 3 | — | — | F | — | 4,3 |
| 3 | 1 | 4 | 3 | 1 | — | F | — | 4,3,1 |
| 4 | 5 | 4 | 3 | 1 | 5 | F | — | 4,3,1,5 |
| 5 | 1 | 4 | 3 | 1 | 5 | — | — | 4,3,1,5 |
| 6 | 2 | 2 | 3 | 1 | 5 | F | 4 | 3,1,5,2 |
| 7 | 3 | 2 | 3 | 1 | 5 | — | — | 3,1,5,2 |
| 8 | 6 | 2 | 6 | 1 | 5 | F | 3 | 1,5,2,6 |
| 9 | 7 | 2 | 6 | 7 | 5 | F | 1 | 5,2,6,7 |
| 10 | 4 | 2 | 6 | 7 | 4 | F | 5 | 2,6,7,4 |
| 11 | 2 | 2 | 6 | 7 | 4 | — | — | 2,6,7,4 |
| 12 | 5 | 5 | 6 | 7 | 4 | F | 2 | 6,7,4,5 |
| 13 | 6 | 5 | 6 | 7 | 4 | — | — | 6,7,4,5 |
| 14 | 1 | 5 | 1 | 7 | 4 | F | 6 | 7,4,5,1 |
| 15 | 3 | 5 | 1 | 3 | 4 | F | 7 | 4,5,1,3 |
| 16 | 4 | 5 | 1 | 3 | 4 | — | — | 4,5,1,3 |
| 17 | 7 | 7 | 1 | 3 | 4 | F | 5 | 5,1,3,7 |

**Total page faults: 12**

---

### Exercise 2: OPT — Reference String Trace (4 frames)

**Problem:** Same reference string `4 3 1 5 1 2 3 6 7 4 2 5 6 1 3 4 7`, 4 frames. Simulate OPT.

**Solution:**

OPT evicts the page whose next use is farthest in the future. When a page will never be used again, it is an immediate eviction candidate.

After the initial compulsory faults (loading 4, 3, 1, 5):

- Reference 2: frames = {4,3,1,5}. Next uses: 4→pos10, 3→pos7, 1→pos14(after evict), 5→pos12. Page 1 has farthest next use → evict 1. Load 2.
- Reference 3: hit (3 in frames).
- Reference 6: frames = {4,3,2,5}. Next uses: 4→pos10, 3→pos16(after), 2→pos11, 5→pos12. Page 3 has farthest next use → evict 3. Load 6.
- Reference 7: frames = {4,6,2,5}. Next uses: 4→pos10, 6→pos13, 2→pos11, 5→pos12. Page 6 has farthest → evict 6. Load 7.
- Reference 4: hit.
- Reference 2: hit.
- Reference 5: frames = {4,7,2,5}: hit? No — 5 was evicted. Frames = {4,7,2,...}. 5 not in frames → fault. Pages 2 and 5 will not reappear → evict either. Evict 2 or 5 (OPT is indifferent). Load 5.
- Reference 6: frames = {4,7,?,5}. 6 not present → fault. Next: 4→pos16, 7→pos17, 5 never again, current→6 never again. Evict 5 or 6 placeholder.

**Total page faults: 10** (minimum achievable for this string with 4 frames).

---

### Exercise 3: LRU — Reference String Trace (4 frames)

**Problem:** Same reference string, 4 frames. Simulate LRU.

**Solution:**

LRU evicts the page not accessed for the longest time. Track the recency of access.

| Step | Ref | Frames (set) | Fault | Evicted | LRU order (LRU→MRU) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 4 | {4} | F | — | 4 |
| 2 | 3 | {4,3} | F | — | 4,3 |
| 3 | 1 | {4,3,1} | F | — | 4,3,1 |
| 4 | 5 | {4,3,1,5} | F | — | 4,3,1,5 |
| 5 | 1 | {4,3,1,5} | — | — | 4,3,5,1 |
| 6 | 2 | {3,1,5,2} | F | 4 | 3,5,1,2 |
| 7 | 3 | {3,1,5,2} | — | — | 5,1,2,3 |
| 8 | 6 | {1,5,2,3}→{1,2,3,6} | F | 5 | 1,2,3,6 |
| 9 | 7 | {1,2,3,6}→{2,3,6,7} | F | 1 | 2,3,6,7 |
| 10 | 4 | {3,6,7,4} | F | 2 | 3,6,7,4 |
| 11 | 2 | {6,7,4,2} | F | 3 | 6,7,4,2 |
| 12 | 5 | {7,4,2,5} | F | 6 | 7,4,2,5 |
| 13 | 6 | {4,2,5,6} | F | 7 | 4,2,5,6 |
| 14 | 1 | {2,5,6,1} | F | 4 | 2,5,6,1 |
| 15 | 3 | {5,6,1,3} | F | 2 | 5,6,1,3 |
| 16 | 4 | {6,1,3,4} | F | 5 | 6,1,3,4 |
| 17 | 7 | {1,3,4,7} | F | 6 | 1,3,4,7 |

**Total page faults: 15**

> **[Key Insight]** For this particular reference string, LRU (15) performs worse than FIFO (12) and much worse than OPT (10). This is not a contradiction of LRU's general superiority — the reference string was designed for the lecture slides' FIFO example and has adversarial properties for LRU.

---

### Exercise 4: FIFO — Short Sequence with 3 Frames

**Problem:** Reference string `0 1 7 2 3 2 7 1 0 3`, 3 frames, initially empty. Count page faults **after** initial fill (i.e., count only replacement faults, not the first 3 compulsory faults).

**Solution:**

Load 0, 1, 7 (3 compulsory faults, not counted per problem statement). Frames = {0,1,7}, queue = [0,1,7].

| Step | Ref | Frames | Fault | Evicted | Queue |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 4 | 2 | {2,1,7} | F | 0 | [1,7,2] |
| 5 | 3 | {2,3,7} | F | 1 | [7,2,3] |
| 6 | 2 | {2,3,7} | — | — | [7,2,3] |
| 7 | 7 | {2,3,7} | — | — | [7,2,3] |
| 8 | 1 | {2,3,1} | F | 7 | [2,3,1] |
| 9 | 0 | {0,3,1} | F | 2 | [3,1,0] |
| 10 | 3 | {0,3,1} | — | — | [3,1,0] |

**Replacement faults: 4**

---

### Exercise 5: LRU — Short Sequence with 3 Frames

**Problem:** Same reference string `0 1 7 2 3 2 7 1 0 3`, 3 frames. Count replacement faults only.

**Solution:**

After loading 0, 1, 7: frames = {0,1,7}, recency order = [0,1,7] (0 = LRU, 7 = MRU).

| Step | Ref | Frames | Fault | Evicted | LRU→MRU |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 4 | 2 | {1,7,2} | F | 0 | [1,7,2] |
| 5 | 3 | {7,2,3} | F | 1 | [7,2,3] |
| 6 | 2 | {7,2,3} | — | — | [7,3,2] |
| 7 | 7 | {7,2,3} | — | — | [3,2,7] |
| 8 | 1 | {2,7,1} | F | 3 | [2,7,1] |
| 9 | 0 | {7,1,0} | F | 2 | [7,1,0] |
| 10 | 3 | {1,0,3} | F | 7 | [1,0,3] |

**Replacement faults: 5**

---

### Exercise 6: Segmentation Address Translation

**Problem:** A process has the following segment table:

| Segment | Base | Limit |
| :--- | :--- | :--- |
| 0 | 1400 | 1000 |
| 1 | 6300 | 400 |
| 2 | 4300 | 400 |
| 3 | 3200 | 1100 |
| 4 | 4700 | 1000 |

Translate virtual address $\langle 2, 53 \rangle$ and $\langle 3, 1500 \rangle$.

**Solution:**

**Address $\langle 2, 53 \rangle$:**
- Segment 2: base = 4300, limit = 400.
- Check: $53 < 400$ ✓ (valid).
- Physical address = $4300 + 53 = 4353$.

**Address $\langle 3, 1500 \rangle$:**
- Segment 3: base = 3200, limit = 1100.
- Check: $1500 < 1100$? No — $1500 \geq 1100$. **Segmentation fault** (access violation).

---

### Exercise 7: Page Table Address Translation

**Problem:** Page size = 4 KiB = $2^{12}$ bytes. A virtual address is 16 bits. The page table entry for virtual page 3 gives frame number 6. Translate virtual address `0x3A1F`.

**Solution:**

Virtual address `0x3A1F` in binary:

$$
0\!x\!3A1F = 0011\;1010\;0001\;1111_2
$$

With page size $= 2^{12}$, the offset field is 12 bits and the page number field is $16 - 12 = 4$ bits.

$$
p = 0011_2 = 3, \quad d = 1010\;0001\;1111_2 = 0\!xA1F
$$

Page table lookup: page 3 → frame 6.

$$
\text{Physical address} = 6 \times 4096 + 0\!xA1F = 0\!x6000 + 0\!xA1F = 0\!x6A1F
$$

---

### Exercise 8: Page Faults vs. Frame Count (LRU, FIFO, OPT)

**Problem:** Reference string `1 2 3 4 2 1 5 6 2 1 2 3 7 6 3 2 1 2 3 6`. Count page faults for 1–7 frames under LRU, FIFO, and OPT.

**Solution:** (From lecture slide answers — verified correct)

| Frames | LRU | FIFO | OPT |
| :--- | :--- | :--- | :--- |
| 1 | 20 | 20 | 20 |
| 2 | 17 | 18 | 15 |
| 3 | 15 | 16 | 11 |
| 4 | 10 | 14 | 8 |
| 5 | 8 | 10 | 7 |
| 6 | 7 | 9 | 7 |
| 7 | 7 | 7 | 7 |

**Observations:**
- At 7 frames all algorithms converge to 7 faults (equal to the number of distinct pages — every unique page causes exactly one compulsory fault).
- OPT consistently achieves the minimum; FIFO consistently performs worst.
- LRU and OPT both decrease monotonically with increasing frames (stack algorithms). FIFO also decreases here but is not guaranteed to be monotonic for all strings (Belady's anomaly).

---

## Exam Tips

### Exam Tip 1: Page Fault Mechanics

When simulating any replacement algorithm:
1. Always check **hit or miss first** — if the page is already in a frame, do nothing (no fault, no eviction).
2. Only when the page is **not present** and **all frames are full** do you need to apply the replacement policy.
3. Track the correct state **after** each step, not before.

**Common mistake:** Applying the replacement rule even when a free frame is available. Free frames are filled first; replacement only occurs when all frames are occupied.

### Exam Tip 2: FIFO Queue vs. LRU Stack

- **FIFO:** The queue tracks **insertion order**. When a page already in memory is re-accessed, the queue does **not** change.
- **LRU:** The recency stack tracks **last-access order**. When a page already in memory is re-accessed, it moves to the **most-recently-used** (MRU) end of the stack.

**Pattern recognition:** In LRU, a hit is never free in terms of bookkeeping — the accessed page's position in the recency order is updated. In FIFO, a hit requires no bookkeeping at all.

### Exam Tip 3: OPT Tie-Breaking

When two pages have equally distant next references (or both will never be referenced again), either may be evicted. Both choices yield the same total fault count. On exams, state your choice explicitly to avoid ambiguity.

### Exam Tip 4: Paging vs. Segmentation One-Liners

- **Paging:** Fixed-size, invisible, eliminates external fragmentation, has internal fragmentation.
- **Segmentation:** Variable-size, visible, eliminates internal fragmentation, has external fragmentation.
- Both allow the total virtual address space to exceed physical RAM.

### Exam Tip 5: Address Translation Steps

For paging problems, always verify you are splitting the address at the correct bit boundary. If page size $= 2^k$ bytes, the offset is exactly $k$ bits and the page number occupies all remaining high-order bits.

---
# OS_Lec09_NOTES.md
---

# Process Scheduling (CPU Scheduling)

This document covers single-processor CPU scheduling — the mechanisms, criteria, policies, and algorithms that determine which process runs next on the CPU. It maps directly to Chapter 9 of the Operating Systems course. The subject is a Type C (Engineering/Applied Systems) topic, meaning formal definitions and step-by-step mechanisms precede all worked examples.

---

## 1. Introduction

**Scheduling** is the OS function that decides the order and timing by which processes access the CPU in a single-processor system.

**Primary goals:**
- Maximize **CPU utilization** — keep the CPU as busy as possible.
- Maximize **throughput** — number of processes completed per unit time.
- Minimize **response time** — time from request submission to first response.

> **[Key Insight]** These goals are often in direct conflict. Maximizing throughput may require long, uninterrupted CPU bursts, while minimizing response time requires frequent context switching.

---

## 2. Performance Evaluation Criteria

| Criterion | Definition | Unit | Direction |
| :--- | :--- | :--- | :--- |
| **Fairness** | Every process gets regular CPU access; avoids starvation | — | Maximize |
| **Utilization** | Fraction of time a device (CPU) is in use: $\frac{t_{use}}{t_{total}}$ | % | Maximize |
| **Throughput** | Number of processes completed per unit time | processes/s | Maximize |
| **Turnaround Time (TAT)** | Total elapsed time from submission to completion; includes waiting | seconds | Minimize |
| **Waiting Time (WT)** | Time spent waiting in the ready queue | seconds | Minimize |
| **Response Time (RT)** | Time from submission until the process first occupies the CPU | seconds | Minimize |
| **Context Switch Overhead** | Time wasted switching execution context between processes | seconds | Minimize |
| **Scheduling Complexity** | Time required to select the next process from the ready list | seconds | Minimize |

**Key relation:**

$$
\text{Waiting Time} = \text{Turnaround Time} - \text{Burst Length}
$$

---

## 3. Optimization Criteria

**Maximize:**
- CPU utilization
- Throughput

**Minimize:**
- Turnaround time
- Waiting time
- Response time

> **[Key Insight]** These criteria frequently conflict. Improving one often degrades another. No single algorithm is optimal for all workloads.

---

## 4. Types of Scheduling

Three levels of scheduling exist in a multiprogramming OS:

### 4.1 Long-Term Scheduling

- Determines whether a **new process is admitted** to the system (enters the ready queue) or waits.
- Controls the **degree of multiprogramming**.
- Admitting more processes: fewer suspensions, better CPU utilization, but lower throughput per process and more context switches.
- Tries to maintain a **balance** between CPU-bound and I/O-bound processes.

### 4.2 Medium-Term Scheduling

- Decides which processes are **swapped in or out of main memory** (disk ↔ RAM).
- Related to the `ready-suspended` and `blocked-suspended` process states.
- Candidates for removal from memory: processes idle for long, low-priority, generating many page faults, or consuming large amounts of memory.
- Performed by **memory management software**.

### 4.3 Short-Term Scheduling (CPU Scheduling)

- The **primary focus** of this chapter.
- Selects which **ready process runs next** on the CPU.
- Also called **dispatching**; the component performing this is the **dispatcher**.
- Triggered by:
  - Clock interrupts
  - I/O interrupts
  - OS calls
  - Signals

**Dispatcher latency:** The time required for the dispatcher to stop one process and start another.

### 4.4 Short-Term Criteria

| Orientation | Criteria |
| :--- | :--- |
| User-oriented | Response time, Turnaround time |
| System-oriented | CPU utilization, Fairness, Throughput |

---

## 5. Scheduling Policies

### 5.1 Non-Preemptive Scheduling

- Once a process is in the **running** state, it continues until it **terminates voluntarily** or **blocks itself** waiting for I/O.
- Results in long waiting and response times.
- Simple to implement.
- **Not suitable for multi-user systems.**

### 5.2 Preemptive Scheduling

- The OS can **interrupt a running process** and move it back to the ready state.
- Possible causes of preemption:
  - Arrival of a higher-priority process
  - An interrupt occurs
  - A process changes state
  - A time limit (quantum) is exceeded
- Prevents CPU monopolization.
- Can lead to **race conditions** — resolved using process synchronization.

---

## 6. CPU-I/O Burst Cycle

Every process alternates between **CPU bursts** (computation) and **I/O bursts** (waiting for I/O).

- CPU bursts are generally **much shorter** than I/O bursts.
- A process **terminates during a CPU burst**.
- **CPU-bound** processes: long CPU bursts, few I/O bursts.
- **I/O-bound** processes: short CPU bursts, many I/O bursts.

> **[Key Insight]** The scheduler always operates per CPU burst, not per complete process execution. The decision of which process runs is re-evaluated at each burst boundary.

---

## 7. Priority Scheduling

- Implemented via **multiple ready queues**, each representing a priority level.
- The scheduler always picks a process from the **highest non-empty priority queue**.
- Low-priority processes may suffer **indefinite starvation**.
- Processes may be allowed to **dynamically change priority** based on time in the system or execution history (aging).

---

## 8. Scheduling Algorithms

### 8.1 First-Come, First-Served (FCFS)

**Type:** Non-preemptive

**Mechanism:**
- Processes are executed in the **order of arrival** (FIFO queue).
- If two processes arrive simultaneously, order is arbitrary (random tie-break).
- A process runs until it **voluntarily suspends** itself.

**Properties:**

| Property | Value |
| :--- | :--- |
| Queue type | FIFO |
| Preemption | No |
| Selection speed | O(1), independent of queue length |
| Starvation risk | Low |
| Suitable for | Batch systems |

**Disadvantages:**
- CPU-bound processes **monopolize** the CPU.
- I/O-bound processes wait even after their I/O completes (they lose their queue position when they block).
- **High variance** in average turnaround time.
- Unsuitable for interactive or time-sharing systems.

---

### 8.2 Shortest-Job-First (SJF)

**Type:** Non-preemptive (base form); preemptive variant = SRTF

**Mechanism:**
- From the ready queue, select the process with the **smallest CPU burst time**.
- If two processes have equal burst times, FCFS tie-breaking applies.
- Each process **declares** its CPU burst time to the scheduler.

**Properties:**

| Property | Value |
| :--- | :--- |
| Preemption | No (standard SJF) |
| Optimality | Gives **minimum average waiting time** for a given set of processes |
| Starvation risk | **High** — long processes may never run if short ones keep arriving |
| Burst time required | Yes — generally hard to know in advance |

> **[Key Insight]** SJF is provably optimal for minimizing average waiting time. However, its practical applicability is limited because CPU burst times are rarely known in advance and must be estimated.

> **[Supplementary]**
> In practice, the next CPU burst is estimated using an **exponential average** of past bursts:
> $$
> \tau_{n+1} = \alpha \cdot t_n + (1 - \alpha) \cdot \tau_n
> $$
> where $t_n$ is the actual $n$-th burst, $\tau_n$ is the $n$-th estimate, and $\alpha \in [0,1]$ controls the weight of recent history. A common value is $\alpha = 0.5$.

---

### 8.3 Shortest Remaining Time First (SRTF)

**Type:** Preemptive variant of SJF

**Mechanism:**
- At every new process arrival, compare the **remaining burst time** of the current process with the **burst time of the new arrival**.
- If the new process has a shorter remaining time, **preempt** the current process and run the new one.
- Remaining time = total burst time − time already spent on CPU.

**Properties:**

| Property | Value |
| :--- | :--- |
| Preemption | Yes (on every new arrival) |
| Decision point | Process completes burst OR new process arrives |
| Response time | Excellent for short processes |
| Context switch overhead | High |
| Starvation risk | High for long processes |
| Multi-user suitability | Good |

> **[Key Insight]** When all processes arrive simultaneously, SRTF degenerates into SJF. The distinction only matters when processes have different arrival times.

---

### 8.4 Round Robin (RR)

**Type:** Preemptive

**Mechanism:**
- Each process receives a fixed **time quantum** (time slice), typically 10–100 ms.
- Queue order is FIFO; after a quantum expires, a clock interrupt fires and the process is moved to the **end** of the ready queue.
- If a process completes before its quantum expires, it releases the CPU voluntarily.

**Properties:**

| Property | Value |
| :--- | :--- |
| Preemption | Yes (quantum expiry) |
| Starvation | None |
| Suitable for | Time-sharing, interactive systems |
| Fairness | High |
| Context switch overhead | Depends on quantum size |

**Quantum Size Trade-off:**

| Quantum | Effect |
| :--- | :--- |
| Very small | Many context switches → excessive overhead |
| Very large | Degenerates to FCFS |
| Optimal guideline | Choose $q$ such that **80–90% of processes** complete their burst within one quantum |

**Criticism — CPU-bound vs. I/O-bound fairness:**
- CPU-bound processes use the **full quantum** and re-enter at the back of the queue.
- I/O-bound processes use only a **fraction** of the quantum, then block for I/O; when they unblock, they re-enter behind processes that had full quanta.
- This implicitly **favors CPU-bound** processes.

**Virtual Round Robin (Solution):**
- When an I/O operation completes, the unblocked process moves into an **auxiliary queue** that has priority over the main ready queue.
- The process is dispatched for at most: $q - t_{used}$ (the remainder of the quantum it was interrupted during).
- This ensures I/O-bound processes are not penalized for blocking.

---

## 9. Algorithm Comparison

| Algorithm | Preemptive | Avg. Waiting Time | Starvation | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| FCFS | No | High (variable) | Rare | Simple batch systems |
| SJF | No | **Minimum** (optimal) | Yes (long jobs) | Batch, known burst times |
| SRTF | Yes | Near-minimum | Yes (long jobs) | Multi-user, short jobs dominant |
| RR | Yes | Medium | **No** | Interactive / time-sharing |

> **[Key Insight]** The best algorithm depends on system load, hardware support for the dispatcher, the relative weight of performance criteria, and the evaluation method used. No universally optimal algorithm exists.

---

## Solved Exercises

### Exercise 1: FCFS — Turnaround and Waiting Times

**Problem:**
Five processes arrive at time 0 in order P1, P2, P3, P4, P5 with burst times:

| Process | Burst Time |
| :--- | :--- |
| P1 | 10 |
| P2 | 1 |
| P3 | 2 |
| P4 | 1 |
| P5 | 5 |

Calculate turnaround and waiting times for FCFS.

**Solution:**

FCFS execution order (arrival order): P1 → P2 → P3 → P4 → P5

Completion times:
- P1 finishes at $t = 10$
- P2 finishes at $t = 11$
- P3 finishes at $t = 13$
- P4 finishes at $t = 14$
- P5 finishes at $t = 19$

Turnaround Time ($TAT = \text{completion} - \text{arrival}$, all arrive at 0):

| Process | Burst | TAT | WT = TAT − Burst |
| :--- | :--- | :--- | :--- |
| P1 | 10 | 10 | 0 |
| P2 | 1 | 11 | 10 |
| P3 | 2 | 13 | 11 |
| P4 | 1 | 14 | 13 |
| P5 | 5 | 19 | 14 |
| **Avg** | | **13.4** | **9.6** |

---

### Exercise 2: SJF (Non-Preemptive) — Same Process Set

**Problem:** Same 5 processes from Exercise 1, apply SJF (all arrive at $t = 0$).

**Solution:**

Sort by burst time: P2(1), P4(1), P3(2), P5(5), P1(10)

Execution: P2 → P4 → P3 → P5 → P1

| Process | Burst | Completion | TAT | WT |
| :--- | :--- | :--- | :--- | :--- |
| P2 | 1 | 1 | 1 | 0 |
| P4 | 1 | 2 | 2 | 1 |
| P3 | 2 | 4 | 4 | 2 |  
| P5 | 5 | 9 | 9 | 4 |
| P1 | 10 | 19 | 19 | 9 |
| **Avg** | | | **7.0** | **3.2** |

SJF reduces average waiting time from 9.6 (FCFS) to **3.2** — a significant improvement.

---

### Exercise 3: Round Robin (q = 1) — Same Process Set

**Problem:** Same 5 processes, RR with time quantum = 1 unit.

**Solution:**

Execution sequence (all arrive at 0, FIFO initial order P1–P5):
```
t=0:P1, t=1:P2, t=2:P3, t=3:P4, t=4:P5, t=5:P1, t=6:P3, t=7:P5, t=8:P1, t=9:P5,
t=10:P1, t=11:P5, t=12:P1, t=13:P5, t=14:P1, t=15:P1, t=16:P1, t=17:P1, t=18:P1
```

P2 completes at $t=2$, P4 at $t=4$, P3 at $t=7$, P5 at $t=14$, P1 at $t=19$.

| Process | Burst | TAT | WT |
| :--- | :--- | :--- | :--- |
| P1 | 10 | 19 | 9 |
| P2 | 1 | 2 | 1 |
| P3 | 2 | 7 | 5 |
| P4 | 1 | 4 | 3 |
| P5 | 5 | 14 | 9 |
| **Avg** | | **9.2** | **5.4** |

---

### Exercise 4: SJF vs. SRTF Comparison (Different Arrival Times)

**Problem:**

| Process | Arrival | Burst |
| :--- | :--- | :--- |
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

Compute average waiting time for SJF (non-preemptive) and SRTF.

**Solution — SJF (Non-Preemptive):**

At $t=0$: only P1 is ready → P1 runs until $t=7$.
At $t=7$: P2(4), P3(1), P4(4) are ready → select P3 (burst=1) → runs $t=7$ to $t=8$.
At $t=8$: P2(4), P4(4) → tie → select P2 → runs $t=8$ to $t=12$.
At $t=12$: P4(4) → runs $t=12$ to $t=16$.

Gantt: `P1(0-7) | P3(7-8) | P2(8-12) | P4(12-16)`

| Process | Arrival | Finish | TAT | WT = TAT − Burst |
| :--- | :--- | :--- | :--- | :--- |
| P1 | 0 | 7 | 7 | 0 |
| P2 | 2 | 12 | 10 | 6 |
| P3 | 4 | 8 | 4 | 3 |
| P4 | 5 | 16 | 11 | 7 |
| **Avg** | | | | **4.0** |

**Solution — SRTF (Preemptive):**

At $t=0$: P1 starts (remaining=7).
At $t=2$: P2 arrives (burst=4) < P1 remaining (5) → preempt P1. P2 runs.
At $t=4$: P3 arrives (burst=1) < P2 remaining (2) → preempt P2. P3 runs.
At $t=5$: P3 finishes. P4 arrives (burst=4). Compare P2 remaining (2) vs P4 (4) → P2 runs.
At $t=7$: P2 finishes. P1 remaining=5, P4=4 → P4 runs.
At $t=11$: P4 finishes. P1 remaining=5 → P1 runs.
At $t=16$: P1 finishes.

Gantt: `P1(0-2) | P2(2-4) | P3(4-5) | P2(5-7) | P4(7-11) | P1(11-16)`

| Process | Arrival | Finish | TAT | WT = TAT − Burst |
| :--- | :--- | :--- | :--- | :--- |
| P1 | 0 | 16 | 16 | 9 |
| P2 | 2 | 7 | 5 | 1 |
| P3 | 4 | 5 | 1 | 0 |
| P4 | 5 | 11 | 6 | 2 |
| **Avg** | | | | **3.0** |

SRTF achieves average WT = 3.0 vs SJF's 4.0, confirming SRTF's theoretical advantage.

---

### Exercise 5: FCFS — Exercise 2 from Lecture (5 Processes, Sequential Arrival)

**Problem:**

| Process | Arrival | Burst |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 0 | 6 |
| C | 0 | 4 |
| D | 0 | 5 |
| E | 0 | 2 |

Apply FCFS. Compute average TAT.

**Solution:**

All arrive at $t=0$, executed in order A, B, C, D, E.

Gantt: `A(0-3) | B(3-9) | C(9-13) | D(13-18) | E(18-20)`

| Process | Finish | TAT |
| :--- | :--- | :--- |
| A | 3 | 3 |
| B | 9 | 9 |
| C | 13 | 13 |
| D | 18 | 18 |
| E | 20 | 20 |

$$
\text{Average TAT} = \frac{3 + 9 + 13 + 18 + 20}{5} = \frac{63}{5} = 12.6 \text{ time units}
$$

---

### Exercise 6: SJF — Exercise 2 from Lecture (Same 5 Processes)

**Problem:** Same 5 processes as Exercise 5. Apply SJF.

**Solution:**

Sort by burst: E(2), A(3), C(4), D(5), B(6)

Gantt: `E(0-2) | A(2-5) | C(5-9) | D(9-14) | B(14-20)`

| Process | Finish | TAT |
| :--- | :--- | :--- |
| E | 2 | 2 |
| A | 5 | 5 |
| C | 9 | 9 |
| D | 14 | 14 |
| B | 20 | 20 |

$$
\text{Average TAT} = \frac{2 + 5 + 9 + 14 + 20}{5} = \frac{50}{5} = 10 \text{ time units}
$$

---

### Exercise 7: RR — Exercise 2 from Lecture (q = 2)

**Problem:** Same 5 processes, all arrive at $t=0$. Apply RR with quantum $q = 2$.

**Solution:**

Initial order: A(3), B(6), C(4), D(5), E(2)

Step-by-step:
```
t=0-2:  A runs, A remaining=1
t=2-4:  B runs, B remaining=4
t=4-6:  C runs, C remaining=2
t=6-8:  D runs, D remaining=3
t=8-10: E runs, E remaining=0 → E DONE at t=10
t=10-11: A runs (1 remaining), A DONE at t=11
t=11-13: B runs, B remaining=2
t=13-15: C runs, C remaining=0 → C DONE at t=15
t=15-17: D runs, D remaining=1
t=17-19: B runs, B remaining=0 → B DONE at t=19
t=19-20: D runs (1 remaining), D DONE at t=20
```

| Process | Burst | Finish | TAT |
| :--- | :--- | :--- | :--- |
| A | 3 | 11 | 11 |
| B | 6 | 19 | 19 |
| C | 4 | 15 | 15 |
| D | 5 | 20 | 20 |
| E | 2 | 10 | 10 |

$$
\text{Average TAT} = \frac{11 + 19 + 15 + 20 + 10}{5} = \frac{75}{5} = 15 \text{ time units}
$$

> **[Key Insight]** For this particular workload, RR (q=2) performs worst on average TAT (15.0) compared to FCFS (12.6) and SJF (10.0). This is expected: RR is optimized for fairness and response time, not for minimizing TAT.

---

### Exercise 8: SRTF with Different Arrival Times

**Problem:**

| Process | Arrival | Burst |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

Apply SRTF. Compute average TAT.

**Solution:**

Step-by-step (tracking remaining times):
- $t=0$: A starts (remaining=3)
- $t=2$: B arrives (6). A remaining=1. $1 < 6$ → A continues
- $t=3$: A finishes. B runs (remaining=6)
- $t=4$: C arrives (4). B remaining=5. $4 < 5$ → preempt B, run C
- $t=6$: D arrives (5). C remaining=2. $2 < 5$ → C continues
- $t=8$: C finishes. E arrives (2). B remaining=5, D remaining=5. $2 < 5$ → run E
- $t=10$: E finishes. B remaining=5, D remaining=5 → run B (arrived first)
- $t=15$: B finishes. D remaining=5 → run D
- $t=20$: D finishes.

Gantt: `A(0-3) | B(3-4) | C(4-6) | [B preempted] | C(6-8) | E(8-10) | B(10-15) | D(15-20)`

| Process | Arrival | Finish | TAT |
| :--- | :--- | :--- | :--- |
| A | 0 | 3 | 3 |
| B | 2 | 15 | 13 |
| C | 4 | 8 | 4 |
| D | 6 | 20 | 14 |
| E | 8 | 10 | 2 |

$$
\text{Average TAT} = \frac{3 + 13 + 4 + 14 + 2}{5} = \frac{36}{5} = 7.2 \text{ time units}
$$

This matches the lecture result directly.

---

## Exam Tip: Common Mistakes and Pattern Recognition

**1. Confusing TAT and WT:**

$$
WT = TAT - \text{Burst Time}
$$

TAT measures from submission to completion. WT measures only idle time in the ready queue. Never subtract arrival time from WT directly.

**2. SRTF preemption condition:**
Preemption occurs when `new_burst < current_remaining`, not `<=`. Equal remaining times do not cause preemption.

**3. SJF with simultaneous arrivals = SRTF:**
When all processes arrive at $t=0$, SRTF never preempts (no new arrivals during execution), so it gives identical results to SJF.

**4. RR quantum selection:**
If a quantum is larger than all burst times, RR = FCFS. Always check whether the quantum causes preemption for each process.

**5. Starvation:**
- FCFS: rarely starves (eventually every process runs).
- SJF/SRTF: **can starve** long processes if short ones keep arriving.
- RR: **never starves** (every process gets regular CPU time).
- Priority: **can starve** low-priority processes — solved by **aging** (gradually raising priority of waiting processes).

**6. Exam pattern — comparative table questions:**
Given a process set, you will almost always be asked to compute TAT and WT for 2–3 algorithms and compare their averages. Always draw the Gantt chart first; computing directly from tables is error-prone.

---
# 1_Introduction_to_UNIX.md
---

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

---
# 2_UNIX_File_System_Navigation.md
---

# 2. UNIX File System Navigation

***

## Understanding the File System

The file system is the component of the operating system responsible for organizing, storing, and retrieving files. In UNIX and Linux, the file system is strictly hierarchical (tree-shaped), with all files and directories stemming from a single origin.

***

## Unix File Types

While UNIX adheres to the philosophy that "everything is a file," it distinguishes between several file types:

- **Regular Files (`-`):** Standard files containing data, text, or executable code.
- **Directories (`d`):** Special files that contain lists of other files and directories.
- **Symbolic Links (`l`):** Pointers to other files or directories.
- **Special Files (`c` or `b`):** Represent hardware devices (e.g., terminals, hard drives) usually found in `/dev`.
- **Pipes and Sockets (`p` or `s`):** Used for inter-process communication.

***

## The Hierarchy and Important Directories

The top level of the hierarchy is the **root directory**, represented by `/`. 

| Directory | Common Contents |
|-----------|-----------------|
| `/` | The absolute root of the file system. |
| `/bin` | Essential executable commands (e.g., `ls`, `cp`, `mkdir`). |
| `/dev` | Device files representing hardware. |
| `/etc` | System-wide configuration files. |
| `/home` | User home directories (e.g., `/home/username`). |
| `/tmp` | Temporary files, often cleared when the system reboots. |
| `/var` | Variable data files, such as logs and databases. |
| `/usr` | Secondary hierarchy for user data and read-only applications. |

***

## Pathnames: Absolute vs. Relative

A pathname is the string of characters used to identify a location in the directory tree. Understanding the difference between absolute and relative pathnames is critical for navigation.

### Absolute Pathnames

An absolute path always defines the location starting from the root directory (`/`). It is a complete path that will work regardless of your current working directory.

**Characteristics:**
- Always begins with a forward slash `/`.
- Uniquely identifies a single file or directory.

**Examples:**
```sh
/home/user1/documents/report.txt
/etc/ssh/sshd_config
/var/log/syslog
```

### Relative Pathnames

A relative path defines the location starting from your **Current Working Directory (CWD)**. It is relative to where you currently are in the file system.

**Characteristics:**
- Never begins with a forward slash `/`.
- Can be shorter and more convenient.

**Special Navigational Symbols:**
| Symbol | Meaning |
|--------|---------|
| `.` | The current directory. |
| `..` | The parent directory (one level up). |
| `~` | The current user's home directory. |

**Examples (Assuming CWD is `/home/user1/`):**
```sh
documents/report.txt     # Refers to /home/user1/documents/report.txt
./documents/report.txt   # Identical to the above
../user2/file.txt        # Refers to /home/user2/file.txt
../../etc/passwd         # Refers to /etc/passwd
```

***

## Navigation Commands

### `pwd` — Print Working Directory

Displays the absolute pathname of your current location in the file system.

```sh
pwd
```
```text
/home/user1/documents
```

### `cd` — Change Directory

Changes your current working directory. It accepts both absolute and relative paths.

**Syntax:**
```sh
cd <path>
```

**Common Usage Patterns:**
| Command | Action |
|---------|--------|
| `cd /etc` | Move to `/etc` (Absolute path). |
| `cd documents` | Move to `documents` within the current directory (Relative path). |
| `cd ..` | Move up one directory level. |
| `cd ../..` | Move up two directory levels. |
| `cd ~` or `cd` | Return immediately to your home directory. |
| `cd -` | Return to the previous directory you were in. |

***

## Directory Management Commands

### `mkdir` — Make Directory

Creates one or more new directories.

**Syntax:**
```sh
mkdir <directory_name>
```

**Examples:**
```sh
mkdir projects           # Creates 'projects' in the current directory
mkdir /tmp/testdir       # Creates 'testdir' in /tmp using an absolute path
```

**Creating Nested Directories:**
If you attempt to create a directory inside a parent that does not exist, `mkdir` will fail. Use the `-p` (parents) flag to create the entire path structure at once.

```sh
mkdir -p projects/python/scripts
```
This command ensures that `projects`, `python`, and `scripts` are all created without errors.

### `rmdir` — Remove Directory

Removes empty directories.

**Syntax:**
```sh
rmdir <directory_name>
```

**Important Caveat:**
`rmdir` will only succeed if the target directory contains absolutely no files or subdirectories. If the directory is not empty, you will receive an error:
```text
rmdir: failed to remove 'projects': Directory not empty
```
To remove a directory and all of its contents simultaneously, you must use the `rm` command with recursive flags (covered in the next section).

***

## Summary of Navigation Workflow

1. Use `pwd` to confirm where you are.
2. Use `cd` to move around the system.
3. Use `mkdir` to create new organizational folders.
4. Remember to use `.` and `..` to reference relative locations quickly without typing long absolute paths.

---
# 3_UNIX_File_and_Directory_Management.md
---

# 3. UNIX File and Directory Management

***

## File and Directory Deletion

### `rm` — Remove Files and Directories

The `rm` command deletes files permanently. Unlike modern graphical desktop environments, the UNIX terminal does not have a "Recycle Bin." Once a file is removed with `rm`, it is generally unrecoverable.

**Syntax:**
```sh
rm <file_name>
```

**Common Flags:**

| Flag | Description |
|------|-------------|
| `-i` | Interactive mode. Prompts for confirmation before deleting each file. |
| `-r` or `-R` | Recursive mode. Required to delete directories and their contents. |
| `-f` | Force mode. Ignores nonexistent files and never prompts for confirmation. Use with extreme caution. |

**Examples:**

```sh
rm report.txt              # Deletes a single file silently
rm -i important_data.csv   # Asks for confirmation before deletion
```
```text
rm: remove regular file 'important_data.csv'? y
```

**Deleting Directories:**
To delete a directory that contains files, you cannot use `rmdir`. You must use `rm -r`.

```sh
rm -r old_project/         # Deletes the directory and everything inside it
rm -ri old_project/        # Deletes recursively, but asks for confirmation at each step
```

**Warning:** Running `rm -rf /` is catastrophically destructive as it attempts to forcefully delete the entire file system starting from the root directory. Never run this command.

***

## Copying Files and Directories

### `cp` — Copy

The `cp` command duplicates files or directories from a source to a destination.

**Syntax:**
```sh
cp <source> <destination>
```

**Common Flags:**

| Flag | Description |
|------|-------------|
| `-r` or `-R` | Recursive mode. Required when copying directories. |
| `-i` | Interactive mode. Prompts before overwriting an existing file at the destination. |
| `-v` | Verbose mode. Prints the name of each file as it is copied. |

**Usage Scenarios:**

1. **Copying a single file to a new name:**
   ```sh
   cp original.txt backup.txt
   ```

2. **Copying a file into another directory:**
   ```sh
   cp original.txt /tmp/
   ```

3. **Copying multiple files into a directory:**
   ```sh
   cp file1.txt file2.txt /backup_dir/
   ```

4. **Copying an entire directory:**
   ```sh
   cp -r project_source/ project_backup/
   ```

**Overwriting Files:**
If a file with the target name already exists at the destination, `cp` will silently overwrite it by default. Using the `-i` flag prevents accidental data loss.

***

## Moving and Renaming

### `mv` — Move / Rename

The `mv` command is used for two distinct operations: moving files from one location to another, and renaming files. It does not require a recursive flag for directories.

**Syntax:**
```sh
mv <source> <destination>
```

**Usage Scenarios:**

1. **Renaming a file (moving it within the same directory):**
   ```sh
   mv old_name.txt new_name.txt
   ```

2. **Moving a file to another directory:**
   ```sh
   mv data.csv /home/user/archives/
   ```

3. **Moving and renaming simultaneously:**
   ```sh
   mv /tmp/download.zip /home/user/software_v2.zip
   ```

4. **Moving a directory:**
   ```sh
   mv my_project/ /var/www/html/
   ```

***

## Listing Directory Contents

### `ls` — List

The `ls` command displays the contents of a directory. By default, it lists files in the current working directory in alphabetical order.

**Syntax:**
```sh
ls [options] [directory]
```

**Common Flags:**

| Flag | Description |
|------|-------------|
| `-l` | Long listing format. Displays permissions, ownership, size, and timestamps. |
| `-a` | Show all files, including hidden files (those starting with a dot `.`). |
| `-h` | Human-readable file sizes (e.g., 1K, 234M, 2G). Often used with `-l`. |
| `-R` | Recursive listing. Lists the contents of all subdirectories. |
| `-t` | Sort by modification time, newest first. |

**Understanding `ls -l` Output:**

Running `ls -l` produces a detailed output row for each file:

```text
-rw-r--r-- 1 user group 1024 Oct 24 10:00 document.txt
drwxr-xr-x 2 user group 4096 Oct 24 10:05 my_folder
```

**Field Breakdown:**
1. **Type and Permissions:** The first 10 characters (e.g., `-rw-r--r--` or `drwxr-xr-x`). The first character indicates the file type (`-` for file, `d` for directory). The next 9 characters represent read, write, and execute permissions.
2. **Hard Links:** The number of hard links pointing to the inode.
3. **Owner:** The user who owns the file.
4. **Group:** The group that owns the file.
5. **Size:** The file size in bytes.
6. **Modification Date:** The date and time the file was last modified.
7. **Name:** The file or directory name.

**Combining Flags:**
Flags can be combined to form powerful commands.
```sh
ls -la       # Long listing, including hidden files
ls -lh       # Long listing with human-readable file sizes
ls -lt       # Long listing sorted by newest modification time
```

---
# 4_UNIX_Access_Permissions.md
---

# 4. UNIX Access Permissions

***

## The Permission Model

UNIX is a multi-user operating system. To maintain security and privacy, every file and directory is protected by a set of permissions that dictate who can read, modify, or execute them.

Permissions are categorized into three ownership tiers:

1. **User (Owner - `u`):** The account that owns the file (usually the creator).
2. **Group (`g`):** A defined collection of users who share access rights to the file.
3. **Other (`o`):** Everyone else on the system who is not the owner and not in the group.

For each of these tiers, three types of permissions can be granted:

| Permission | Symbol | Value | Meaning on a File | Meaning on a Directory |
|------------|--------|-------|-------------------|------------------------|
| **Read** | `r` | 4 | View file contents. | List the files inside the directory (`ls`). |
| **Write** | `w` | 2 | Modify or delete file contents. | Create, delete, or rename files inside the directory. |
| **Execute**| `x` | 1 | Run the file as a program or script. | Traverse the directory (access files within it). |

***

## Interpreting Permission Strings

When you run `ls -l`, the first column displays a 10-character string representing the file type and permissions.

```text
-rwxr-x--- 1 user1 staff  1024 Oct 24 file.txt
drwxr-xr-x 2 user1 staff  4096 Oct 24 folder/
```

**Deconstructing `-rwxr-x---`:**
- `[` `-` `]` Type: Regular file.
- `[` `rwx` `]` User (Owner): Has Read, Write, and Execute permissions.
- `[` `r-x` `]` Group: Has Read and Execute permissions, but cannot Write (modify).
- `[` `---` `]` Other: Has no access whatsoever.

***

## Directories: The `Execute` Bit

A common point of confusion is how permissions apply to directories.

- To use `cd` to enter a directory, you **must** have Execute (`x`) permission on it.
- To see the names of files inside a directory (using `ls`), you need Read (`r`) permission.
- However, to read the attributes of the files inside (using `ls -l`), you need **both** Read and Execute permissions on the directory.
- To create or delete a file inside a directory, you need Write (`w`) and Execute (`x`) permissions on the directory, regardless of the permissions of the file itself.

***

## Modifying Permissions: `chmod`

The `chmod` (change mode) command is used to alter permissions. Only the file owner or the `root` user can change a file's permissions.

There are two primary methods to use `chmod`: Numeric (Octal) and Symbolic.

### Method 1: Numeric (Octal) Notation

This method uses numbers to represent permission sets. You sum the values of the permissions you want to grant for each tier.
- Read = 4
- Write = 2
- Execute = 1

**Examples:**
- `rwx` = 4 + 2 + 1 = **7**
- `rw-` = 4 + 2 + 0 = **6**
- `r-x` = 4 + 0 + 1 = **5**
- `r--` = 4 + 0 + 0 = **4**

You construct a 3-digit number representing User, Group, and Other:

```sh
chmod 755 script.sh
```
*Sets `rwxr-xr-x`. Owner can do everything; Group and Other can read and execute.*

```sh
chmod 644 document.txt
```
*Sets `rw-r--r--`. Owner can read/write; Group and Other can only read. (Standard file permission)*

```sh
chmod 700 private_folder/
```
*Sets `rwx------`. Only the owner has access. (Standard for private directories)*

### Method 2: Symbolic Notation

This method uses letters to selectively add or remove permissions without affecting others.

**Syntax:** `chmod [who][operator][permission] file`

- **Who:** `u` (user), `g` (group), `o` (other), `a` (all)
- **Operator:** `+` (add), `-` (remove), `=` (set exactly)
- **Permission:** `r`, `w`, `x`

**Examples:**

```sh
chmod u+x script.sh         # Add execute permission for the owner
chmod go-w file.txt         # Remove write permission for group and others
chmod a+r public.txt        # Add read permission for everyone
chmod g=rx shared_dir/      # Set group permission exactly to read and execute
chmod u=rwx,g=rx,o=r file   # Set multiple permissions separated by commas
```

***

## Ownership Commands

### `chown` — Change Owner

Changes the user ownership of a file or directory.

```sh
chown user2 report.txt              # Change owner to user2
chown user2:finance report.txt      # Change owner to user2 and group to finance
chown -R user2 project_dir/         # Recursively change ownership for a directory
```

### `chgrp` — Change Group

Changes only the group ownership of a file or directory.

```sh
chgrp finance report.txt
```

*(Note: In most Linux systems, including JSLinux, changing ownership usually requires `root` privileges via `sudo` or logging in as root.)*

***

## Default Permissions: `umask`

When you create a new file or directory, the system assigns default permissions based on the `umask` (user file-creation mode mask).

The default maximum permissions are `666` for files and `777` for directories. The `umask` value is *subtracted* from these maximums.

If your `umask` is `022`:
- New files will have `666 - 022 = 644` (`rw-r--r--`).
- New directories will have `777 - 022 = 755` (`rwxr-xr-x`).

You can check or set your umask:
```sh
umask        # Displays current umask (e.g., 0022)
umask 027    # Sets new umask, resulting in files (640) and dirs (750)
```

---
# 5_UNIX_File_Viewing_and_Linking.md
---

# 5. UNIX File Viewing and Linking

***

## Viewing File Contents

### `cat` — Concatenate and Print

The `cat` command is primarily used to display the entire contents of a file on the terminal screen.

**Syntax:**
```sh
cat <file_name>
cat file1 file2       # Displays the contents of file1 followed immediately by file2
```

**Common Flags:**
- `-n`: Numbers all output lines.
- `-A`: Displays non-printable characters (e.g., ends of lines as `$`, tabs as `^I`).

*(Note: `cat` is not ideal for very large files because it prints everything at once, causing the text to scroll by too quickly to read. For large files, pagers like `less` or `more` are preferred.)*

### `less` and `more` — Pagers

Pagers allow you to view the contents of a file one screen at a time.

```sh
less large_log.txt
```
**Navigation in `less`:**
- `Spacebar` or `Page Down`: Scroll down one screen.
- `b` or `Page Up`: Scroll up one screen.
- `Down Arrow` / `Up Arrow`: Scroll line by line.
- `q`: Quit and return to the prompt.
- `/pattern`: Search forward for a specific word or pattern.

### `head` — View the Beginning of a File

Displays the first few lines of a file (default is 10 lines).

**Syntax:**
```sh
head <file_name>
head -n 20 <file_name>    # Displays the first 20 lines
head -c 50 <file_name>    # Displays the first 50 bytes/characters
```

### `tail` — View the End of a File

Displays the last few lines of a file (default is 10 lines).

**Syntax:**
```sh
tail <file_name>
tail -n 15 <file_name>    # Displays the last 15 lines
```

**Following a file:**
The `-f` (follow) flag is incredibly useful for monitoring log files. It keeps the file open and displays new lines as they are appended in real-time.
```sh
tail -f /var/log/syslog
```
*(Press `Ctrl + C` to stop following the file.)*

***

## File Analysis Commands

### `wc` — Word Count

Counts the number of lines, words, and characters in a file.

**Syntax:**
```sh
wc <file_name>
```

**Output example:**
```text
  45  130  850 report.txt
```
*(Represents 45 lines, 130 words, 850 characters)*

**Common Flags:**
- `-l`: Print only the line count.
- `-w`: Print only the word count.
- `-c`: Print only the byte/character count.

### `sort` — Sort Lines of Text

Sorts the contents of a text file line by line. By default, it sorts in lexicographical (alphabetical) ascending order.

**Syntax:**
```sh
sort data.txt
```

**Common Flags:**
- `-r`: Reverse the sorting order (descending).
- `-n`: Sort numerically rather than alphabetically (e.g., treats "10" as greater than "2").
- `-u`: Unique. Removes duplicate lines from the output.

***

## Linking Files

UNIX allows you to create links to files. A link is essentially a pointer or an alias to an existing file. There are two types: Hard Links and Symbolic (Soft) Links.

### Symbolic Links (Soft Links)

A symbolic link is a special type of file that simply contains the path to another file. If you delete the original file, the symbolic link becomes "broken" or "dangling."

**Creating a Symbolic Link:**
```sh
ln -s <target_file> <link_name>
```

**Examples:**
```sh
ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/myapp.conf
```
*(Creates a symlink in `sites-enabled` pointing to the actual configuration file.)*

When you run `ls -l`, symbolic links are indicated by an `l` in the permissions string and an arrow `->` pointing to the target:
```text
lrwxrwxrwx 1 user user 35 Oct 24 10:00 myapp.conf -> /etc/nginx/sites-available/myapp.conf
```

### Hard Links

A hard link creates a direct pointer to the underlying data (inode) on the hard drive. The system treats a hard link identically to the original file. If you delete the original file, the data remains accessible via the hard link until all hard links to that data are deleted.

**Creating a Hard Link:**
```sh
ln <target_file> <link_name>
```

**Differences between Hard and Soft Links:**
- Hard links cannot cross different file systems or partitions; soft links can.
- Hard links cannot point to directories; soft links can.
- Soft links are far more common in everyday UNIX usage.

---
# 6_UNIX_IO_Redirection_and_Pipes.md
---

# 6. UNIX I/O Redirection and Pipes

***

## Standard I/O Streams

In UNIX, every command-line program automatically opens three standard streams (files) when it runs:

| Stream Name                    | File Descriptor | Default Device  | Purpose                                                |
| ------------------------------ | --------------- | --------------- | ------------------------------------------------------ |
| **Standard Input (`stdin`)**   | 0               | Keyboard        | Where the program reads input from.                    |
| **Standard Output (`stdout`)** | 1               | Terminal Screen | Where the program sends its normal output.             |
| **Standard Error (`stderr`)**  | 2               | Terminal Screen | Where the program sends error and diagnostic messages. |

I/O Redirection allows you to detach these streams from their default devices and connect them to files or other programs.

***

## Output Redirection

### Overwrite Output (`>`)

Redirects `stdout` to a file. If the file does not exist, it is created. **If the file already exists, it is completely overwritten.**

**Syntax:**
```sh
command > filename
```

**Examples:**
```sh
echo "Hello, World!" > greeting.txt
ls -l > directory_listing.txt
```
*(The output is not printed to the screen; it goes directly into the file.)*

### Append Output (`>>`)

Redirects `stdout` to a file. **If the file exists, the new output is appended to the end of the file.** It does not overwrite the existing contents.

**Syntax:**
```sh
command >> filename
```

**Example:**
```sh
echo "New line of text" >> greeting.txt
```

***

## Error Redirection

By default, error messages bypass standard output redirection and still print to the screen. To capture errors in a file, you must redirect `stderr` specifically.

### Redirect `stderr` (`2>`)

**Syntax:**
```sh
command 2> error_log.txt
```

**Example:**
```sh
ls /nonexistent_directory 2> errors.txt
```

### Redirect both `stdout` and `stderr`

You can redirect both streams to the same file.

**Syntax:**
```sh
command > output_and_errors.txt 2>&1
```
*(This tells the shell to send descriptor 2 to wherever descriptor 1 is currently pointing.)*

Modern bash shells also support a shorthand for this:
```sh
command &> output_and_errors.txt
```

***

## Input Redirection

### Redirect `stdin` (`<`)

Feeds the contents of a file into a command as if it were typed on the keyboard.

**Syntax:**
```sh
command < input_file
```

**Example:**
```sh
wc -l < data.txt
```
*(Counts the lines in `data.txt`. Note: Unlike `wc -l data.txt`, using input redirection will only output the number, without printing the filename.)*

***

## Pipes (`|`)

Pipes are one of the most powerful features in UNIX. A pipe connects the `stdout` of one command directly to the `stdin` of another command. This allows you to chain small programs together to perform complex tasks without creating temporary files.

**Syntax:**
```sh
command1 | command2 | command3
```

**How it works:**
The output of `command1` becomes the input for `command2`. The output of `command2` becomes the input for `command3`. Only the final output is printed to the screen.

**Examples:**

1. **Viewing long output:**
   ```sh
   ls -l /etc | less
   ```
   *(Passes the long directory listing into `less` for easier scrolling.)*

2. **Counting files in a directory:**
   ```sh
   ls -1 | wc -l
   ```
   *(Lists files one per line, then passes that list to `wc -l` to count the lines.)*

3. **Finding specific processes:**
   ```sh
   ps aux | grep "python"
   ```
   *(Lists all running processes, then filters that list to show only lines containing "python".)*

4. **Complex chaining:**
   ```sh
   cat access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -10
   ```
   *(Reads a web server log, extracts IP addresses, sorts them, counts unique occurrences, sorts by highest count, and shows the top 10.)*

---
# 7_UNIX_Wildcards_and_Glob_Patterns.md
---

# 7. UNIX Wildcards and Glob Patterns

***

## What are Wildcards (Globbing)?

Wildcards are special characters used in the terminal to match multiple filenames or directories simultaneously based on a pattern. The process of expanding these patterns into actual filenames is called "globbing," and it is performed by the shell *before* the command executes.

Using wildcards makes file management highly efficient, saving you from typing long lists of files manually.

***

## The Primary Wildcards

### The Asterisk (`*`) — Zero or More Characters

The asterisk is the most common wildcard. It matches any sequence of characters, including an empty string (zero characters).

**Examples:**

| Command | Matches | Does Not Match |
|---------|---------|----------------|
| `ls *.txt` | All files ending in `.txt` (e.g., `report.txt`, `data.txt`). | `report.csv`, `script.sh` |
| `rm doc*` | Any file starting with `doc` (e.g., `doc1`, `document.pdf`, `doc`). | `mydoc.txt` |
| `cp *backup* /tmp/` | Any file containing the word `backup` anywhere in its name. | `back_up.zip` |
| `ls *` | All visible files and directories in the current folder. | Hidden files (e.g., `.bashrc`) |

### The Question Mark (`?`) — Exactly One Character

The question mark matches exactly one character. It will not match zero characters or multiple characters.

**Examples:**

| Command | Matches | Does Not Match |
|---------|---------|----------------|
| `ls file?.txt` | `file1.txt`, `fileA.txt`, `file_.txt` | `file10.txt`, `file.txt` |
| `rm ??-report` | `Q3-report`, `01-report` | `1-report`, `2024-report` |
| `mv ??? archives/`| Any file with exactly 3 characters in its name. | `ab`, `abcd` |

### Square Brackets (`[...]`) — Character Classes

Square brackets define a set or range of characters. It matches exactly one character that is included within the brackets.

**Examples:**

| Command | Matches |
|---------|---------|
| `ls file[123].txt` | `file1.txt`, `file2.txt`, `file3.txt` |
| `cat [a-z]*.log` | Any `.log` file starting with a lowercase letter. |
| `rm [A-Z]*` | Any file starting with an uppercase letter. |
| `mv [0-9][0-9]_data.csv /tmp/`| Files starting with exactly two digits (e.g., `14_data.csv`). |

**Negation (`[!...]` or `[^...]`):**
Placing an exclamation mark `!` (or a caret `^` in some shells) immediately inside the opening bracket negates the class, matching any character *except* those listed.

```sh
ls [!0-9]*
```
*(Matches any file that does **not** start with a number.)*

***

## Wildcard Exceptions and Gotchas

### 1. Hidden Files
By default, wildcards **do not** match hidden files (files starting with a dot `.`).

If you run `rm *`, it deletes all visible files but leaves `.bashrc` and `.profile` intact. To match hidden files, you must explicitly include the dot in your pattern:
```sh
ls .*
```

### 2. Directory Separators
Wildcards do not cross directory boundaries (the `/` character).
The pattern `*/*.txt` matches `.txt` files located exactly one directory level down, but it will not match `.txt` files in the current directory or two levels down.

***

## Escaping Wildcards

Sometimes you need to use a literal asterisk `*` or question mark `?` in a filename (though this is bad practice). To stop the shell from interpreting them as wildcards, you must escape or quote them.

**Using a Backslash (`\`):**
```sh
rm file\*.txt
```
*(Deletes a file literally named `file*.txt`)*

**Using Quotes:**
```sh
rm 'file*.txt'
```
*(Single quotes prevent all globbing and variable expansion.)*

***

## Practical Workflow Examples

**1. Organizing a messy downloads folder:**
```sh
mv *.jpg *.png *.gif ~/Pictures/
mv *.pdf *.doc *.docx ~/Documents/
```

**2. Cleaning up numbered logs, keeping only recent ones:**
```sh
rm log_file_2022_??.log
```
*(Deletes all monthly logs from 2022, e.g., `log_file_2022_01.log` to `log_file_2022_12.log`)*

**3. Running a command on specific script versions:**
```sh
chmod +x script_v[2-5].sh
```
*(Makes versions 2, 3, 4, and 5 executable)*

