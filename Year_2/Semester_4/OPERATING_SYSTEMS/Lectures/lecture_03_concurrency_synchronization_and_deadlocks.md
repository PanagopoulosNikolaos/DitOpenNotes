# Lecture 03: Concurrency, Synchronization, and Deadlocks

This lecture addresses concurrent process execution, the critical section problem, software and hardware synchronization primitives (Peterson's algorithm, semaphores, mutexes), and deadlock theory (Coffman conditions, Banker's algorithm).

---

## 1. The Critical Section Problem

When multiple concurrent threads or processes share read-write memory, uncontrolled interleaved execution leads to **race conditions**, where the final outcome depends arbitrarily on the exact scheduling order.

### 1.1 Requirements for Valid Solution
Any valid protocol solving the Critical Section (CS) problem must satisfy:
1. **Mutual Exclusion:** If process $P_i$ is executing in its critical section, no other processes can be executing in their critical sections.
2. **Progress:** If no process is executing in its critical section and some processes wish to enter, only those processes not in remainder sections can participate in deciding who enters next, and selection cannot be postponed indefinitely.
3. **Bounded Waiting:** A bound must exist on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted (prevents starvation).

---

## 2. Synchronization Primitives

### 2.1 Peterson's Algorithm (Software Solution for 2 Processes)

```c
// Shared variables
int flag[2] = {0, 0};
int turn = 0;

void process(int i) {
    int j = 1 - i;
    while (1) {
        flag[i] = 1;         // Declare intent to enter
        turn = j;            // Be polite: yield turn to other process
        while (flag[j] && turn == j) {
            // Busy wait
        }
        // --- CRITICAL SECTION ---
        flag[i] = 0;         // Exit section: release intent
        // --- REMAINDER SECTION ---
    }
}
```

### 2.2 Semaphores (Dijkstra)
A semaphore $S$ is an integer variable accessed exclusively via two atomic operations:
- `wait(S)` (or `P(S)`): Decrements value; if negative or zero, blocks calling process.
  ```c
  void wait(Semaphore *S) {
      S->value--;
      if (S->value < 0) {
          // add this process to S->queue and block()
      }
  }
  ```
- `signal(S)` (or `V(S)`): Increments value; unblocks one waiting process from queue.
  ```c
  void signal(Semaphore *S) {
      S->value++;
      if (S->value <= 0) {
          // remove process P from S->queue and wakeup(P)
      }
  }
  ```

---

## 3. Deadlocks

A deadlock occurs when a set of blocked processes each holds a resource and waits to acquire a resource held by another process in the set.

### 3.1 The Four Coffman Necessary Conditions
Deadlock can arise if and only if all four conditions hold simultaneously:
1. **Mutual Exclusion:** At least one resource must be held in a non-shareable mode.
2. **Hold and Wait:** A process must currently hold at least one resource and be waiting to acquire additional resources held by other processes.
3. **No Preemption:** Resources cannot be forcibly confiscated; they can be released only voluntarily by the holding process.
4. **Circular Wait:** A closed chain of processes exists: $P_0$ waits for resource held by $P_1$, $P_1$ waits for $P_2$, $\dots$, $P_{n-1}$ waits for $P_n$, and $P_n$ waits for $P_0$.

---

## 4. Deadlock Handling Strategies

1. **Deadlock Prevention:** Design protocols that structurally violate at least one of the four Coffman conditions (e.g., impose a global total ordering on all resource types to eliminate Circular Wait).
2. **Deadlock Avoidance (Banker's Algorithm):** Dynamically inspect resource requests. Grant requests only if the resulting state is guaranteed to be **Safe** (an execution sequence $\langle P_1, P_2, \dots, P_n \rangle$ exists where each process can satisfy its maximum claim using currently available resources plus resources freed by previously completed processes).
3. **Deadlock Detection and Recovery:** Periodically execute cycle-detection algorithms on the Resource Allocation Graph (RAG); recover via process termination or resource preemption.
4. **Ostrich Algorithm:** Ignore the problem entirely (standard approach in general-purpose operating systems when deadlocks are rare).

