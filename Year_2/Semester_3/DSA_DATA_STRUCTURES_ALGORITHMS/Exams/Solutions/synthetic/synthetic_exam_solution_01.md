# University of Ioannina - Department of Informatics and Telecommunications
## Course: Data Structures and Algorithms (Course Code: 305)
### Academic Year: 2025-2026
### Synthetic Final Examination Solutions - Paper 01

---

### Solution 1: Asymptotic Complexity & Recurrence Relations (15 Marks)

#### Part A: Loop Analysis & Closed Form (8 Marks)
Given code:
```cpp
int sum_value = 0;
for (int i = 1; i <= n; i *= 2) {
    for (int j = 0; j < i; ++j) {
        for (int k = 1; k <= n; k += 2) {
            sum_value += (i * j) + k;
        }
    }
}
```

1. **Summation Formulation:**
   - Outer loop index $i$ assumes values $i = 2^p$ for integer $p \ge 0$, terminating when $2^p > n$. The number of outer iterations is $m = \lfloor \log_2 n \rfloor + 1$.
   - Middle loop iterates exactly $i = 2^p$ times for each value of $p$.
   - Innermost loop increments $k$ by $2$ starting from $1$ up to $n$. The number of inner loop executions is $\lceil n/2 \rceil$.
   - Inside the inner loop, `sum_value += (i * j) + k;` performs 2 additions (addition of $k$ and compound assignment $+=$) and 1 multiplication.

   The total number of inner loop executions $S(n)$ is:
   $$S(n) = \sum_{p=0}^{\lfloor \log_2 n \rfloor} \sum_{j=0}^{2^p - 1} \sum_{\substack{k=1 \\ k \text{ odd}}}^{n} 1 = \left\lceil \frac{n}{2} \right\rceil \sum_{p=0}^{\lfloor \log_2 n \rfloor} 2^p$$

2. **Closed-Form Evaluation:**
   Using the standard geometric series formula $\sum_{p=0}^{m-1} 2^p = 2^m - 1$:
   $$\sum_{p=0}^{\lfloor \log_2 n \rfloor} 2^p = 2^{\lfloor \log_2 n \rfloor + 1} - 1$$
   Since $2^{\lfloor \log_2 n \rfloor} \le n < 2^{\lfloor \log_2 n \rfloor + 1}$, we have:
   $$n < 2^{\lfloor \log_2 n \rfloor + 1} \le 2n$$
   Substituting this into $S(n)$:
   $$S(n) = \left\lceil \frac{n}{2} \right\rceil \left( 2^{\lfloor \log_2 n \rfloor + 1} - 1 \right)$$
   For large $n$, $S(n) \approx \frac{n}{2} (2n) = n^2$.

3. **Asymptotic Bound:**
   $$S(n) = \Theta(n^2)$$
   The total running time of the algorithm is strictly $\Theta(n^2)$.

---

#### Part B: Recurrence Relations (7 Marks)

1. **Recurrence 1:** $T(n) = 3T\left(\frac{n}{4}\right) + n \log_2 n$
   - Form: $T(n) = a T(n/b) + f(n)$ where $a = 3$, $b = 4$, and $f(n) = n \log_2 n$.
   - Critical exponent: $\log_b a = \log_4 3 \approx 0.7925$.
   - Comparison: $n^{\log_b a} = n^{\log_4 3} \approx n^{0.793}$.
   - We compare $f(n) = n \log_2 n$ to $n^{\log_4 3}$. Because $1 > \log_4 3$, we have:
     $$f(n) = \Omega\left(n^{\log_4 3 + \epsilon}\right) \quad \text{for } \epsilon \approx 1 - 0.793 = 0.207 > 0$$
   - **Regularity Condition Check:**
     $$a f\left(\frac{n}{b}\right) = 3 \left(\frac{n}{4} \log_2 \frac{n}{4}\right) = \frac{3}{4} n (\log_2 n - 2) \le \frac{3}{4} n \log_2 n$$
     For $c = \frac{3}{4} < 1$, the regularity condition $a f(n/b) \le c f(n)$ holds for all $n \ge 4$.
   - **Conclusion:** By Case 3 of the Master Theorem:
     $$T(n) = \Theta(f(n)) = \Theta(n \log n)$$

