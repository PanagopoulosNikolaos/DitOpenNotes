# Operating Systems — Chapter 6: Deadlock

Deadlock is one of the fundamental concepts in operating systems and concerns the indefinite waiting of a set of processes due to competition for resources. The chapter covers definitions, resource categories, resource allocation graphs, the 4 necessary conditions for deadlock, the basic handling strategies, and the classic dining philosophers problem.

---

## 1. Basic concepts

### Definition of deadlock

Deadlock is the permanent or indefinite waiting of a set of processes that either compete for system resources or communicate with each other.

### Why it occurs

In a multiprogramming system, the total demands of active processes usually exceed the available resources. Deadlock occurs when two or more processes have conflicting needs for resources and none can continue.

### Design goal

The basic goal is to design systems where deadlock cannot happen or where it can be detected and recovered from in a controlled manner.

> **[Key Insight]**
> The problem is not simply the lack of resources, but the specific sequence of resource acquisition and waiting by many processes.

---

## 2. Types of resources

### Preemptable resources

Preemptable resources are those that can be taken away from a process without causing failure.

Examples:

- Memory space in certain management models.
- CPU registers in environments where state is saved and restored.

### Nonpreemptable resources

Nonpreemptable resources are those that cannot be taken away without undesirable consequences or failure of the process.

Examples:

- Printers.
- Tape drives.
- CD recorders.
- Input/output devices with critical state.

Nonpreemptable resources are the main cause of deadlock occurrence.

### Resource usage cycle

The use of a resource by a process usually follows the sequence:

1. Request.
2. Use.
3. Release.

If the request is not satisfied, the process is either suspended or fails with an error message.

### Reusable resources

Reusable resources can be safely used by one process at a time and then returned for use by other processes.

Examples:

- Processors.
- I/O channels.
- Main memory.
- Secondary storage.
- Files.
- Databases.
- Semaphores.

Deadlock here arises when a process holds a resource and requests another.

### Consumable resources

Consumable resources are produced and destroyed during their use. Once consumed, they cease to exist as available resources.

Examples:

- Interrupts.
- Signals.
- Messages.
- Information in I/O buffers.

In this category, deadlock can occur, for example, when a message sent by one process is not received by another.

---

## 3. Examples of deadlock

### Classic pattern

If process $P$ first acquires resource $A$ and then requests $B$, while process $Q$ first acquires $B$ and then requests $A$, a deadlock can arise.

This happens because:

- $P$ waits for a resource held by $Q$.
- $Q$ waits for a resource held by $P$.
- Neither can proceed to release the resource it holds.

### Example with memory

Assume available main memory of $200\text{KB}$ and two processes:

- $P_1$: requests $80\text{KB}$ and then $60\text{KB}$.
- $P_2$: requests $70\text{KB}$ and then $80\text{KB}$.

If the first requests are satisfied first, $150\text{KB}$ are allocated and $50\text{KB}$ remain. Then none of the second requests can be satisfied, so the processes block.

This case is solved more easily because memory is considered a preemptable resource.

---

## 4. Resource allocation graphs

Resource allocation graphs are a tool for modeling the state of resources and processes.

### Notation

- Process node: $P_i$.
- Resource type node: $R_j$.
- Request edge: $P_i \rightarrow R_j$.
- Assignment edge: $R_j \rightarrow P_i$.

### Interpretation

- If there is an edge from a process to a resource, the process requests an instance of the resource.
- If there is an edge from a resource to a process, an instance of the resource has been assigned to the process.

### Relationship between cycles and deadlock

- If the graph **does not** contain a cycle, then there is **no** deadlock.
- If the graph contains a cycle and there is only one instance per resource type, then there is a deadlock.
- If the graph contains a cycle and there are multiple instances per resource type, then there is only a possibility of deadlock, not a certainty.

> **[Key Insight]**
> A cycle in a resource allocation graph does not always mean deadlock. The critical detail is whether each resource type has one or more instances.

---

## 5. The 4 necessary conditions for deadlock

Deadlock can occur only if the following four conditions hold **simultaneously**.

### 5.1 Mutual exclusion

Each resource is either available or belongs exclusively to only one process.

### 5.2 Hold and wait

A process can already hold some resources and simultaneously wait for additional resources.

