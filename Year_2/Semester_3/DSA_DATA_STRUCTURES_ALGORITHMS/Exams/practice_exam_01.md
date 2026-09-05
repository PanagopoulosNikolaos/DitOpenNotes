# Practice Exam 01: Data Structures and Algorithms

**Course:** Data Structures and Algorithms (Course Code 305)  
**Format:** Comprehensive Practice Examination with Full Worked Solutions  
**Total Points:** 100 points  
**Time Allowed:** 120 minutes  

---

## Part I: Examination Questions

### Section A: Asymptotic Analysis & Recurrences (25 Points)

1. *(10 Points)* Using the formal definition of Big-$O$ and Big-$\Omega$ notations:
   - Prove that $f(n) = 5n^3 - 2n^2 + 8n = \Theta(n^3)$ by finding explicit positive constants $c_1, c_2, n_0$.
   - Using the limit quotient test, determine the asymptotic relationship between $g(n) = n^2 \log_2 n$ and $h(n) = n^{2.5}$.

2. *(15 Points)* Apply the Master Theorem or alternative recurrence methods to determine the tight bound $\Theta$ for each of the following:
   - $T_1(n) = 9 T_1(n/3) + n^2$
   - $T_2(n) = 4 T_2(n/2) + n^2 \log_2 n$
   - $T_3(n) = T_3(n-1) + \frac{1}{n}$

---

### Section B: Trees and Self-Balancing AVL Structures (25 Points)

1. *(10 Points)* Consider a Binary Search Tree (BST).
   - State the BST Invariant. Why does an In-Order traversal of any valid BST output keys in monotonically non-decreasing order?
   - Describe the three cases encountered when deleting a node from a BST. Explain how the In-Order Successor preserves the BST invariant when deleting a node with two children.

2. *(15 Points)* Starting with an initially empty AVL tree, insert the following keys sequentially:
   $$[30, 20, 10, 25, 40, 50, 22]$$
   - Draw the tree and indicate the Balance Factor $BF = h_L - h_R$ for all nodes after each insertion.
   - For every detected imbalance ($|BF| \ge 2$), explicitly state the rotation type (LL, RR, LR, RL) and draw the resulting rebalanced tree.

---

### Section C: Binary Heaps, Priority Queues, and Hashing (25 Points)

1. *(12 Points)* Binary Max-Heaps:
   - Given array $A = [4, 10, 3, 5, 1, 14, 8, 9, 2]$, trace Robert Floyd's bottom-up `buildMaxHeap` algorithm. Show the array after each `siftDown` pass.
   - Explain why Floyd's bottom-up heap construction runs in $O(n)$ time while $n$ sequential insertions require $O(n \log n)$ time.

2. *(13 Points)* Hash Table Collision Resolution:
   - Given a hash table of size $m = 11$ with primary hash function $h_1(k) = k \pmod{11}$ and secondary hash function $h_2(k) = 7 - (k \pmod 7)$.
   - Insert keys $[22, 33, 44, 15, 26, 37]$ into:
     - Table 1: Using Linear Probing: $h(k, i) = (h_1(k) + i) \pmod{11}$.
     - Table 2: Using Double Hashing: $h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod{11}$.
   - Explain what **Primary Clustering** is and why Double Hashing eliminates it.

---

### Section D: Graph Traversals and Shortest Paths (25 Points)

1. *(15 Points)* Consider a directed weighted graph $G = (V, E)$ with vertices $V = \{A, B, C, D, E\}$ and directed edges:
   - $(A, B, 4)$, $(A, C, 2)$
   - $(B, C, 1)$, $(B, D, 5)$
   - $(C, B, 1)$, $(C, D, 8)$, $(C, E, 10)$
   - $(D, E, 2)$
   - $(E, D, 3)$
   
   Execute **Dijkstra's Algorithm** with source vertex $s = A$.
   - Maintain a step-by-step trace table showing visited vertices, candidate priority queue contents, and tentative shortest distances $[d(A), d(B), d(C), d(D), d(E)]$ at each iteration.
   - Draw the resulting Shortest Path Tree.

2. *(10 Points)* Topological Sorting:
   - Explain Kahn's algorithm for computing a topological ordering of a Directed Acyclic Graph (DAG) using in-degrees.
   - Prove that if Kahn's algorithm terminates with fewer than $|V|$ processed vertices, the input graph must contain at least one directed cycle.

