# Exercises — Chapter 2: Purposes and Evolution of OS

**Based on:** `OS_Lec02_NOTES.md`  
**Number of exercises:** 35

---

## Part A — OS Purposes

### Exercise 1
State the four central purposes of an OS and briefly describe each one.

---

### Exercise 2
Explain the dual-mode operation (user mode / monitor mode). What is the mode bit?

---

### Exercise 3
What happens on an interrupt or fault with respect to CPU operation?

---

### Exercise 4
State five privileged instructions mentioned in the notes.

---

### Exercise 5
Describe the flow of a system call for executing I/O from a user program (4 steps).

---

### Exercise 6
Explain the operation of the base and limit registers for memory protection.

---

### Exercise 7
Suppose base = 1000, limit = 500. Which logical addresses are valid? What happens for address 1600?

---

### Exercise 8
How does the timer work to protect the CPU? Why is loading it a privileged instruction?

---

### Exercise 9
State the services provided by the OS to user programs (at least 6).

---

### Exercise 10
Explain the five main responsibilities of the OS in memory management.

---

## Part B — Processes, Memory, Scheduling

### Exercise 11
Define process and state the fields of a process table.

---

### Exercise 12
Describe the memory organization of a process (text, data, stack).

---

### Exercise 13
State five reasons for the creation of errors in processes.

---

### Exercise 14
Explain paging: logical address of 16 bits, page size of 1024 bytes. Calculate: (a) offset bits, (b) size of the page table.

---

### Exercise 15
Logical address 0x3A4F, page size 4KB (4096 bytes). Calculate the page number and offset.

---

### Exercise 16
What is virtual memory and what problems does it solve?

---

### Exercise 17
State four scheduling criteria.

---

### Exercise 18
Explain multiprogramming as a technique for increasing CPU utilization. What are the trade-offs in the degree of multiprogramming?

---

## Part C — Security and Structure

### Exercise 19
State three aspects of protection and information security covered by the OS.

---

### Exercise 20
What problems arise from increasing the size of an OS? Which design trend does modular design address?

---

### Exercise 21
Describe the OS design hierarchy (hardware → kernel → system calls → utilities → applications).

---

### Exercise 22
State three hardware, software, and OS architecture developments in modern systems.

---

## Part D — Application Exercises

### Exercise 23
**Dual-Mode:** A user program runs normally. A page fault occurs. Describe the mode changes and who handles the fault.

---

### Exercise 24
**Memory Protection:** base=2000, limit=300. Check whether access is allowed to addresses 2100, 2299, 2300, 1999.

---

### Exercise 25
**System Call I/O:** Design the flow from `read()` in a user program to the return of data.

---

### Exercise 26
**Paging:** Page 3, offset 256, page size 512 bytes. Calculate the logical address.

---

### Exercise 27
**Deadlock:** Process P holds a printer and requests a plotter. Process Q holds a plotter and requests a printer. Is this a deadlock? Why?

---

### Exercise 28
**OS Hierarchy:** Classify into layers: `ls`, kernel scheduler, `malloc` wrapper, device driver, shell.

---

## Part E — True/False and Multiple Choice

### Exercise 29
Mark **T** or **F**:

1. I/O instructions are executed only in monitor mode.
2. In monitor mode the OS has unlimited access to memory.
3. A microkernel is always faster than a monolithic kernel.
4. The timer is decremented by 1 with each clock tick.
5. Paging allows non-contiguous physical memory.

---

### Exercise 30
Circle the correct answer: Which instruction is privileged?

- a) ADD  
- b) LOAD base register  
- c) MOV  
- d) PUSH

---

### Exercise 31
Which register defines the size of the acceptable memory region?

- a) Program Counter  
- b) Stack Pointer  
- c) Limit register  
- d) Mode register

---

### Exercise 32
Explain the difference between system programs and application programs in the context of OS-user communication.

---

### Exercise 33
What is microprogramming and how does it relate to abstraction levels?

---

### Exercise 34
Scenario: Two processes share a printer. Which OS purpose (I–IV) is mainly involved and how?

---

### Exercise 35
Complete the table:

| Concept | Brief definition |
| :--- | :--- |
| Trap | |
| Interrupt vector | |
| Page table | |
| Degree of multiprogramming | |
| Throughput | |