### 5.3 No preemption

Resources cannot be forcibly taken away from the process holding them.

### 5.4 Circular wait

There is a closed chain of processes where each process waits for a resource held by the next.

### Basic conclusion

To prevent deadlock, it suffices to violate at least **one** of the four necessary conditions.

---

## 6. Handling approaches

There are four basic approaches:

1. Prevention.
2. Avoidance.
3. Detection & recovery.
4. Manual intervention.

### 6.1 Prevention

In prevention we design the system so that at least one of the four necessary conditions is violated.

#### Violating mutual exclusion

The goal is to reduce the cases of exclusive resource use.

Example:

- For a printer, instead of many processes using it directly, a `printer daemon` and a print queue are used.

Limitation: not all resources can be practically converted into shared ones.

#### Violating hold and wait

Two basic techniques:

- The process requests **all** its resources before it starts.
- If it needs new resources later, it first releases those it already holds and re-requests the full set.

Disadvantages:

- Usually not all requirements are known in advance.
- Prolonged deprivation can arise.
- Resources remain allocated without being used continuously.

#### Violating no preemption

If possible, a resource is temporarily taken from a process and given elsewhere.

It applies only to resources whose state can be saved and restored later.

Examples where it is **not** practical:

- Writing to a CD.
- Many physical I/O devices.

#### Violating circular wait

A linear ordering of resources is defined and processes are required to request resources only in increasing order.

Example:

- If $R_1 < R_2 < R_3$, a process may request $R_1$ and then $R_3$, but not $R_3$ and then $R_1$.

### 6.2 Avoidance

In avoidance the system allows the first three conditions, but decides dynamically whether a new allocation could later lead to a deadlock.

Additional advance information is required, mainly the maximum number of resources each process may request.

Main idea:

- Allocate resources only if the system remains in a **safe state**.

### 6.3 Detection and recovery

In this approach the system allocates resources whenever it can and periodically checks whether a deadlock has formed.

If a deadlock is detected, recovery is applied through:

- Termination of processes.
- Preemption of resources.
- Rolling back to previous checkpoints.

### 6.4 Manual intervention

In some practical systems, the administrator simply restarts the system when the situation seems out of control or excessively slow.

---

## 7. Banker's algorithm

The banker's algorithm is the classic deadlock avoidance technique for systems with multiple resource instances.

### Basic concepts

- **System state:** the current allocation of resources to processes.
- **Safe state:** there is at least one completion sequence of processes without deadlock.
- **Unsafe state:** there is no guaranteed safe sequence. This does not mean certain deadlock, but a real possibility.

### Assumptions

The algorithm assumes that:

- There are multiple resource instances.
- Each process declares its maximum demand in advance.
- A process that receives all its resources will return them in finite time.
- The number of resources is fixed.
- The significant processes are independent.
- No process terminates while holding resources.

### Data structures

Let $n$ processes and $m$ resource types.

- `Available[j]`: available instances of resource $R_j$.
- `Max[i,j]`: maximum demand of process $P_i$ for resource $R_j$.
- `Allocation[i,j]`: instances of resource $R_j$ already assigned to $P_i$.
- `Need[i,j]`: additional instances of $R_j$ that $P_i$ may need.

It is defined:

$$
Need[i,j] = Max[i,j] - Allocation[i,j]
$$

### Criterion of a safe sequence

A sequence $\langle P_1, P_2, \dots, P_n \rangle$ is safe if for every process in the sequence, its remaining needs can be satisfied from the currently available resources together with the resources that will be returned by the preceding processes.

### Steps of the safety algorithm

1. Find a process $P_i$ with $Need[i,j] \leq Available[j]$ for every $j$.
2. Assume that the process completes.
3. Return its resources:
   $$
   Available[j] = Available[j] + Allocation[i,j]
   $$
4. Mark it as completed.
5. Repeat until either all processes complete or no other suitable process can be found.

If all complete, the state is safe.

---

## 8. Deadlock detection

Detection is algorithmically similar to the safety check, but the logic is different: here the system **does not** reject allocations in advance, but checks whether deadlock has already occurred.

### Data structures

Used:

- `Available`
- `Allocation`
- `Need`

### Steps