2. **Recurrence 2:** $T(n) = 4T\left(\frac{n}{2}\right) + n^2 \sqrt{n}$
   - Form: $a = 4$, $b = 2$, and $f(n) = n^{2.5}$.
   - Critical exponent: $\log_b a = \log_2 4 = 2$.
   - Comparison: $n^{\log_b a} = n^2$.
   - Here $f(n) = n^{2.5} = n^{2 + 0.5} = \Omega(n^{\log_2 4 + 0.5})$ where $\epsilon = 0.5 > 0$.
   - **Regularity Condition Check:**
     $$a f\left(\frac{n}{b}\right) = 4 \left(\frac{n}{2}\right)^{2.5} = 4 \frac{n^{2.5}}{2^{2.5}} = \frac{4}{4\sqrt{2}} n^{2.5} = \frac{1}{\sqrt{2}} n^{2.5} \approx 0.707 n^{2.5} \le c f(n)$$
     Choosing $c = \frac{1}{\sqrt{2}} < 1$, the regularity condition holds.
   - **Conclusion:** By Case 3 of the Master Theorem:
     $$T(n) = \Theta(n^{2.5}) = \Theta(n^2 \sqrt{n})$$

---

### Solution 2: Binary Search Trees & Structural Integrity (12 Marks)

#### Part A: BST Insertion & Traversals (6 Marks)
Inserted keys: $\{45, 23, 68, 12, 34, 56, 89, 7, 28, 50\}$

1. **Resulting Binary Search Tree:**
   ```
                45
              /    \
            23      68
           /  \    /  \
          12  34  56   89
         /    /   /
        7    28  50
   ```

2. **Traversals:**
   - **In-order (Left-Root-Right):** `7, 12, 23, 28, 34, 45, 50, 56, 68, 89` (strictly sorted).
   - **Pre-order (Root-Left-Right):** `45, 23, 12, 7, 34, 28, 68, 56, 50, 89`.
   - **Post-order (Left-Right-Root):** `7, 12, 28, 34, 23, 50, 56, 89, 68, 45`.

3. **Height and Balance Factors:**
   - Single node has height $0$.
   - Heights: $h(7)=0, h(12)=1, h(28)=0, h(34)=1, h(23)=2$.
   - $h(50)=0, h(56)=1, h(89)=0, h(68)=2$.
   - Overall tree height: $h(45) = 3$.
   - Balance factors $BF(u) = h(\text{left}) - h(\text{right})$:
     - $BF(7) = -1 - (-1) = 0$
     - $BF(12) = 0 - (-1) = 1$
     - $BF(28) = 0$
     - $BF(34) = 0 - (-1) = 1$
     - $BF(23) = h(12) - h(34) = 1 - 1 = 0$
     - $BF(50) = 0$
     - $BF(56) = 0 - (-1) = 1$
     - $BF(89) = 0$
     - $BF(68) = h(56) - h(89) = 1 - 0 = 1$
     - $BF(45) = h(23) - h(68) = 2 - 2 = 0$

---

#### Part B: Node Deletion via In-Order Successor (6 Marks)
1. **Tracing Deletion of Key `23`:**
   - Node `23` has two children (`12` and `34`).
   - The in-order successor is the minimum node in the right subtree: find the leftmost node starting from `34`, which is `28`.
   - Key `28` replaces `23` at the node.
   - Node `28` is then detached from its original position (left child of `34` becomes `nullptr`).

2. **BST After Deletion:**
   ```
                45
              /    \
            28      68
           /  \    /  \
          12  34  56   89
         /        /
        7        50
   ```

3. **AVL Invariant Verification:**
   - $BF(34) = -1 - (-1) = 0$
   - $BF(28) = h(12) - h(34) = 1 - 0 = 1$
   - $BF(45) = h(28) - h(68) = 2 - 2 = 0$
   - All balance factors satisfy $|BF(u)| \le 1$. The resulting tree remains a valid AVL tree.

---

### Solution 3: AVL Tree Construction & Rotations (16 Marks)

