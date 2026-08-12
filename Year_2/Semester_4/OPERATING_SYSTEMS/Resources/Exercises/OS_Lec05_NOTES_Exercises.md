# Exercises — Mutual Exclusion

**Based on:** `OS_Lec05_NOTES.md`  
**Number of exercises:** 30

---

## Part A — Theory

### Exercise 1
Define mutual exclusion and critical section.

---

### Exercise 2
State the 8 conditions for correct mutual exclusion (from the notes).

---

### Exercise 3
Explain why the length of the critical section must be as short as possible.

---

### Exercise 4
Why does the Dekker algorithm (1st attempt — strict alternation) cause busy waiting?

---

### Exercise 5
Why does the 2nd Dekker attempt (flag array) fail?

---

## Part B — Implementation

### Exercise 6
Explain disabling interrupts as a mutual exclusion technique. Advantages and disadvantages.

---

### Exercise 7
Describe the Test-and-Set (TAS) operation. Why is it atomic?

---

### Exercise 8
Give pseudocode using TAS for mutual exclusion.

---

### Exercise 9
What is Priority Inversion and how does it relate to TAS?

---

### Exercise 10
Explain semaphores: what they are, what the operations P (wait) and V (signal) do.

---

### Exercise 11
Distinguish binary and counting semaphores. When is each used?

---

### Exercise 12
**Exam Tip:** With what value is a binary semaphore initialized for mutual exclusion? With what value for execution synchronization (P2 after P1)?

---

## Part C — Application Exercises

### Exercise 13
Two processes share a `counter` variable. Without mutual exclusion, why can the result be incorrect?

---

### Exercise 14
Write pseudocode for mutual exclusion with a binary semaphore Q=1.

---

### Exercise 15
Write pseudocode so that Process 2 executes B only after Process 1 completes A (semaphore flag=0).

---

### Exercise 16
What happens when a program calls `wait` on a binary semaphore S with value 1?

---

### Exercise 17
What happens when it calls `wait` on S with value 0?

---

### Exercise 18
What happens when it calls `signal` on S with value 0 and an empty waiting queue?

---

### Exercise 19
Mark **T** or **F**:

1. Semaphores eliminate busy waiting through sleep/wakeup.
2. Disabling interrupts guarantees mutual exclusion on SMP.
3. TAS can cause starvation.
4. An incorrect wait/signal order can cause deadlock.
5. Counting semaphores take only the values 0 and 1.

---

### Exercise 20
Circle the correct answer: Which operation is called **before** the critical section?

- a) signal (V)  
- b) wait (P)  
- c) TAS return  
- d) enable interrupts

---

## Part D — Complex Questions

### Exercise 21
Compare software solutions (Dekker) with hardware support (TAS, semaphores).

---

### Exercise 22
Describe a scenario where a counting semaphore with value 3 manages a pool of 3 buffer slots.

---

### Exercise 23
Two processes: P1 does wait(A) wait(B), P2 does wait(B) wait(A). Can deadlock occur with semaphores? Explain.

---

### Exercise 24
Why are Dijkstra's semaphores considered better than TAS for multiprogramming environments?

---

### Exercise 25
Explain the difference between busy waiting and blocking wait.

---

### Exercise 26
How many processes can be in the critical section simultaneously with a binary semaphore? With a counting semaphore of value N?

---

### Exercise 27
Producer-Consumer scenario with one slot: what semaphore initialization (empty, full, mutex)?

---

### Exercise 28
Analyze: "Only one process must succeed in entering if many try" — which mutual exclusion condition?

---

### Exercise 29
Describe how the violation of "no assumption about processor speeds" affects the Dekker algorithm.

---

### Exercise 30
Combined exercise: Use semaphores for mutual exclusion among 3 processes that update a common log file. Describe the structure (without full code).
