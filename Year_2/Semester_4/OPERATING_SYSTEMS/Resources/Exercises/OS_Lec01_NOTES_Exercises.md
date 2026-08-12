# Exercises — Chapter 1: Introduction to Operating Systems

**Based on:** `OS_Lec01_NOTES.md`  
**Number of exercises:** 30

---

## Part A — Definitions and OS Fundamentals

### Exercise 1
Define the Operating System and state its four main objectives.

---

### Exercise 2
Explain the two approaches to defining the OS: "extended machine" and "resource manager". Give one example for each.

---

### Exercise 3
What is the difference between an Operating System and a Kernel?

---

### Exercise 4
State the four layers of a Computer System and briefly describe each one.

---

### Exercise 5
Mark **T** (True) or **F** (False):

1. The kernel is the only program that runs continuously while the OS is active.
2. The hardware is part of the Operating System.
3. DBMS belong to application programs.
4. The OS always runs in user mode for security.
5. Users can be humans, machines, or other computers.

---

## Part B — Historical Evolution

### Exercise 6
What were the main problems of serial processing (1940s) before the advent of OS?

---

### Exercise 7
Explain the role of the Monitor in simple batch systems. What is JCL?

---

### Exercise 8
Complete the table of required hardware features for the Monitor:

| Feature | Purpose |
| :--- | :--- |
| Memory protection | |
| Timer | |
| Privileged instructions | |
| Interrupts | |

---

### Exercise 9
Calculate the CPU Utilization for the following job in a uniprogramming system:

```
Read one record   → 0.0015 sec
Execute 100 inst. → 0.0001 sec
Write one record  → 0.0015 sec
```

---

### Exercise 10
Explain why multiprogramming (1965–1980) was developed. Which OS function allows CPU utilization of up to 100%?

---

### Exercise 11
Compare **multiprogramming** and **time sharing** with respect to: objective, way of job submission, type of job.

---

### Exercise 12
What is the quantum in time-sharing systems and how does it exploit human reaction time?

---

### Exercise 13
State the characteristics of the Fourth Generation of OS (1980–1990): LSI, networks, distributed systems, real-time.

---

### Exercise 14
What is POSIX and when did it appear? What is middleware (2000+)?

---

## Part C — Multiple-Choice Questions

### Exercise 15
Which of the following constitutes the definition of the Kernel?

- a) The set of user applications  
- b) The only program that runs continuously  
- c) The compiler  
- d) The hardware

---

### Exercise 16
In which era did multiprogramming appear?

- a) Early 1940s  
- b) Early 1960s  
- c) 1965–1980  
- d) 1980–1990

---

### Exercise 17
What is the main difference between multiprogramming and time sharing?

- a) Multiprogramming uses multiple CPUs  
- b) Multiprogramming aims to maximize CPU usage, time sharing aims to minimize response time  
- c) Time sharing processes only batch jobs  
- d) There is no difference

---

### Exercise 18
What does it mean that the OS is treated as an "extended machine"?

- a) It has more physical memory  
- b) It hides the complexity of the hardware  
- c) It executes programs faster  
- d) It provides virtualization

---

## Part D — Complex Questions

### Exercise 19
Sort chronologically: Time-Sharing, Serial processing, Linux, Multiprogramming Batch, LSI/Distributed OS.

---

### Exercise 20
State four OS functions required for multiprogramming (memory management, process management, etc.).

---

### Exercise 21
What does "throughput" measure and how does it relate to OS performance metrics?

---

### Exercise 22
Explain the dependency relationship between the OS and the hardware architecture. Why does DOS allow only one process?

---

### Exercise 23
Describe the difference between batch jobs and interactive users in the context of historical evolution.

---

### Exercise 24
Mark **T** or **F** and correct:

1. CPU Utilization in uniprogramming with an I/O-bound job can reach 3%.
2. In batch with Monitor, each job loads its own JCL.
3. Linux appeared in the period 1990–2000.
4. Distributed OS appear as traditional single-processor systems.
5. Interrupts are used only in modern OS.

---

### Exercise 25
State the theory and the laboratory (Unix) covered by the course according to the notes.

---

### Exercise 26
Why did the expensive machines of the 1960s lead to the development of batch systems?

---

### Exercise 27
Explain how hardware features (interrupts, I/O, DMA) form the basis of multiprogrammable systems.

---

### Exercise 28
What is the average response time and why is it minimized in time sharing?

---

### Exercise 29
Complete: "Kernel ___ OS" — explain the relationship.

---

### Exercise 30
Scenario: A batch system processes 100 jobs/hour. A time-sharing system serves 20 users with a quantum of 100ms. Compare which system you choose for: (a) overnight scientific computations, (b) interactive terminal lab.