Keys inserted: $\{30, 20, 10, 40, 50, 25, 28\}$

- **Step 1: Insert 30**
  Tree: `(30)` | $BF(30) = 0$.

- **Step 2: Insert 20**
  `20` inserted as left child of `30`.
  $BF(20) = 0$, $BF(30) = 1$. Balanced.

- **Step 3: Insert 10**
  `10` inserted as left child of `20`.
  $BF(10) = 0$, $BF(20) = 1$, $BF(30) = 2$.
  Imbalance at node `30` with child `20` ($BF=+1$). **Left-Left (LL) Case**.
  Apply **Single Right Rotation** at node `30`:
  ```
         20 (BF=0)
        /  \
       10   30 (BF=0)
  ```

- **Step 4: Insert 40**
  `40` inserted as right child of `30`.
  $BF(40) = 0$, $BF(30) = -1$, $BF(20) = 0 - 1 = -1$. Balanced.

- **Step 5: Insert 50**
  `50` inserted as right child of `40`.
  $BF(50) = 0$, $BF(40) = -1$, $BF(30) = -1 - 0 = -2$.
  Imbalance at node `30` with child `40` ($BF=-1$). **Right-Right (RR) Case**.
  Apply **Single Left Rotation** at node `30`:
  ```
         20 (BF=-1)
        /  \
       10   40 (BF=0)
           /  \
          30   50 (BF=0)
  ```

- **Step 6: Insert 25**
  `25` inserted as left child of `30`.
  $BF(25) = 0$, $BF(30) = 1$, $BF(40) = 1 - 0 = 1$.
  $BF(20) = h(10) - h(40) = 0 - 2 = -2$.
  Imbalance at root `20` ($BF = -2$), right child `40` has $BF = +1$. **Right-Left (RL) Case**.
  Apply **Double Right-Left Rotation** at node `20`:
  1. Right rotate at node `40`: `30` rises, `40` becomes right child of `30`, `25` stays left child of `30`.
  2. Left rotate at node `20`: `30` becomes the new root; `20` becomes left child of `30`, taking `25` as its right child.
  ```
              30 (BF=0)
            /    \
          20      40 (BF=-1)
         /  \       \
        10  25       50
  ```
  Check balance factors:
  $BF(10)=0, BF(25)=0 \implies BF(20) = 0 - 0 = 0$.
  $BF(50)=0 \implies BF(40) = -1 - 0 = -1$.
  $BF(30) = h(20) - h(40) = 1 - 1 = 0$. Tree fully balanced.

- **Step 7: Insert 28**
  `28` inserted as right child of `25`.
  $BF(28) = 0$, $BF(25) = -1 - 0 = -1$.
  $BF(20) = h(10) - h(25) = 0 - 1 = -1$.
  $BF(30) = h(20) - h(40) = 2 - 1 = 1$.
  All $|BF| \le 1$. No further rotations required.

**Final AVL Tree:**
```
              30
            /    \
          20      40
         /  \       \
        10  25       50
              \
               28
```

---

### Solution 4: AVL Node Deletion & Cascading Rebalancing (12 Marks)

Given initial AVL tree:
```
              44
            /    \
          17      62
         /  \    /  \
        10  28  50  78
            /         \
           22         88
```

1. **Balance Factors Verification:**
   - $h(10)=0 \implies BF(10)=0$
   - $h(22)=0 \implies BF(22)=0$
   - $h(28)=1 \implies BF(28) = 0 - (-1) = 1$
   - $h(17)=2 \implies BF(17) = 0 - 1 = -1$
   - $h(50)=0 \implies BF(50)=0$
   - $h(88)=0 \implies BF(88)=0$
   - $h(78)=1 \implies BF(78) = -1 - 0 = -1$
   - $h(62)=2 \implies BF(62) = 0 - 1 = -1$
   - $h(44)=3 \implies BF(44) = 2 - 2 = 0$
   All nodes have $|BF| \le 1$.

2. **Deletion of Key `50`:**
   - Node `50` is a leaf; remove it by setting the left child of `62` to `nullptr`.