---

## Part II: Complete Worked Solutions & Grading Rubric

### Section A Solutions

#### 1.1 Formal Proof for $5n^3 - 2n^2 + 8n = \Theta(n^3)$ (5 pts)
We seek $c_1, c_2, n_0 > 0$ such that $c_1 n^3 \le 5n^3 - 2n^2 + 8n \le c_2 n^3$ for all $n \ge n_0$.
- **Upper Bound:** For $n \ge 1$:
  $$5n^3 - 2n^2 + 8n \le 5n^3 + 8n \le 5n^3 + 8n^3 = 13n^3 \implies c_2 = 13$$
- **Lower Bound:** For $n \ge 2$, $2n^2 \le n^3 \implies -2n^2 \ge -n^3$. Since $8n > 0$:
  $$5n^3 - 2n^2 + 8n \ge 5n^3 - n^3 = 4n^3 \implies c_1 = 4$$
- **Valid Region:** For all $n \ge n_0 = 2$, $4n^3 \le 5n^3 - 2n^2 + 8n \le 13n^3$. Therefore, $f(n) = \Theta(n^3)$. *(Rubric: 2.5 pts upper bound, 2.5 pts lower bound)*

#### 1.2 Limit Test for $g(n)$ vs $h(n)$ (5 pts)
$$
L = \lim_{n \to \infty} \frac{n^2 \log_2 n}{n^{2.5}} = \lim_{n \to \infty} \frac{\log_2 n}{n^{0.5}}
$$
Applying L'Hôpital's rule:
$$
\lim_{n \to \infty} \frac{\frac{1}{n \ln 2}}{\frac{1}{2} n^{-0.5}} = \lim_{n \to \infty} \frac{2}{\ln 2 \cdot n^{0.5}} = 0
$$
Since $L = 0$, $g(n) = o(h(n)) \implies g(n) = O(h(n))$ and $h(n) = \omega(g(n))$.

#### 2. Recurrence Resolutions (15 pts, 5 pts each)
- **$T_1(n) = 9 T_1(n/3) + n^2$:**
  $a = 9, b = 3 \implies n^{\log_3 9} = n^2$.
  Here $f(n) = n^2 = \Theta(n^2) = \Theta(n^{\log_b a})$.
  By Master Theorem **Case 2** ($k = 0$):
  $$T_1(n) = \Theta(n^2 \log n)$$

- **$T_2(n) = 4 T_2(n/2) + n^2 \log_2 n$:**
  $a = 4, b = 2 \implies n^{\log_2 4} = n^2$.
  Here $f(n) = n^2 \log_2 n = \Theta(n^{\log_b a} \log^1 n)$.
  By Master Theorem **Extended Case 2** ($k = 1$):
  $$T_2(n) = \Theta(n^2 \log^{1+1} n) = \Theta(n^2 \log^2 n)$$

- **$T_3(n) = T_3(n-1) + \frac{1}{n}$:**
  Unrolling the recurrence:
  $$T_3(n) = T_3(0) + \sum_{i=1}^n \frac{1}{i} = H_n$$
  Recall the $n$-th harmonic number satisfies $H_n = \ln n + \gamma + O(1/n)$.
  $$T_3(n) = \Theta(\log n)$$

---

### Section B Solutions

#### 1. BST Invariant and 3-Case Deletion (10 pts)
- **BST Invariant:** For node $x$, all keys in $x.\text{left} < x.\text{key}$ and all keys in $x.\text{right} > x.\text{key}$. In-order traversal recursively visits left subtree, current node, then right subtree. Since all left keys are smaller and all right keys are larger, induction proves values are emitted in monotonically increasing order. (4 pts)
- **Deletion Cases:**
  - Case 1 (Leaf): Node has no children. Free node and set parent's pointer to `nullptr`.
  - Case 2 (Single Child): Splice the child directly to the deleted node's parent.
  - Case 3 (Two Children): Find In-Order Successor (minimum node in right subtree). Overwrite deleted node's key with successor's key. Recursively delete successor from right subtree (which has at most one child). This preserves order because the successor is strictly greater than all nodes in the left subtree and strictly less than all remaining nodes in the right subtree. (6 pts)

