# Operating Systems — Chapter 3: Processes

## What is a process
- A process = a program in execution.
- It is also an asynchronous activity monitored by the operating system.
- The operating system associates each process with a data structure, the process descriptor or Process Control Block (PCB).
- Analogy: the program is like a musical score, while the process is the actual performance of the "piece".

## Process address space
Each process has its own address space, which includes:
- **Text region**: the executable code.
- **Data region**: variables and dynamically allocated memory.
- **Stack region**: local variables and information of active procedure calls.

## Why process management is critical
- It is a core subject of every operating system.
- The OS maintains for each process information about:
  - its state,
  - the resources it holds,
  - the way in which it can control it.
- The OS must:
  - interleave the execution of many processes,
  - maximize CPU utilization,
  - minimize response time,
  - allocate resources with a policy that avoids deadlocks,
  - support communication and creation of processes.

## Basic process states
### 3 basic states
- **Running**: the process is executing on the CPU.
- **Ready**: it is ready to execute, but waiting for the CPU.
- **Blocked**: it cannot continue until some external event occurs.

### Extended model
- **New**: just created.
- **Exit**: completed and released by the OS.

## State transitions
Important transitions:
- **New → Ready**: the process is admitted into the system when allowed by the system limits.
- **Running → Ready**: it exhausts the allowed execution time limit.
- **Running → Blocked**: it requests a service/I/O that cannot be performed immediately.
- **Blocked → Ready**: the event it was waiting for completes, e.g., I/O.
- **Running → Exit**: process termination.

## Dispatcher and time quantum
- New processes enter the ready list.
- When the CPU becomes available, the **dispatcher** assigns the first suitable process for execution.
- So that the CPU is not monopolized, the OS uses a timer interrupt.
- The predefined execution time interval is called the **time quantum**.
- If the quantum expires without the process surrendering the CPU on its own, the OS moves it from Running to Ready and gives the CPU to another process.
- If it requests I/O before the quantum expires, it transitions to Blocked.

## Suspended processes
When main memory is insufficient or when better resource utilization is required:
- some processes are moved to disk,
- two additional states are created:
  - **Blocked/Suspend**
  - **Ready/Suspend**

This is used because the processor is much faster than the I/O devices and a situation can arise where many processes wait for I/O.

## Schedulers
The OS uses different schedulers:
- **Long-term scheduler (job scheduler)**:
  - selects which processes will enter the ready queue,
  - controls the degree of multiprogramming.
- **Short-term scheduler (CPU scheduler)**:
  - selects which process will be executed next on the CPU.
- **Medium-term scheduler**:
  - used particularly in time-sharing systems,
  - periodically moves processes to/from memory.

## Process queues
Processes are organized into queues such as:
- **Ready queue**: processes ready for the CPU.
- **Blocked queue**: processes waiting for an event or completion of I/O.

The scheduler selects processes from these queues.

## PCB — Process Control Block
### Role
- When a new process is created, the OS assigns it a unique **PID**.
- It then creates the **PCB**.
- The PCB contains all the necessary information for managing and controlling the process.
- It is a basic part of the process image together with the program, data, and stack.

### Important idea
- The process image is not necessarily stored in contiguous memory locations.
- At a given moment, part of it may reside in main memory and another part in secondary storage.

## Process table
- The OS implements a **process table**.
- There is one entry for each process.
- The entries store its state so that it can continue after an interrupt or a switch.

## Fields stored for a process
### 1. Process management
- Registers
- Program Counter
- Program status word
- Stack pointer
- Process state
- Process start time
- CPU time used
- CPU time of child processes
- Time of next wakeup
- Message queue pointer

### 2. Memory management / identity
- Pointer to text segment
- Pointer to data segment
- Exit status
- Signal status
- Process identity
- Parent process
- Process group
- Real and effective user/group identity
- Bitmap for signals

### 3. File management
- Permission mask
- Root path
- Working path
- File descriptors
- Effective user and group identity
- System call parameters
- Various indicators

## Process change and context switch
### Reasons for switching the executing process
- Clock interrupt: exhaustion of the time quantum.
- I/O interrupt.
- Memory fault.
- Trap.
- System call, e.g., opening a file.

### What the OS does on a state change
When a process leaves the Running state:
1. It saves the processor context in the PCB (PC and other registers).
2. It moves the PCB to the appropriate queue.
3. It selects a new process for execution.
4. It updates the PCB of the new process.
5. It updates memory management structures.
6. It restores the saved context of the new process.

### Context switch
- The CPU saves the state of the old process and loads that of the new one.
- This time is **overhead**: no useful work is produced.
- The cost depends on the hardware support.

## OS services for processes
- Multiprogrammed OS provide system calls for process management.
- These services can be activated:
  - directly, through supervisor calls within the code,
  - indirectly, through terminal commands that are translated into system calls.
- Although OS differ in design, they provide a similar basic set of functions for processes.

## Process creation
When the OS creates a new process:
- it creates the necessary data structures,
- allocates memory to it,
- admits it into the system.

### Common causes of creation
- Submission of a new job.
- Login of a new user.
- Service request from an application.
- Creation by an existing process.

## Unix: fork, exec, exit, wait
### fork()
- Creates a new child process as a clone of the parent.
- The child:
  - has a virtual copy of the parent's virtual memory,
  - initially executes the same program,
  - starts with the same register values.

### exec()
- Replaces the memory image of the calling process with a new program.
- Transfers control to the new program.

### exit(status)
- Terminates the process.

### wait(&status)
- The parent process waits for the termination or another state change of a descendant.

## Possible exam questions
1. What is a process and how does it differ from a program?
2. What are the basic process states?
3. What causes the Running → Ready and Running → Blocked transitions?
4. What is the role of the dispatcher?
5. What is the PCB and what data does it contain?
6. What is a context switch and why is it considered overhead?
7. What is the difference between the long-term, short-term, and medium-term scheduler?
8. What is the relationship of fork(), exec(), exit(), wait() in Unix?

## Short summary for revision
- Process = a program in execution with its own address space and PCB.
- Basic states: New, Ready, Running, Blocked, Exit, and in some models Suspend states.
- The OS uses a scheduler, dispatcher, queues, and time quanta to share the CPU.
- The PCB and the process table hold all the necessary information for restarting/continuing a process.
- Process switching requires a context switch, which has a cost.
- In Unix, the creation/execution/termination cycle is closely linked with fork(), exec(), wait(), exit().