3. **Rebalancing after Deleting `50`:**
   - Retracing up to parent `62`:
     Left subtree height is $-1$; right subtree (rooted at `78`) height is $1$.
     $$BF(62) = -1 - 1 = -2 \quad (\text{Imbalance!})$$
   - Look at right child `78`: $BF(78) = -1 \le 0$.
   - This matches the **Right-Right (RR) Case**.
   - Perform **Single Left Rotation** at node `62`:
     - Node `78` ascends to replace `62`.
     - Node `62` becomes the left child of `78`.
     - Subtree rooted at `78` has children `62` (left) and `88` (right).
     - $BF(62) = 0$, $BF(88) = 0$, $BF(78) = 0$, height of `78` is $1$.
   - Check parent `44`:
     Left subtree (rooted at `17`) height is $2$.
     Right subtree (rooted at `78`) height is $1$.
     $$BF(44) = 2 - 1 = 1 \quad (|BF| \le 1)$$
   - Intermediate Tree:
     ```
                   44
                 /    \
               17      78
              /  \    /  \
             10  28  62  88
                 /
                22
     ```

4. **Deletion of Key `62`:**
   - Node `62` is currently a leaf; remove it.
   - Retrace up to node `78`:
     Left child is `nullptr` (height $-1$), right child is `88` (height $0$).
     $$BF(78) = -1 - 0 = -1 \quad (|BF| \le 1)$$
     Height of `78` is $1$.
   - Retrace up to root `44`:
     Left child `17` has height $2$, right child `78` has height $1$.
     $$BF(44) = 2 - 1 = 1 \quad (|BF| \le 1)$$
   - No rotation required.

**Final Tree:**
```
              44
            /    \
          17      78
         /  \       \
        10  28       88
            /
           22
```

---

### Solution 5: Binary Heaps & Floyd's Linear-Time Construction (15 Marks)

#### Part A: Floyd's Bottom-Up `buildHeap` (9 Marks)
Given array: $A = [14, 33, 27, 45, 62, 19, 81, 92, 55, 38]$ ($n = 10$).

1. **Initial Complete Binary Tree:**
   ```
                 14 [0]
              /          \
          33 [1]          27 [2]
         /      \        /      \
      45 [3]  62 [4]  19 [5]  81 [6]
      /   \    /
    92[7] 55[8] 38[9]
   ```

2. **Bottom-Up Heapification Trace:**
   Non-leaf indices run from $i = \lfloor n/2 \rfloor - 1 = \lfloor 10/2 \rfloor - 1 = 4$ down to $0$.

   - **Index $i = 4$ ($A[4] = 62$):**
     Child: Left child at index $2(4) + 1 = 9$ ($A[9] = 38$).
     $62 \ge 38 \implies$ no swap. Array unchanged.

   - **Index $i = 3$ ($A[3] = 45$):**
     Children: Index $7$ ($A[7] = 92$) and Index $8$ ($A[8] = 55$).
     Max child is $A[7] = 92$. Since $92 > 45$, swap $A[3]$ and $A[7]$.
     Subtree at index $7$ has no children.
     Array: `[14, 33, 27, 92, 62, 19, 81, 45, 55, 38]`.

   - **Index $i = 2$ ($A[2] = 27$):**
     Children: Index $5$ ($A[5] = 19$) and Index $6$ ($A[6] = 81$).
     Max child is $A[6] = 81$. Since $81 > 27$, swap $A[2]$ and $A[6]$.
     Subtree at index $6$ has no children.
     Array: `[14, 33, 81, 92, 62, 19, 27, 45, 55, 38]`.

   - **Index $i = 1$ ($A[1] = 33$):**
     Children: Index $3$ ($A[3] = 92$) and Index $4$ ($A[4] = 62$).
     Max child is $A[3] = 92$. Since $92 > 33$, swap $A[1]$ and $A[3]$.
     Continue percolateDown from index $3$:
     Children of index $3$: Index $7$ ($A[7] = 45$) and Index $8$ ($A[8] = 55$).
     Max child is $A[8] = 55$. Since $55 > 33$, swap $A[3]$ and $A[8]$.
     Subtree at index $8$ has no children.
     Array: `[14, 92, 81, 55, 62, 19, 27, 45, 33, 38]`.

   - **Index $i = 0$ ($A[0] = 14$):**
     Children: Index $1$ ($A[1] = 92$) and Index $2$ ($A[2] = 81$).
     Max child is $A[1] = 92$. Since $92 > 14$, swap $A[0]$ and $A[1]$.
     Continue percolateDown from index $1$:
     Children: Index $3$ ($A[3] = 55$) and Index $4$ ($A[4] = 62$).
     Max child is $A[4] = 62$. Since $62 > 14$, swap $A[1]$ and $A[4]$.
     Continue percolateDown from index $4$:
     Child: Index $9$ ($A[9] = 38$).
     Since $38 > 14$, swap $A[4]$ and $A[9]$.
     Subtree at index $9$ has no children.

