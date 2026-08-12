# Exercises — Chapter 3: Processes

**Based on:** `OS_Lec03_NOTES.md`  
**Number of exercises:** 32

---

## Part A — Basic Concepts

### Exercise 1
What is a process and how does it differ from a program? Use the sheet music/performance analogy.

---

### Exercise 2
Describe the process address space: text region, data region, stack region.

---

### Exercise 3
Why is process management critical? State five goals of the OS.

---

### Exercise 4
Draw (or describe) the basic process states and their transitions: New, Ready, Running, Blocked, Exit.

---

### Exercise 5
What causes the Running → Ready and Running → Blocked transitions?

---

### Exercise 6
Explain the Ready/Suspend and Blocked/Suspend states. When are they used?

---

### Exercise 7
Which process in the Waiting/Blocked state in memory can transition to Ready or to Suspended Waiting? When?

---

## Part B — Schedulers and PCB

### Exercise 8
Compare long-term, short-term, and medium-term schedulers with respect to role and usage.

---

### Exercise 9
What is the dispatcher and what is its relationship to the time quantum?

---

### Exercise 10
Describe the Ready queue and the Blocked queue.

---

### Exercise 11
What is the PCB (Process Control Block) and what fields does it contain (grouped into: process management, memory, files)?

---

### Exercise 12
Why is the process image not necessarily in contiguous memory locations?

---

### Exercise 13
What is the process table and how is it linked to the PID?

---

## Part C — Context Switch and Unix

### Exercise 14
State five reasons for switching the executing process.

---

### Exercise 15
Describe the 6 steps the OS performs when a process leaves Running.

---

### Exercise 16
What is a context switch and why is it considered overhead?

---

### Exercise 17
Explain the Unix functions: `fork()`, `exec()`, `exit()`, `wait()`. How are they linked in the process lifecycle?

---

### Exercise 18
After `fork()`, what do the parent and child processes share? What differs?

---

### Exercise 19
Why does `exec()` not create a new process but replace the memory image?

---

## Part D — Application Exercises

### Exercise 20
Process P is running. The time quantum expires before it requests I/O. Which state does it transition to and to which queue?

---

### Exercise 21
Process P is running and calls `read()` for a file on disk. Describe the state transition.

---

### Exercise 22
Main memory is full. A process in Ready must be moved to disk. Which suspend state does it transition to?

---

### Exercise 23
Mark **T** or **F**:

1. The PCB stores the Program Counter.
2. The short-term scheduler controls the degree of multiprogramming.
3. A context switch produces useful work for the user.
4. `wait()` allows the parent to wait for the termination of a child.
5. `fork()` returns 0 to the child process.

---

### Exercise 24
Circle the correct answer: Which scheduler selects which process runs **immediately** on the CPU?

- a) Long-term  
- b) Medium-term  
- c) Short-term  
- d) I/O scheduler

---

### Exercise 25
Complete the table of process creation causes:

| Cause | Example |
| :--- | :--- |
| Submission of a new job | |
| Login of a new user | |
| Request for a service | |
| Creation by an existing process | |

---

### Exercise 26
Describe a scenario: a user runs `./myprogram` in the shell. Which system calls/functions are involved?

---

### Exercise 27
A process in Blocked completes its I/O. Which state does it transition to? Which scheduler selects it for the CPU?

---

### Exercise 28
Explain the difference between "saving the processor context in the PCB" vs "restoring the context from the PCB".

---

### Exercise 29
Why is the medium-term scheduler used mainly in time-sharing systems?

---

### Exercise 30
Answer the 8 "possible exam questions" mentioned at the end of the notes (one sentence each).

---

### Exercise 31
Scenario: 3 processes are in the Ready queue, the CPU is free. Describe the role of the short-term scheduler and the dispatcher.

---

### Exercise 32
Compare context switch overhead with system call overhead. Which is usually larger and why?