1. Find a row $i$ where $Need[i,j] \leq Available[j]$ for all $j$.
2. If no such row exists, the unmarked processes are in deadlock.
3. Otherwise, consider that the process completes and returns its resources.
4. Repeat.

### Cost and practice

Detection avoids the continuous restriction of resource access, but requires periodic checks and a recovery strategy.

In practice, many operating systems do not apply strict global detection, but use combinations of techniques such as:

- Quotas.
- Design constraints.
- Conventions for the use of semaphores and resources.
- Process failure when it cannot acquire a critical resource.

### Recovery strategies

When a deadlock is detected, the following can be applied:

- Termination of all processes in deadlock.
- Successive termination until the cycle is broken.
- Checkpoint/rollback.
- Successive resource preemption.

### Criteria for selecting a process for termination

Common criteria:

- Smaller CPU time already consumed.
- Smaller number of output lines produced.
- Larger estimated remaining time.
- Smaller number of allocated resources.
- Lower priority.

---

## 9. Dining philosophers problem

### Description

Five philosophers sit around a circular table. Each philosopher alternates between thinking and eating. To eat, he needs two forks: his left and his right one.

The problem models:

- Each philosopher as a process.
- Each fork as a shared resource.

### What it shows

The problem is used to highlight the difficulty of resource allocation without:

- Deadlock.
- Prolonged starvation.
- Pointless reduction of parallelism.

### Naive solution that fails

If each philosopher executes:

```c
wait(fork[i]);
wait(fork[(i+1) mod 5]);
eat();
signal(fork[(i+1) mod 5]);
signal(fork[i]);
```

all of them can pick up one fork and wait forever for the second one.

### Avoidance techniques

The following solutions emerge from the material:

- Adding one more fork.
- At most 4 philosophers at the table simultaneously.
- Different fork acquisition order for even and odd philosophers.
- Acquiring forks only when both are available.
- Non-symmetric protocol design.

### Solution with the `room` semaphore

```c
semaphore fork[5] = {1};
semaphore room = {4};

while (true) {
    think();
    wait(room);
    wait(fork[i]);
    wait(fork[(i+1) mod 5]);
    eat();
    signal(fork[(i+1) mod 5]);
    signal(fork[i]);
    signal(room);
}
```

The idea is that at most 4 philosophers are allowed to attempt eating simultaneously, so the possibility of a full circular wait is broken.

---

## 10. Connection of concepts

| Concept | Role |
| :--- | :--- |
| Mutual exclusion | A resource is not shared simultaneously |
| Hold and wait | A process holds resources while requesting others |
| No preemption | Resources are not forcibly taken away |
| Circular wait | Closed cycle of process dependency |
| Prevention | Breaks one of the 4 conditions |
| Avoidance | Allows allocations only if the state remains safe |
| Detection | Checks whether the deadlock already exists |
| Recovery | Termination, rollback, or preemption for release |
| Dining philosophers | Classic model of deadlock and starvation |

---

## Solved Exercises

### Exercise 1: Checking deadlock conditions

**Problem:** A process holds a printer and waits for access to a file held by a second process, while the second waits for the printer. Which deadlock conditions hold?

**Solution:**

1. The printer and the file are considered exclusive resources, so mutual exclusion holds.
2. Each process holds a resource and waits for another, so hold and wait holds.
3. The resources are not forcibly taken away, so no preemption holds.
4. The first waits for a resource of the second and the second for a resource of the first, so there is circular wait.
5. Since all 4 conditions hold, the system is in a deadlock.

### Exercise 2: Allocation graph from a description

**Problem:** Given the following: process $P_1$ requests resource $R_1$, process $P_2$ requests resource $R_3$, resource $R_1$ is assigned to $P_2$, $R_2$ is assigned to $P_1$, and $R_3$ is assigned to $P_1$. Describe the graph and check whether there is a deadlock.

**Solution:**

1. The request edges are $P_1 \rightarrow R_1$ and $P_2 \rightarrow R_3$.
2. The assignment edges are $R_1 \rightarrow P_2$, $R_2 \rightarrow P_1$, $R_3 \rightarrow P_1$.
3. $P_1$ waits for $R_1$, which belongs to $P_2$.
4. $P_2$ waits for $R_3$, which belongs to $P_1$.
5. A cycle is formed: $P_1 \rightarrow R_1 \rightarrow P_2 \rightarrow R_3 \rightarrow P_1$.
6. If there is one instance per resource, then there is a deadlock.

