# Exam 7: OS Theory - Processes and Semaphores

This theoretical exam evaluates your understanding of process states and synchronization mechanisms like semaphores.

***

## Questions

**Question 1: Process State Transitions**
Explain the circumstances under which a process transitions to the "Suspended" (or "Suspended in Memory") state. What causes this transition, and when does the process return to a ready or active state?

**Question 2: Semaphore Operations**
Consider a binary semaphore `S` initialized with a value of 1. 
- Describe in detail what happens to the program execution and the value of the semaphore when a process calls the `wait(S)` (or `P(S)`) operation.

**Question 3: Deadlocks**
What are the four necessary conditions for a deadlock to occur in an operating system? Briefly explain each condition.

**Question 4: Context Switching**
Describe the steps an operating system takes when performing a context switch between two processes. Why is context switching considered overhead?

**Question 5: CPU Scheduling**
Compare the First-Come, First-Served (FCFS) scheduling algorithm with the Round Robin (RR) algorithm. In what scenario would RR perform significantly better than FCFS in terms of average response time?

***
*Tip: For semaphores, clearly distinguish between the value of the semaphore and the blocking/waking of processes.*
