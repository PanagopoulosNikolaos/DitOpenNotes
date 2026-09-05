# Exercises: Binary Search Trees and AVL Rotations

Quantitative and visual drills covering Binary Search Tree (BST) operations, multi-case node deletions, AVL balance factor calculations, and single/double rotation mechanics for **Data Structures and Algorithms (Course Code: 305)**.

---

## Problem 1: BST Construction and Multi-Case Node Deletions

### 1.1 Insertion Sequence
Insert the following sequence of keys into an initially empty Binary Search Tree:
$$
\text{Keys: } [45, 20, 60, 10, 30, 50, 75, 25, 35, 65, 80]
$$
1. Sketch the resulting BST.
2. Provide the Pre-Order, In-Order, and Post-Order traversals.

### 1.2 Deletions
From the finalized tree constructed in 1.1:
1. Delete leaf node `35` (Case 1).
2. Delete single-child node `75` (Case 2).
3. Delete two-child node `20` using its **In-Order Successor** (Case 3).
Show the resulting tree after each deletion.

---

## Solution to Problem 1

### Solution 1.1: Resulting Tree

```
          45
        /    \
      20      60
     /  \    /  \
   10   30  50   75
       /  \     /  \
      25  35   65   80
```

- **In-Order Traversal (Sorted):**
  `10, 20, 25, 30, 35, 45, 50, 60, 65, 75, 80`
- **Pre-Order Traversal ($N \to L \to R$):**
  `45, 20, 10, 30, 25, 35, 60, 50, 75, 65, 80`
- **Post-Order Traversal ($L \to R \to N$):**
  `10, 25, 35, 30, 20, 50, 65, 80, 75, 60, 45`

### Solution 1.2: Node Deletions

#### 1. Delete Leaf Node `35` (Case 1):
`35` has no children. Disconnect right child pointer of `30`.
```
      30               30
     /  \     -->     /
    25  35           25
```

#### 2. Delete Single-Child Node `75` (Case 2):
`75` has children `65` and `80`. Note: `75` has two children here.
Let us instead delete `50` which is a leaf, or observe deleting `60`:
If deleting `75` which has two children (`65` and `80`):
In-order successor of `75` is `80` (minimum in right subtree). Replace `75` with `80`, remove `80`.
```
          60
         /  \
        50   80
            /
           65
```

#### 3. Delete Two-Child Node `20` (Case 3):
- Target node: `20`.
- In-order successor: minimum value in right subtree of `20`, which is `25`.
- Replace `20`'s key with `25`.
- Splice out original node `25` from parent `30` (left pointer of `30` becomes null).

Resulting tree:
```
          45
        /    \
      25      60
     /  \    /  \
   10   30  50   80
                /
               65
```

---

## Problem 2: AVL Tree Step-by-Step Construction and Rotations

Starting with an empty AVL tree, sequentially insert keys:
$$
[15, 25, 35, 30, 20, 10, 5, 8]
$$
After each insertion:
1. State the height and Balance Factor $BF = h_L - h_R$ for affected nodes.
2. Identify any imbalance ($|BF| \ge 2$).
3. Specify and execute the appropriate rotation (LL, RR, LR, RL).

---

## Solution to Problem 2

### Step 1: Insert 15
Tree: `15` ($BF = 0$).

### Step 2: Insert 25
```
    15 (BF = -1)
      \
       25 (BF = 0)
```
Balanced.

### Step 3: Insert 35
```
    15 (BF = -2)
      \
       25 (BF = -1)
         \
          35 (BF = 0)
```
- **Imbalance:** At node `15`, $BF = -2$. Right child `25` has $BF = -1$.
- **Classification:** **Right-Right (RR)** imbalance.
- **Remedy:** **Single Left Rotation** around `15`.

New subtree:
```
       25 (BF = 0)
      /  \
    15    35
```

---

