# Theory Examination - June 2023

## QUESTION 1 (1 unit)
(a) Explain in what state(s) a process that is in a suspended waiting state in memory can transition to, and when.
(b) What will happen when a program calls the `wait` method on a binary semaphore S with value 1? (i.e., what will happen to the program and to the semaphore)

## QUESTION 2 (1 unit)
A computing system uses 16-bit logical addresses and paging to support virtual memory. Explain:
(i) What will be the number of bits for specifying the offset in the page if the size of each page is 1024 bytes.
(ii) How many entries the page table must have to support the maximum number of pages.

## QUESTION 3 (3 units: a=1, b=2)
In a computing system, processes P1, P2, P3, P4 and P5 arrive for execution at time 0 in that order.
The CPU burst times for the five processes are:
P1=1, P2=3, P3=4, P4=3 and P5=1

(a1) Complete the following execution diagram of the five processes as scheduled by the "Shortest Job First" (SJF) algorithm. Each column in the table corresponds to one millisecond.

| Time | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Executing Process | | | | | | | | | | | | |

(a2) Calculate the response times of the processes and the average response time.

(b1) Complete the following execution diagram of the five processes as scheduled by the "Round Robin" algorithm with a time quantum of two (2) units, showing which process is executing at each moment and which processes are in the waiting queue. Each column in the table corresponds to one millisecond.

| Time | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Executing Process | | | | | | | | | | | | |
| QUEUE (Note the processes in the order they are waiting. The first in the queue enters at the top) | | | | | | | | | | | | |

(b2) Calculate the waiting times of the processes and the average waiting time.