#### 2. AVL Insertions and Rotations (15 pts)
1. **Insert 30:** Root `30` ($BF = 0$).
2. **Insert 20:** `30` has left child `20` ($BF(30) = +1$).
3. **Insert 10:** Left-Left chain $30 \to 20 \to 10$.
   - $BF(30) = +2$, $BF(20) = +1$.
   - **LL Imbalance** at `30` $\implies$ **Right Rotation** around `30`.
   - Result: `20` is root with children `10` and `30` ($BF(20) = 0$).
4. **Insert 25:** Enters as left child of `30`. Tree balanced ($BF(20) = -1, BF(30) = +1$).
5. **Insert 40:** Enters as right child of `30`. Tree balanced ($BF(20) = -1, BF(30) = 0$).
6. **Insert 50:** Enters as right child of `40`.
   - Node `30`: $h_L = 1, h_R = 2 \implies BF(30) = -1$.
   - Node `20`: $h_L = 1, h_R = 3 \implies BF(20) = -2$.
   - Right child `30` has $BF(30) = -1$.
   - **RR Imbalance** at `20` $\implies$ **Left Rotation** around `20`.
   - New root is `30`. Left child is `20` (with children `10`, `25`), right child is `40` (with child `50`). Balanced!
7. **Insert 22:** Inserts as left child of `25`.
   - Subtree at `20`: $h_L(20) = 1$ (node `10`), $h_R(20) = 2$ (path $25 \to 22$).
   - $BF(20) = 1 - 2 = -1$. Tree remains completely balanced!

---

### Section C Solutions

#### 1. Floyd's `buildMaxHeap` Trace & Complexity (12 pts)
Given array: `[4, 10, 3, 5, 1, 14, 8, 9, 2]` ($n = 9$).
Internal nodes: indices $\lfloor 9/2 \rfloor - 1 = 3$ down to 0.
- Index 3 (`5`): Children at 7 (`9`), 8 (`2`). Max child is `9`. Swap `5` and `9` $\implies [4, 10, 3, \mathbf{9}, 1, 14, 8, \mathbf{5}, 2]$.
- Index 2 (`3`): Children at 5 (`14`), 6 (`8`). Max child is `14`. Swap `3` and `14` $\implies [4, 10, \mathbf{14}, 9, 1, \mathbf{3}, 8, 5, 2]$.
- Index 1 (`10`): Children at 3 (`9`), 4 (`1`). $10 \ge 9, 1 \implies$ No swap.
- Index 0 (`4`): Children at 1 (`10`), 2 (`14`). Max child is `14`. Swap `4` and `14` $\implies [\mathbf{14}, 10, \mathbf{4}, 9, 1, 3, 8, 5, 2]$.
  - Sift down `4` at index 2: Children at 5 (`3`), 6 (`8`). Max child is `8`. Swap `4` and `8` $\implies [14, 10, \mathbf{8}, 9, 1, 3, \mathbf{4}, 5, 2]$.
- **Final Max-Heap:** `[14, 10, 8, 9, 1, 3, 4, 5, 2]`. (6 pts)
- **$O(n)$ Proof:** Most nodes reside near the leaves where height $k$ is small. Summing $\sum_{k=0}^{\lfloor \log n \rfloor} \frac{n}{2^{k+1}} k = \frac{n}{2} \sum \frac{k}{2^k} = \frac{n}{2} \cdot 2 = n = O(n)$. (6 pts)

#### 2. Hash Table Collision Resolution (13 pts)
$m = 11$, $h_1(k) = k \pmod{11}$, $h_2(k) = 7 - (k \pmod 7)$.
Keys: `[22, 33, 44, 15, 26, 37]`.

- **Linear Probing:**
  - `22`: $22 \pmod{11} = 0 \implies$ Slot 0.
  - `33`: $33 \pmod{11} = 0$ (Collision!). Probe 1: $(0 + 1) \pmod{11} = 1 \implies$ Slot 1.
  - `44`: $44 \pmod{11} = 0$ (Collision!). Probe 1: 1 (occupied). Probe 2: $(0 + 2) \pmod{11} = 2 \implies$ Slot 2.
  - `15`: $15 \pmod{11} = 4 \implies$ Slot 4.
  - `26`: $26 \pmod{11} = 4$ (Collision!). Probe 1: $(4 + 1) \pmod{11} = 5 \implies$ Slot 5.
  - `37`: $37 \pmod{11} = 4$ (Collision!). Probes 4, 5 occupied. Probe 2: $6 \implies$ Slot 6.
  - *Final Table (Linear):* `[0:22, 1:33, 2:44, 3:_, 4:15, 5:26, 6:37, 7:_, 8:_, 9:_, 10:_]`.

