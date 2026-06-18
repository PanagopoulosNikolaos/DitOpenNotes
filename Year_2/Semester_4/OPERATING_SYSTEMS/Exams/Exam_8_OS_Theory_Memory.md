# Exam 8: OS Theory - Memory Management

***

## Questions

**Question 1: Paging and Logical Addresses**
A computer system uses 16-bit logical addresses and pagination (paging) to support virtual memory. The size of each page is 1024 bytes.
- (i) Explain how many bits will be used to specify the offset within the page.
- (ii) How many entries must the page table have to support the maximum number of pages for this address space?

**Question 2: Fragmentation**
Differentiate between Internal Fragmentation and External Fragmentation. Which type of memory allocation scheme (Paging or Segmentation) suffers from which type of fragmentation?

**Question 3: Page Replacement Algorithms**
Explain the concept of the Least Recently Used (LRU) page replacement algorithm. How does it decide which page to evict from memory when a page fault occurs?

**Question 4: Thrashing**
What is thrashing in the context of virtual memory? What are its primary causes, and how can an operating system mitigate it?

**Question 5: Translation Lookaside Buffer (TLB)**
What is the purpose of a Translation Lookaside Buffer (TLB) in a paged memory system? How does it improve the performance of logical-to-physical address translation?

***
*Tip: Remember that 1 KB = 1024 bytes, which is 2^10 bytes. This will help you calculate offset bits quickly.*