### Exercise 3: Tape drives

**Problem:** The system has 6 identical tape drives and $n$ processes. Each process may request up to 2 tape drives. For which value of $n$ is the system deadlock-free?

**Solution:**

1. For a guarantee of deadlock absence, there must always be the possibility of at least one process getting the second tape drive it may need.
2. In the worst case, each process holds 1 tape drive and waits for another 1.
3. If there are $n$ processes, then in the worst case $n$ drives are allocated.
4. For some process to complete, at least 1 drive must be free.
5. Therefore $n \leq 5$ is required.
6. For $n = 6$, all processes can hold 1 drive each and wait for another 1, so circular wait is possible.

### Exercise 4: Memory example

**Problem:** $P_1$ requests $80\text{KB}$ and then $60\text{KB}$, while $P_2$ requests $70\text{KB}$ and then $80\text{KB}$. The total available memory is $200\text{KB}$. Examine whether a deadlock can be created.

**Solution:**

1. We satisfy the first request of $P_1$: $120\text{KB}$ remain.
2. We satisfy the first request of $P_2$: $50\text{KB}$ remain.
3. $P_1$ requests an additional $60\text{KB}$, but there are not enough available.
4. $P_2$ requests an additional $80\text{KB}$, but again there are not enough available.
5. Both block on the second request.
6. The problem is solved with memory preemption, because memory can be recalled/reallocated more easily than other resources.

### Exercise 5: Computing the Need matrix

**Problem:** If for a process $Max = (6,1,2)$ and $Allocation = (2,1,1)$, find $Need$.

**Solution:**

1. We use the formula:
   $$
   Need = Max - Allocation
   $$
2. We compute per component:
   $$
   Need = (6-2, 1-1, 2-1)
   $$
3. Hence:
   $$
   Need = (4,0,1)
   $$
4. The process still needs 4 units of the first resource, 0 of the second, and 1 of the third to complete.

### Exercise 6: Checking a safe sequence

**Problem:** Let $Available = (0,1,1)$ and from the chapter example a safe sequence is $P_2 \rightarrow P_1 \rightarrow P_3 \rightarrow P_4$. What does this mean?

**Solution:**

1. The existence of this sequence means that the system is in a safe state.
2. First, $P_2$ can complete with the available resources.
3. After its completion, it returns its resources and increases `Available`.
4. This makes the completion of $P_1$, then $P_3$, and finally $P_4$ feasible.
5. Therefore, although the initially available resources are few, there is an execution order that avoids deadlock.

### Exercise 7: Prevention through resource ordering

**Problem:** Suppose there are resources $R_1 < R_2 < R_3$. Can a process request $R_2$ first and then $R_1$?

**Solution:**

1. If a linear resource numbering policy is applied, requests must follow increasing order.
2. Requesting $R_2$ first and then $R_1$ violates this policy.
3. The violation could allow the creation of a waiting cycle with other processes.
4. Therefore the request is not allowed.
5. The goal is to preclude the circular wait condition.

### Exercise 8: Dining philosophers with room = 4

**Problem:** Why does the use of the `room = 4` semaphore prevent deadlock in the philosophers problem?

**Solution:**

1. Without restriction, all 5 philosophers can simultaneously pick up one fork.
2. Then each waits for the second and a full waiting cycle is created.
3. With `room = 4`, at most 4 philosophers attempt to acquire forks simultaneously.
4. So at least one always remains outside the acquisition process, which breaks the possibility of forming a 5-member cycle.
5. Thus deadlock is avoided.

---

## Exam Tip: Quick recognition method

In theory questions, the fastest check is the following:

1. Ask whether there is exclusive resource use.
2. Check whether some process holds resources while requesting others.
3. Check whether resources are forcibly taken away or not.
4. Look for a waiting cycle.

If the answer is **yes** to all 4, then you have a deadlock or the exact preconditions for it to occur.

> **[Key Insight]**
> In graph exercises, first check for a cycle and immediately after for the number of instances per resource type. These two steps solve almost the entire question.
