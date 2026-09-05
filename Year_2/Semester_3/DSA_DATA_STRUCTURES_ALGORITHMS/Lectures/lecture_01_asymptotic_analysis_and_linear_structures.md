# Lecture 01: Asymptotic Analysis and Linear Data Structures

This lecture establishes the mathematical foundations of computational complexity analysis, asymptotic notations, amortized cost models, and the internal mechanics of fundamental linear data structures including dynamic arrays, linked lists, stacks, and queues.

---

## 1. Asymptotic Complexity and Growth of Functions

Algorithm analysis evaluates computational resource utilization (time and memory) as input size $n \to \infty$.

### 1.1 Formal Mathematical Definitions

Let $f(n)$ and $g(n)$ be functions mapping $\mathbb{N} \to \mathbb{R}^+$.

1. **Big-$O$ Notation (Asymptotic Upper Bound):**
   $$
   O(g(n)) = \{ f(n) : \exists c > 0, n_0 > 0 \text{ such that } 0 \le f(n) \le c \cdot g(n) \quad \forall n \ge n_0 \}
   $$
2. **Big-$\Omega$ Notation (Asymptotic Lower Bound):**
   $$
   \Omega(g(n)) = \{ f(n) : \exists c > 0, n_0 > 0 \text{ such that } 0 \le c \cdot g(n) \le f(n) \quad \forall n \ge n_0 \}
   $$
3. **Big-$\Theta$ Notation (Asymptotically Tight Bound):**
   $$
   \Theta(g(n)) = \{ f(n) : \exists c_1 > 0, c_2 > 0, n_0 > 0 \text{ such that } 0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \quad \forall n \ge n_0 \}
   $$
   **Theorem:** $f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \text{ and } f(n) = \Omega(g(n))$.

4. **Strict Bounds (Little-$o$ and Little-$\omega$):**
   - $f(n) = o(g(n)) \iff \lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$
   - $f(n) = \omega(g(n)) \iff \lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$

### 1.2 The Limit Test for Asymptotic Classification
Evaluating the ratio limit simplifies asymptotic comparisons:
$$
L = \lim_{n \to \infty} \frac{f(n)}{g(n)} = \begin{cases}
0, & f(n) = o(g(n)) \implies f(n) = O(g(n)) \\
c \in (0, \infty), & f(n) = \Theta(g(n)) \\
\infty, & f(n) = \omega(g(n)) \implies f(n) = \Omega(g(n))
\end{cases}
$$
Apply L'Hôpital's Rule when encountering indeterminate forms $\left[\frac{\infty}{\infty}\right]$.

---

## 2. Dynamic Arrays and Amortized Analysis

A static array allocates fixed contiguous memory. A dynamic array (`std::vector` in C++) grows dynamically to accommodate unbounded insertions.

### 2.1 Geometric Resizing Mechanics
When the current element count $N$ reaches capacity $C$:
1. Allocate new memory block of capacity $\alpha \cdot C$ (commonly $\alpha = 2$).
2. Copy existing $N$ elements to the new buffer.
3. Deallocate the legacy memory block.
4. Append the incoming element.

### 2.2 Proof of Amortized $O(1)$ Insertion via Aggregate Method
Consider inserting $N = 2^k$ elements into an initially empty array of capacity 1 with growth factor $\alpha = 2$.
- Resizing occurs at sizes $i = 1, 2, 4, 8, \dots, 2^{k-1}$.
- Copy cost for resizing at size $2^j$ is $2^j$ operations.
- Total copy cost for $N$ insertions:
  $$
  T_{\text{copy}}(N) = \sum_{j=0}^{k-1} 2^j = 2^k - 1 = N - 1
  $$
- Constant insertion cost for $N$ append operations is $N$.
- Total work:
  $$
  T_{\text{total}}(N) = N + (N - 1) = 2N - 1
  $$
- Amortized cost per operation:
  $$
  \hat{c} = \frac{T_{\text{total}}(N)}{N} = \frac{2N - 1}{N} < 2 = O(1)
  $$