3. **Final Max-Heap Array:**
   $$A = [92, 62, 81, 55, 38, 19, 27, 45, 33, 14]$$

4. **Final Max-Heap Tree Structure:**
   ```
                 92
              /      \
            62        81
          /    \     /  \
         55    38   19  27
        /  \   /
       45  33 14
   ```

---

#### Part B: Heap Extraction and Insertion (6 Marks)

1. **`extractMax()` Trace:**
   - Root `92` removed.
   - Last element $A[9] = 14$ moved to root $A[0]$. Heap size reduced to $9$.
   - Array: `[14, 62, 81, 55, 38, 19, 27, 45, 33]`.
   - `percolateDown(0)`:
     Children: $A[1] = 62$, $A[2] = 81$. Max child is $81$. Swap $A[0]$ and $A[2]$.
     Array: `[81, 62, 14, 55, 38, 19, 27, 45, 33]`.
   - `percolateDown(2)`:
     Children: $A[5] = 19$, $A[6] = 27$. Max child is $27$. Swap $A[2]$ and $A[6]$.
     Array: `[81, 62, 27, 55, 38, 19, 14, 45, 33]`.
   - Leaf reached. State: `[81, 62, 27, 55, 38, 19, 14, 45, 33]`.

2. **Insert Key `95`:**
   - Append `95` at index $9$: $A[9] = 95$.
   - Parent index $\lfloor (9-1)/2 \rfloor = 4$ ($A[4] = 38$).
   - Since $95 > 38$, swap $A[9]$ and $A[4]$.
   - Parent index $\lfloor (4-1)/2 \rfloor = 1$ ($A[1] = 62$).
   - Since $95 > 62$, swap $A[4]$ and $A[1]$.
   - Parent index $\lfloor (1-1)/2 \rfloor = 0$ ($A[0] = 81$).
   - Since $95 > 81$, swap $A[1]$ and $A[0]$.
   - Final Array after insertion:
     $$A = [95, 81, 27, 55, 62, 19, 14, 45, 33, 38]$$

---

### Solution 6: Hash Tables & Collision Resolution Strategies (15 Marks)

Keys: $\{35, 12, 46, 23, 79, 57, 68\}$, table capacity $M = 11$.
- $h_1(k) = k \pmod{11}$
- $h_2(k) = 7 - (k \pmod 7)$

Hash values for all keys:
| Key ($k$) | $k \pmod{11}$ ($h_1$) | $k \pmod 7$ | $h_2(k) = 7 - (k \pmod 7)$ |
|:---------:|:---------------------:|:-----------:|:--------------------------:|
| 35        | 2                     | 0           | 7                          |
| 12        | 1                     | 5           | 2                          |
| 46        | 2                     | 4           | 3                          |
| 23        | 1                     | 2           | 5                          |
| 79        | 2                     | 2           | 5                          |
| 57        | 2                     | 1           | 6                          |
| 68        | 2                     | 5           | 2                          |

---

#### Part A: Separate Chaining (4 Marks)
Table with linked lists:
- Index 0: `nullptr`
- Index 1: `12` -> `23` -> `nullptr`
- Index 2: `35` -> `46` -> `79` -> `57` -> `68` -> `nullptr`
- Indices 3–10: `nullptr`

---

#### Part B: Linear Probing (5 Marks)
Probe sequence: $h(k, i) = (h_1(k) + i) \pmod{11}$