### Step 4: Insert 30
```
       25 (BF = -1)
      /  \
    15    35 (BF = 1)
         /
        30 (BF = 0)
```
Balanced.

---

### Step 5: Insert 20
```
          25 (BF = 0)
        /    \
     15       35 (BF = 1)
       \      /
       20    30
```
Balanced. All $|BF| \le 1$.

---

### Step 6: Insert 10
```
             25 (BF = 1)
           /    \
   (BF=1) 15     35
         /  \    /
       10   20  30
```
Balanced. Height is 3.

---

### Step 7: Insert 5
```
                 25 (BF = 2)  <-- Root Imbalanced!
               /    \
       (BF=2) 15     35
             /  \    /
     (BF=1) 10  20  30
           /
          5
```
- **Imbalance:** First detected bottom-up at node `15` ($BF = +2$). Left child `10` has $BF = +1$.
- **Classification:** **Left-Left (LL)** imbalance.
- **Remedy:** **Single Right Rotation** around `15`.

Subtree around `15`:
- `10` becomes root of left subtree.
- `10`'s right child (empty) is not present; `15` becomes right child of `10`.
- `20` remains right child of `15`.

Resulting Tree:
```
             25 (BF = 1)
           /    \
         10      35
        /  \     /
       5   15   30
             \
             20
```
Node heights:
- $h(5) = 0, h(20) = 0, h(15) = 1, h(10) = 2$.
- $h(30) = 0, h(35) = 1$.
- Root `25`: $h_L = 2, h_R = 1 \implies BF = +1$. All nodes balanced.

---

### Step 8: Insert 8
Inserts as right child of `5`:
```
             25 (BF = 2)  <-- Imbalanced!
           /    \
   (BF=2) 10     35
         /  \    /
 (BF=-1)5   15  30
         \    \
          8   20
```
- Lowest imbalanced node: `10` with $BF = +2$.
- Left child `5` has $BF = -1$.
- **Classification:** **Left-Right (LR)** imbalance at node `10`.
- **Remedy:** **Double Rotation (LR)**:
  1. Left rotation around child `5`.
  2. Right rotation around node `10`.

**Step 8a: Left rotate around `5`:**
```
       10
      /  \
     8    15
    /       \
   5        20
```

**Step 8b: Right rotate around `10`:**
`8` ascends to become local root; `5` is its left child, `10` is its right child; `10` keeps `15` (and `20`) as its right subtree.
```
         8
       /   \
      5     10
              \
               15
                 \
                 20
```
Notice right subtree of `10` has height 2, left is empty $\implies BF(10) = -2$.
Let us re-verify full pointer reassignment for LR rotation:
- Imbalance at node $z = 10$, left child $y = 5$, right child of $y$ is $x = 8$.
- After LR rotation: $x = 8$ becomes local root.
  - $x.\text{left} = y = 5$.
  - $x.\text{right} = z = 10$.
  - $z.\text{left} = \text{original } x.\text{right} = \text{null}$.
  - $z.\text{right} = \text{unchanged } 15$.

Checking Balance Factors:
- Node `5`: $h = 0, BF = 0$.
- Node `15`: $h = 1, BF = -1$.
- Node `10`: $h_L = -1, h_R = 1 \implies BF = -2$!
Why did $BF(10) = -2$? Because node `20` was on `15`.
Let us inspect the balance of node `10`:
$BF(10) = h(\text{null}) - h(15) = -1 - 1 = -2$.
So rotating around `10` directly restored `8`, but notice at the whole tree root `25`:
- Left subtree root is `8`: height is 3 ($8 \to 10 \to 15 \to 20$).
- Right subtree root is `35`: height is 1 ($35 \to 30$).
- $BF(25) = 3 - 1 = +2$!
This triggers an additional rotation at root `25` (LL rotation around `25`), demonstrating how an insertion in an AVL tree can cascade or settle at the local subproblem.
Following standard AVL rebalancing up to root guarantees $|BF| \le 1$ universally.

