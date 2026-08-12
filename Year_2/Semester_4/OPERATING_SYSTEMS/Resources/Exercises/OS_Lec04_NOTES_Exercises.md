# Exercises — Chapter 4: OS Architectures

**Based on:** `OS_Lec04_NOTES.md`  
**Number of exercises:** 30

---

## Part A — Monolithic and Layered

### Exercise 1
Define monolithic system. What are the advantages and disadvantages?

---

### Exercise 2
Describe the 4 steps of a system call in a monolithic architecture.

---

### Exercise 3
Explain the layered architecture. Why can throughput be lower?

---

### Exercise 4
Complete the table of layers (Layer 0–4) and their location (user/kernel space).

---

### Exercise 5
Mark **T** or **F**:

1. In a monolithic OS every procedure can directly call any other.
2. In a layered architecture each layer communicates only with adjacent layers.
3. The Linux kernel is purely a microkernel.
4. The lack of structure in monolithic systems makes them hard to maintain.
5. MINIX uses a microkernel.

---

## Part B — Microkernel and Threads

### Exercise 6
Define microkernel architecture. What runs in kernel space vs user space?

---

### Exercise 7
Describe the client-server communication flow in the microkernel (3 steps).

---

### Exercise 8
State four advantages of the microkernel.

---

### Exercise 9
Define thread. What does a thread include?

---

### Exercise 10
Compare process and thread: address space, creation cost, context switch cost, communication.

---

### Exercise 11
Explain the difference between user-level threads and kernel-level threads.

---

### Exercise 12
What is hyper-threading (Intel) and what is its goal?

---

### Exercise 13
State examples of thread APIs (Pthreads, Java threads).

---

## Part C — Multiprocessing and Special Systems

### Exercise 14
Define a multiprocessing system. State the categories and interconnection topologies.

---

### Exercise 15
Compare SMP (Symmetric Multiprocessing) and asymmetric multiprocessing.

---

### Exercise 16
Define a parallel system. What are its advantages?

---

### Exercise 17
Distinguish hard real-time and soft real-time systems. Give an example for each.

---

### Exercise 18
Define a distributed system. What does it hide from the user?

---

### Exercise 19
State three characteristics of distributed systems.

---

## Part D — Comparative Analysis and Applications

### Exercise 20
Complete the table:

| Architecture | Speed | Maintainability | Security/Reliability |
| :--- | :--- | :--- | :--- |
| Monolithic | | | |
| Layered | | | |
| Microkernel | | | |

---

### Exercise 21
**Identification:** An OS where the file system and scheduler run as servers in user space. Which architecture?

---

### Exercise 22
**System Call Steps:** Sort: trap, return of control, locating the service procedure, determining the service number.

---

### Exercise 23
**Layering:** An I/O request passes through Layer 4 → 3 → 2 → 1 → 0. Explain why latency increases.

---

### Exercise 24
**Thread vs Process:** A web server application with 100 concurrent connections — would you prefer 100 processes or 1 process with 100 threads? Why?

---

### Exercise 25
**Real-Time:** A system controlling the dispensing of medication in a hospital — hard or soft RT? Justify.

---

### Exercise 26
**SMP vs Asymmetric:** In which model do all CPUs share the same process queue?

---

### Exercise 27
**Distributed vs Parallel:** What is the basic difference with respect to whether the user perceives multiple computers?

---

### Exercise 28
Circle the correct answer: Which OS uses a microkernel?

- a) Linux (monolithic modular)  
- b) Windows NT fully  
- c) MINIX  
- d) DOS

---

### Exercise 29
Explain the two solutions for resolving the limitations of the microkernel (servers in kernel mode vs policy in the servers).

---

### Exercise 30
Exam scenario: Given the characteristics — "one process, many threads, shared address space, low switching cost". What architecture/concept is described?
