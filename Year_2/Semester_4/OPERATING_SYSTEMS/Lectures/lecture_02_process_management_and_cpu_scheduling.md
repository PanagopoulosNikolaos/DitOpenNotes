# Lecture 02: Process Management and CPU Scheduling

This lecture analyzes the process abstraction, Process Control Blocks (PCB), process lifecycle state transitions, the POSIX `fork()`/`exec()` execution model, and single-processor CPU scheduling algorithms.

---

## 1. The Process Abstraction

A process is a program in active execution. Unlike a passive program stored on disk, a process encompasses:
- Program Counter (PC) and processor registers.
- Text section: compiled executable machine instructions.
- Data section: global and static variables.
- Stack: temporary data (function parameters, return addresses, local variables).
- Heap: dynamically allocated memory at runtime (`malloc` / `new`).

### 1.1 Process Lifecycle States

```
                +------------+
                |    NEW     |
                +------------+
                      | Admitted
                      v
Interrupt /     +------------+ Dispatcher /      +------------+
Timeout  <----- |   READY    | --------------->  |  RUNNING   |
                +------------+ Allocated CPU     +------------+
                      ^                                |
                      | I/O or Event Completion        | I/O or Event Wait
                +------------+                         |
                |  WAITING   | <-----------------------+
                +------------+
                      | Exit
                      v
                +------------+
                | TERMINATED |
                +------------+
```

### 1.2 Process Control Block (PCB)
The kernel tracks each process via an internal data structure:
- **Process ID (PID):** Unique numeric process identifier.
- **Process State:** Running, Ready, Waiting, Terminated.
- **CPU Registers & PC:** Saved upon context switch and restored upon resumption.
- **CPU Scheduling Information:** Priority, scheduling queue pointers.
- **Memory Management Info:** Page tables or base/limit registers.
- **I/O Status & Open File Table:** Pointers to open files and devices.

---

## 2. Process Creation in POSIX: fork() and exec()

POSIX decouples process creation from executable binary loading:

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(void) {
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        return 1;
    } else if (pid == 0) {
        // Child process: replace address space with new binary
        char *args[] = {"ls", "-la", NULL};
        execvp("ls", args);
        perror("execvp failed");
        return 1;
    } else {
        // Parent process: await child termination
        int status;
        waitpid(pid, &status, 0);
        printf("Child process %d exited with status %d\n", pid, WEXITSTATUS(status));
    }
    return 0;
}
```

- `fork()` clones the caller, creating an exact duplicate child process with separate memory pages (optimized via Copy-on-Write). Returns `0` in child and child PID in parent.
- `execvp()` overlays the process image with a new executable program.
- `waitpid()` suspends the parent until the child changes state, preventing orphan processes and reclaiming zombie processes.

---

## 3. CPU Scheduling Metrics and Algorithms

The CPU scheduler selects an available process from the Ready queue when the CPU becomes idle.

### 3.1 Evaluation Metrics
- **Turnaround Time ($T_{\text{turn}}$):** $T_{\text{completion}} - T_{\text{arrival}}$.
- **Waiting Time ($T_{\text{wait}}$):** $T_{\text{turnaround}} - T_{\text{burst}}$.
- **Response Time ($T_{\text{resp}}$):** Time from arrival to first execution on CPU.
- **Throughput:** Number of processes completed per unit time.

### 3.2 Scheduling Algorithms

| Algorithm | Preemption | Strategy / Priority Criteria | Strengths & Weaknesses |
|---|---|---|---|
| **First-Come, First-Served (FCFS)** | Non-preemptive | Order of arrival | Simple, but suffers from **Convoy Effect** (short jobs wait behind long I/O-bound jobs). |
| **Shortest Job First (SJF)** | Non-preemptive | Shortest expected CPU burst | **Provably optimal** minimum average waiting time; requires predicting future burst lengths. |
| **Shortest Remaining Time First (SRTF)** | Preemptive | Preempts if newly arrived job has shorter burst than current remaining | Optimal waiting time among preemptive schedulers; causes starvation of long jobs. |
| **Round Robin (RR)** | Preemptive | FIFO queue with fixed time quantum $q$ | Fair, low response time for interactive systems. If $q$ too large $\to$ FCFS; if $q$ too small $\to$ context switch overhead dominates. |
| **Priority Scheduling** | Either | Highest integer priority runs first | Reflects business importance; vulnerable to indefinite blocking (**Starvation**), solved via **Aging**. |

