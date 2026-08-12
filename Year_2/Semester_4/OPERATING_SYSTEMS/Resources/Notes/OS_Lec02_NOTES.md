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
