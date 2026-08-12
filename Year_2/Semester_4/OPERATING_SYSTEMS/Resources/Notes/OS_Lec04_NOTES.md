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