```mermaid
graph TD
    A[Initial Cap: 1 | Elements: 1] -->|Resize 2x| B[Cap: 2 | Elements: 2]
    B -->|Resize 2x| C[Cap: 4 | Elements: 4]
    C -->|Resize 2x| D[Cap: 8 | Elements: 8]
    style A fill:#e1f5fe
    style B fill:#b3e5fc
    style C fill:#81d4fa
    style D fill:#4fc3f7
```

---

## 3. Linked Lists

Linked lists store elements non-contiguously in heap memory, where each node encapsulates payload data and pointer links.

```cpp
template <typename T>
struct Node {
    T data;
    Node* next;
    Node* prev; // Present in doubly linked lists
    Node(const T& val) : data(val), next(nullptr), prev(nullptr) {}
};
```

### 3.1 Structural Comparison

| Property | Dynamic Array (`std::vector`) | Singly Linked List (`std::forward_list`) | Doubly Linked List (`std::list`) |
|:---|:---|:---|:---|
| Memory Layout | Contiguous | Fragmented heap nodes | Fragmented heap nodes |
| Cache Locality | Outstanding (spatial prefetching) | Poor (pointer chasing) | Poor (pointer chasing) |
| Random Access ($k$-th element) | $O(1)$ | $O(k)$ | $O(k)$ |
| Prepend (`push_front`) | $O(n)$ | $O(1)$ | $O(1)$ |
| Append (`push_back`) | $O(1)$ amortized | $O(1)$ with tail pointer | $O(1)$ with tail pointer |
| Insertion/Deletion at Cursor | $O(n)$ | $O(1)$ | $O(1)$ |
| Per-Element Overhead | 0 bytes | 8 bytes (`next` pointer on 64-bit) | 16 bytes (`next` + `prev`) |

---

## 4. Stacks and Queues

### 4.1 LIFO Stack
The Stack follows Last-In, First-Out semantics:
- `push(x)`: Inserts element to top ($O(1)$).
- `pop()`: Removes and returns top element ($O(1)$).
- `top()` / `peek()`: Inspects top element ($O(1)$).
- Primary Applications: Function call frame stack, recursive backtrackers, parenthesis validation, arithmetic expression parsing (Shunting-Yard algorithm).

### 4.2 FIFO Queue and Circular Buffer
The Queue follows First-In, First-Out semantics:
- `enqueue(x)`: Appends element to tail ($O(1)$).
- `dequeue()`: Removes element from head ($O(1)$).

When implemented over a static array of capacity $M$, a linear queue suffers from false overflow. A **Circular Buffer** resolves this using modular arithmetic:
$$
\text{tail} \leftarrow (\text{tail} + 1) \pmod M
$$
$$
\text{head} \leftarrow (\text{head} + 1) \pmod M
$$

```cpp
template <typename T, size_t Capacity>
class CircularQueue {
private:
    T buffer_[Capacity];
    size_t head_ = 0;
    size_t tail_ = 0;
    size_t count_ = 0;

public:
    bool enqueue(const T& item) {
        if (count_ == Capacity) return false; // Buffer full
        buffer_[tail_] = item;
        tail_ = (tail_ + 1) % Capacity;
        ++count_;
        return true;
    }

    bool dequeue(T& out_item) {
        if (count_ == 0) return false; // Buffer empty
        out_item = buffer_[head_];
        head_ = (head_ + 1) % Capacity;
        --count_;
        return true;
    }
};
```

---

## 5. Algorithmic Complexity Summary

| Data Structure | Access | Search | Insertion | Deletion | Space Complexity |
|:---|:---|:---|:---|:---|:---|
| Array (Static) | $O(1)$ | $O(n)$ | N/A | N/A | $O(n)$ |
| Dynamic Array | $O(1)$ | $O(n)$ | $O(1)$ amortized | $O(1)$ back / $O(n)$ middle | $O(n)$ |
| Singly Linked List | $O(n)$ | $O(n)$ | $O(1)$ front | $O(1)$ front | $O(n)$ |
| Doubly Linked List | $O(n)$ | $O(n)$ | $O(1)$ front/back | $O(1)$ at node | $O(n)$ |
| Stack | $O(n)$ | $O(n)$ | $O(1)$ top | $O(1)$ top | $O(n)$ |
| Circular Queue | $O(n)$ | $O(n)$ | $O(1)$ tail | $O(1)$ head | $O(n)$ |

