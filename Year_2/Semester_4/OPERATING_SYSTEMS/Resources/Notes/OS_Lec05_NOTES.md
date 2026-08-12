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