1. Insertion trace:
   - **Key 35:** $h_1 = 2$. Slot 2 empty $\implies T[2] = 35$. (1 probe)
   - **Key 12:** $h_1 = 1$. Slot 1 empty $\implies T[1] = 12$. (1 probe)
   - **Key 46:** $h_1 = 2$ (collision with 35). $i=1 \implies (2+1)\%11 = 3$ empty $\implies T[3] = 46$. (2 probes)
   - **Key 23:** $h_1 = 1$ (collision with 12). $i=1 \implies 2$ (collides), $i=2 \implies 3$ (collides), $i=3 \implies 4$ empty $\implies T[4] = 23$. (4 probes)
   - **Key 79:** $h_1 = 2$ (collides with 35, 46, 23). $i=3 \implies (2+3)\%11 = 5$ empty $\implies T[5] = 79$. (4 probes)
   - **Key 57:** $h_1 = 2$ (collides at 2, 3, 4, 5). $i=4 \implies (2+4)\%11 = 6$ empty $\implies T[6] = 57$. (5 probes)
   - **Key 68:** $h_1 = 2$ (collides at 2, 3, 4, 5, 6). $i=5 \implies (2+5)\%11 = 7$ empty $\implies T[7] = 68$. (6 probes)

2. Table Array $T[0 \dots 10]$:
   `[EMPTY, 12, 35, 46, 23, 79, 57, 68, EMPTY, EMPTY, EMPTY]`

3. Average Successful Search Probes:
   $$\text{Avg Probes} = \frac{1 + 1 + 2 + 4 + 4 + 5 + 6}{7} = \frac{23}{7} \approx 3.29 \text{ probes}$$

---

#### Part C: Double Hashing (6 Marks)
Probe sequence: $h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod{11}$

1. Insertion trace:
   - **Key 35:** $i=0 \implies 2$. Slot 2 empty $\implies T[2] = 35$. (1 probe)
   - **Key 12:** $i=0 \implies 1$. Slot 1 empty $\implies T[1] = 12$. (1 probe)
   - **Key 46:** $i=0 \implies 2$ (collision).
     $i=1 \implies (2 + 1 \cdot 3) \pmod{11} = 5$. Slot 5 empty $\implies T[5] = 46$. (2 probes)
   - **Key 23:** $i=0 \implies 1$ (collision).
     $i=1 \implies (1 + 1 \cdot 5) \pmod{11} = 6$. Slot 6 empty $\implies T[6] = 23$. (2 probes)
   - **Key 79:** $i=0 \implies 2$ (collision).
     $i=1 \implies (2 + 1 \cdot 5) \pmod{11} = 7$. Slot 7 empty $\implies T[7] = 79$. (2 probes)
   - **Key 57:** $i=0 \implies 2$ (collision).
     $i=1 \implies (2 + 1 \cdot 6) \pmod{11} = 8$. Slot 8 empty $\implies T[8] = 57$. (2 probes)
   - **Key 68:** $i=0 \implies 2$ (collision).
     $i=1 \implies (2 + 1 \cdot 2) \pmod{11} = 4$. Slot 4 empty $\implies T[4] = 68$. (2 probes)

2. Final Table State:
   `[EMPTY, 12, 35, EMPTY, 68, 46, 23, 79, 57, EMPTY, EMPTY]`

3. Unsuccessful Search for Key `90`:
   - $h_1(90) = 90 \pmod{11} = 2$.
   - $h_2(90) = 7 - (90 \pmod 7) = 7 - 6 = 1$.
   - Probe $i=0$: index $(2 + 0) \pmod{11} = 2 \implies T[2] = 35 \ne 90$.
   - Probe $i=1$: index $(2 + 1) \pmod{11} = 3 \implies T[3] = \text{EMPTY}$.
   - Search terminates with failure at slot 3.
   - Total probes required = **2 probes**.

---

### Solution 7: Huffman Coding & Algorithmic Implementation (15 Marks)

#### Part A: Huffman Tree Construction (8 Marks)
Character frequencies:
$\Sigma = \{A: 28, B: 15, C: 12, D: 22, E: 5, F: 18\}$, Total $N = 100$.