- **Double Hashing:**
  - `22`: Slot 0.
  - `33`: $h_1(33) = 0$. $h_2(33) = 7 - (33 \pmod 7) = 7 - 5 = 2$.
    Probe 1: $(0 + 1 \times 2) \pmod{11} = 2 \implies$ Slot 2.
  - `44`: $h_1(44) = 0$. $h_2(44) = 7 - (44 \pmod 7) = 7 - 2 = 5$.
    Probe 1: $(0 + 1 \times 5) \pmod{11} = 5 \implies$ Slot 5.
  - `15`: $h_1(15) = 4 \implies$ Slot 4.
  - `26`: $h_1(26) = 4$. $h_2(26) = 7 - (26 \pmod 7) = 7 - 5 = 2$.
    Probe 1: $(4 + 1 \times 2) \pmod{11} = 6 \implies$ Slot 6.
  - `37`: $h_1(37) = 4$. $h_2(37) = 7 - (37 \pmod 7) = 7 - 2 = 5$.
    Probe 1: $(4 + 1 \times 5) \pmod{11} = 9 \implies$ Slot 9.
  - *Final Table (Double):* `[0:22, 1:_, 2:33, 3:_, 4:15, 5:44, 6:26, 7:_, 8:_, 9:37, 10:_]`.
- **Clustering:** Primary clustering in linear probing causes long occupied runs to coalesce, increasing probe lengths for all nearby keys. Double hashing eliminates this because the step size depends on $h_2(k)$, dispersing collisions across different modulo cycles. (4 pts)

---

### Section D Solutions

#### 1. Dijkstra's Algorithm Trace (15 pts)
Initial distances from $A$: $d[A] = 0, d[B] = \infty, d[C] = \infty, d[D] = \infty, d[E] = \infty$.

| Iteration | Visited | Relaxed Edges | Tentative Distances $[d(A), d(B), d(C), d(D), d(E)]$ | Min-Priority Queue State |
|:---|:---|:---|:---|:---|
| Init | — | — | $[0, \infty, \infty, \infty, \infty]$ | $\{(0, A)\}$ |
| 1 | $A$ | $(A, B): 4, (A, C): 2$ | $[0, 4, 2, \infty, \infty]$ | $\{(2, C), (4, B)\}$ |
| 2 | $C$ | $(C, B): 2+1=3 < 4, (C, D): 2+8=10, (C, E): 2+10=12$ | $[0, 3, 2, 10, 12]$ | $\{(3, B), (10, D), (12, E)\}$ |
| 3 | $B$ | $(B, D): 3+5=8 < 10$ | $[0, 3, 2, 8, 12]$ | $\{(8, D), (12, E)\}$ |
| 4 | $D$ | $(D, E): 8+2=10 < 12$ | $[0, 3, 2, 8, 10]$ | $\{(10, E)\}$ |
| 5 | $E$ | $(E, D): 10+3=13 > 8$ | $[0, 3, 2, 8, 10]$ | $\emptyset$ |

**Final Shortest Paths:**
- $A \to A$: 0
- $A \to C$: 2
- $A \to C \to B$: 3
- $A \to C \to B \to D$: 8
- $A \to C \to B \to D \to E$: 10

#### 2. Kahn's Topological Sort & Cycle Proof (10 pts)
- **Algorithm:** Compute in-degrees $\text{in}[u]$ for all $u \in V$. Enqueue all vertices with $\text{in}[u] = 0$. While queue is non-empty, dequeue $u$, append to order, and for each outgoing edge $(u, v)$, decrement $\text{in}[v]$. If $\text{in}[v] = 0$, enqueue $v$. (5 pts)
- **Cycle Proof:** If the graph contains a directed cycle $C = v_1 \to v_2 \to \dots \to v_k \to v_1$, every vertex $v_i \in C$ has at least one incoming edge within $C$. Therefore, no vertex in $C$ can ever have in-degree 0 unless an edge in $C$ is removed. Since an edge in $C$ can only be removed after its source vertex is dequeued, no vertex in $C$ will ever be enqueued. Thus, all vertices in $C$ (and any downstream nodes) remain unprocessed. If the processed count $< |V|$, a cycle must exist. (5 pts)

