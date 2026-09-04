# Assignment 02: Process Synchronization and Inter-Process Communication in C

This coursework evaluates low-level systems programming in C on Linux: managing POSIX processes, inter-process communication using anonymous pipes and shared memory, and resolving the classic Producer-Consumer synchronization problem.

---

## 1. Objective and Problem Description

Implement the **Bounded-Buffer Producer-Consumer** coordination problem in C using POSIX Threads (`pthreads`), counting semaphores (`sem_t`), and mutex locks (`pthread_mutex_t`).

### Architectural Specifications
- A circular shared buffer of capacity $N = 10$ integer items.
- $P$ concurrent Producer threads that generate random integers and insert them into the circular buffer.
- $C$ concurrent Consumer threads that remove integers from the circular buffer and display them.
- Synchronization requirements:
  - Producers must block when the circular buffer is full.
  - Consumers must block when the circular buffer is empty.
  - Buffer insertions and removals must be protected by mutual exclusion so that multiple threads never corrupt internal buffer state or indices.

---

## 2. Technical Requirements

### 2.1 Synchronization Invariants
Maintain three synchronization primitives:
1. `pthread_mutex_t mutex`: Protects critical sections during index advancement and buffer manipulation.
2. `sem_t empty_slots`: Initialized to buffer capacity $N$. Decremented by producers; incremented by consumers.
3. `sem_t full_slots`: Initialized to `0`. Incremented by producers; decremented by consumers.

### 2.2 Graceful Termination
The program must run for a user-specified duration in seconds (`./bounded_buffer <duration> <num_producers> <num_consumers>`), after which the main thread signals all worker threads to terminate cleanly, destroys all mutexes and semaphores, and exits with status 0 without memory or resource leaks.

---

## 3. Evaluation Rubric

| Criteria | Points |
|---|---|
| Correct semaphore and mutex initialization and destruction | 25 |
| Deadlock-free ordering of `sem_wait` and `pthread_mutex_lock` operations | 35 |
| Correct circular array index advancement (`(in + 1) % N`, `(out + 1) % N`) | 20 |
| Clean shutdown handling and memory safety (Valgrind verified) | 20 |