1. **Priority Queue Trace:**
   - Initial min-heap: `[E:5, C:12, B:15, F:18, D:22, A:28]`
   - Iteration 1: Extract `E(5)` and `C(12)`. Merge into internal node `EC(17)`.
     Queue: `[B:15, EC:17, F:18, D:22, A:28]`
   - Iteration 2: Extract `B(15)` and `EC(17)`. Merge into internal node `B_EC(32)`.
     Queue: `[F:18, D:22, A:28, B_EC:32]`
   - Iteration 3: Extract `F(18)` and `D(22)`. Merge into internal node `FD(40)`.
     Queue: `[A:28, B_EC:32, FD:40]`
   - Iteration 4: Extract `A(28)` and `B_EC(32)`. Merge into internal node `A_BEC(60)`.
     Queue: `[FD:40, A_BEC:60]`
   - Iteration 5: Extract `FD(40)` and `A_BEC(60)`. Merge into root `Root(100)`.

2. **Binary Tree Structure (Left = 0, Right = 1):**
   ```
                       [Root: 100]
                     /             \
                   0/               \1
               [FD: 40]          [A_BEC: 60]
               /      \          /         \
             0/        \1      0/           \1
           F(18)      D(22)   A(28)      [B_EC: 32]
                                         /        \
                                       0/          \1
                                      B(15)      [EC: 17]
                                                 /      \
                                               0/        \1
                                              E(5)       C(12)
   ```

3. **Prefix Codes & Code Lengths:**
   | Symbol | Frequency ($f_i$) | Codeword | Length ($l_i$) | Total Bits ($f_i \cdot l_i$) |
   |:------:|:-----------------:|:--------:|:--------------:|:----------------------------:|
   | A      | 28                | `10`     | 2              | 56                           |
   | B      | 15                | `110`    | 3              | 45                           |
   | C      | 12                | `1111`   | 4              | 48                           |
   | D      | 22                | `01`     | 2              | 44                           |
   | E      | 5                 | `1110`   | 4              | 20                           |
   | F      | 18                | `00`     | 2              | 36                           |
   | **Total** | **100**        | —        | —              | **249 bits**                 |

4. **Metrics:**
   - **Total Compressed Size:** $249 \text{ bits}$.
   - **Average Codeword Length:**
     $$L_{\text{avg}} = \frac{249 \text{ bits}}{100 \text{ symbols}} = 2.49 \text{ bits/symbol}$$
   - **Uncompressed ASCII Size:** $100 \times 8 = 800 \text{ bits}$.
   - **Compression Ratio:**
     $$\text{Space Saving} = \frac{800 - 249}{800} \times 100\% = 68.875\%$$
     $$\text{Compression Factor} = \frac{800}{249} \approx 3.21 : 1$$

---

#### Part B: C++ Implementation (7 Marks)

```cpp
#include <vector>
#include <utility>

/**
 * Partitions a sub-array around a pivot using Hoare's two-pointer partitioning scheme.
 *
 * Args:
 *     arr_data (std::vector<int>&): Reference to the vector containing elements to partition.
 *     low_idx (int): The starting index of the sub-array.
 *     high_idx (int): The ending index of the sub-array.
 *
 * Returns:
 *     int: The split index dividing the two partitioned segments.
 */
int hoarePartition(std::vector<int>& arr_data, int low_idx, int high_idx) {
    int pivot_val = arr_data[low_idx]; // Selects first element as pivot baseline
    int left_ptr = low_idx - 1;        // Starts one position before left boundary
    int right_ptr = high_idx + 1;      // Starts one position after right boundary

    while (true) {
        // Advances left pointer past elements smaller than pivot
        do {
            ++left_ptr;
        } while (arr_data[left_ptr] < pivot_val);

        // Decrements right pointer past elements greater than pivot
        do {
            --right_ptr;
        } while (arr_data[right_ptr] > pivot_val);

        // Returns split index when pointers cross
        if (left_ptr >= right_ptr) {
            return right_ptr;
        }

        // Swaps misplaced elements across the partition boundary
        std::swap(arr_data[left_ptr], arr_data[right_ptr]);
    }
}
```

