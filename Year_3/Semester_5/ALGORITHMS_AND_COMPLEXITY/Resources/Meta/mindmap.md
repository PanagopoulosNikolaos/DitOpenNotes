---

## markmap:
colorFreezeLevel: 2
initialExpandLevel: 2
maxWidth: 300

# Algorithms and Complexity (504) Mindmap

* **Algorithms and Complexity (504)**
* **Exam Scope & Syllabus (Goodrich & Tamassia)**


* **Midterm Exam (Proodos) — 7 Chapters**


* `Ch. 1` — Analysis of Algorithms (excludes `1.4.1`)


* `Ch. 5` — Priority Queues & Heaps (excludes `5.5`)


* `Ch. 6` — Hash Tables & Cuckoo Hashing (excludes Linear Probing analysis pp. 202–203, Cuckoo Hashing analysis pp. 208–211, `6.5`)


* `Ch. 7` — Union-Find (excludes `7.3.1`)


* `Ch. 8` — Sorting & Lower Bounds (all sections included)


* `Ch. 10` — Greedy Method (excludes Huffman Coding analysis pp. 294–297)


* `Ch. 11` — Divide & Conquer (all sections included)




* **Final Exam (Teliki Exetasi) — All 13 Chapters (Midterm + 6 Additional)**


* Includes all Midterm chapters with identical exclusions


* `Ch. 12` — Dynamic Programming (excludes `12.4`)


* `Ch. 13` — Graphs, DFS & BFS (excludes `13.4.3`, `13.5`)


* `Ch. 14` — Shortest Paths (excludes `14.5.2`)


* `Ch. 15` — Minimum Spanning Trees (all sections included)


* `Ch. 16` — Maximum Flow (excludes `16.2.2`, `16.3`, `16.4`, `16.5`)


* `Ch. 17` — NP-Completeness (excludes `17.3`, `17.4`, `17.5`)






* **Ch. 1: Analysis of Algorithms [Midterm & Final]**


* **Computation Model & Scalability**


* **RAM Model (Random Access Machine)**


* Single CPU with potentially infinite numbered memory cells


* Constant time `O(1)` access to any memory cell


* Primitive operations — variable assignment, array indexing, method call, method return (`O(1)` each)




* **Scalability** — system capability to handle growing data volume or workload


* **Primitive Step Counting**


* `arrayMax(A, n)` — `7n - 2` worst-case operations, `5n` best-case operations (`O(n)`)






* **Seven Important Growth Functions**


* Constant `1`, Logarithmic `log n`, Linear `n`, N-Log-N `n log n`, Quadratic `n^2`, Cubic `n^3`, Exponential `2^n`


* Input doubling impact — `c n^2` quadruples (`4c n^2`), `c n^3` octuples (`8c n^3`), `c 2^n` squares (`c 2^(2n)`)




* **Asymptotic Notation**


* **Big-Oh `O(g(n))**` — asymptotic upper bound (`f(n) <= c * g(n)` for `n >= n0`, `c > 0`, `n0 >= 1`)


* Simplification rules — drop lower-order terms, drop constant factors, use tightest simplest class




* **Big-Omega `Omega(g(n))**` — asymptotic lower bound (`f(n) >= c * g(n)` for `n >= n0`)


* **Big-Theta `Theta(g(n))**` — asymptotically tight bound (`c' * g(n) <= f(n) <= c'' * g(n)` for `n >= n0`)


* **Pitfalls & Gotchas**
* Using loose bounds (e.g., `2n` as `O(n^2)` instead of `O(n)`)


* `n^2` is NOT `O(n)` because `n <= c` cannot hold for constant `c`






* **Amortized Analysis (Dynamic Arrays)**


* **Incremental Strategy** — grow by constant `c` (`k = n/c` resizes)


* Total time `T(n) = O(n^2)` — amortized `O(n)` per `add`




* **Doubling Strategy** — double capacity on overflow (`k = log2 n` resizes)


* Total time `T(n) = n + 2^(k+1) - 1 = 3n - 1 = O(n)` — amortized `O(1)` per `add`




* **Accounting Method (Cyber-Dollars)**


* Charge `3` cyber-dollars per `add` — `1` for current op, `2` banked on inserted element


* Overflow at `2^i` elements paid by banked credits in cells `2^(i-1)` to `2^i - 1`






* **Syllabus Exclusion** — Section `1.4.1` excluded




* **Ch. 5: Priority Queues & Heaps [Midterm & Final]**


* **Priority Queue ADT**


* Stores `(key, value)` entries ordered by priority


* **Core Operations** — `insert(k, v)`, `removeMin()`, `min()`, `size()`, `isEmpty()`


* **Applications** — stock matching machines (continuous limit order books), auctions, standby flights


* **Sequence Implementations (Sorting Trade-offs)**
* Unsorted sequence -> Selection-Sort (`O(n^2)`)
* Sorted sequence -> Insertion-Sort (`O(n^2)`)




* **Binary Heaps**


* **Structural & Order Properties**


* Heap-Order Property — `key(v) >= key(parent(v))` for every non-root internal node `v`


* Complete Binary Tree — `2^i` nodes at depth `i` (`0..h-1`), internal nodes left-aligned at depth `h-1`


* Height Theorem — heap with `n` keys has height `h <= log n` (`O(log n)`)




* **Array Representation (1-indexed)**
* Left child of rank `i` at `2i`, right child at `2i + 1` (no pointer overhead)
* `add` appends at `n + 1`; `removeMin` swaps root with `n` and shrinks


* **Core Operations & Complexity**
* `insert(k, v)` + `upheap` — swap upward until root or `key(parent) <= k` (`O(log n)`)
* `removeMin()` + `downheap` — replace root with last node, swap downward with smaller child (`O(log n)`)
* `min()`, `size()`, `isEmpty()` — `O(1)`


* **Bottom-Up Heap Construction**
* Merges pairs of heaps across `log n` phases using `downheap`
* Worst-case analysis — each node traversed by at most two right-then-left paths -> `O(n)` total time
* Accelerates Phase 1 of in-place `HeapSort` (Phase 2 remains `O(n log n)`)




* **Syllabus Exclusion** — Section `5.5` excluded




* **Ch. 6: Maps, Hash Tables & Cuckoo Hashing [Midterm & Final]**


* **Map ADT**


* Operations — `get(k)`, `put(k, v)`, `remove(k)`, `size()`, `isEmpty()`




* **Hash Tables**


* **Hash Functions** — hash code (keys -> integers) + compression map (`[0, N - 1]`)
* **Collision Handling Schemes**


* **Separate Chaining** — each bucket stores a secondary list/map
* **Open Addressing — Linear Probing** — probe `(h(k) + j) mod N`


* Expected `O(1)` when load factor `<= 1/2` (Chernoff bound proof excluded from exam)


* Pitfall — primary clustering of contiguous occupied cells




* **Open Addressing — Double Hashing** — secondary hash `d(k)`, probe `(i + j * d(k)) mod N` for `j = 0..N-1`






* **Cuckoo Hashing (Power of Two Choices)**


* **Structure** — two tables `T1`, `T2` of size `N >= 2n` with independent hash functions `h1`, `h2`


* **Placement Invariant** — any key `k` resides exclusively at `T1[h1(k)]` or `T2[h2(k)]`


* **Complexity** — guaranteed `O(1)` worst-case lookup (`get(k)`)


* **Pitfall** — insertion eviction cycles require rehashing with fresh hash functions


* **Syllabus Exclusions** — Linear Probing analysis (pp. 202–203), Cuckoo Hashing analysis (pp. 208–211), Section `6.5`




* **Ch. 7: Union-Find (Disjoint Sets) [Midterm & Final]**


* **Partition ADT Operations**


* `makeSet(u)` — create singleton set `{u}`


* `find(u)` — return canonical representative of set containing `u`


* `union(A, B)` — merge disjoint sets `A` and `B`




* **Tree-Based Implementation**
* Each set is an up-tree; root points to itself as set identifier
* `union` links one root to the other; `find` follows parent pointers to root


* **Optimization Heuristics**
* **Union by Size** — attach smaller tree root under larger tree root
* Each pointer hop doubles subtree size -> tree height `O(log n)`, `n` ops in `O(n log n)`


* **Path Compression** — flatten path during `find` (note: advanced amortized proof in `7.3.1` excluded)




* **Primary Application** — cycle detection and cluster merging in Kruskal's MST algorithm


* **Syllabus Exclusion** — Section `7.3.1` excluded




* **Ch. 8: Sorting & Lower Bounds [Midterm & Final]**


* **Merge-Sort**


* **Paradigm** — Divide (`S` into `S1`, `S2` of size `n/2`), Conquer (recursive sort), Combine (`merge(S1, S2)` in `O(n)`)


* **Complexity** — recursion tree height `O(log n)`, `O(n)` work per level -> `O(n log n)` worst-case


* **Application** — inverted index construction in Internet search engines




* **Quick-Sort (Randomized)**


* **Three-Way Partition** — pick random pivot `x`, split into `L` (`< x`), `E` (`= x`), `G` (`> x`) in `O(n)`


* **In-Place Variant** — `inPlaceQuickSort(S, l, r)` swaps elements via `inPlacePartition(x)` returning `(h, k)` bounds


* **Complexity** — expected tree height `O(log n)`, expected time `O(n log n)`, worst-case `O(n^2)`




* **Comparison-Based Sorting Lower Bound**


* Applies to `bubble-sort`, `selection-sort`, `insertion-sort`, `heap-sort`, `merge-sort`, `quick-sort`


* **Decision Tree Model** — internal nodes represent comparisons (`x_i < x_j?`), leaves represent output permutations


* **Height Lower Bound** — `n!` distinct permutations require at least `n!` leaves -> height `>= log(n!) = Omega(n log n)`




* **Syllabus Scope** — entire Chapter 8 included




* **Ch. 10: Greedy Method [Midterm & Final]**


* **Core Paradigm** — build solution iteratively via locally optimal greedy choices (requires greedy-choice property + optimal substructure)


* **Fractional Knapsack Problem**


* **Greedy Choice** — sort items by highest value density `v_i = b_i / w_i` and take `min(w_i, W - w)`


* **Complexity** — `O(n log n)` sorting + `O(n)` greedy scan -> `O(n log n)`


* **Correctness** — proof by contradiction (exchange argument swapping fractions of items `i` and `j`)


* **Pitfall** — fails for `0-1 Knapsack` where items cannot be split




* **Task Scheduling (Interval Partitioning)**


* **Problem** — schedule all tasks `[s_i, f_i]` minimizing total machines


* **Greedy Choice** — process tasks sorted by earliest start time `s_i`, reuse non-conflicting machine or allocate new one


* **Complexity** — `O(n log n)`


* **Correctness** — if `k` machines used, first task `i` on machine `k` conflicts with `k - 1` active tasks simultaneously




* **Huffman Coding (Data Compression)**
* **Goal** — optimal prefix-free binary code minimizing encoded length of string `X`
* **Greedy Choice** — repeatedly merge two lowest-frequency trees using a min-heap priority queue
* **Complexity** — `O(n + d log d)` (`n` = string length, `d` = distinct characters)
* **Syllabus Exclusion** — Huffman Coding formal analysis (pp. 294–297) excluded






* **Ch. 11: Divide & Conquer [Midterm & Final]**


* **General Pattern** — Divide input into disjoint subsets, Conquer recursively to base case, Combine sub-solutions
* **Recurrence Solving Techniques**


* **Iterative Substitution ("Plug-and-Chug")** — expand `T(n)` repeatedly until base case pattern emerges
* **Recursion Tree** — sum work per depth level (`i = 0..log n`)
* **Guess-and-Test** — hypothesize closed form and prove via mathematical induction
* **Master Theorem** — for `T(n) = a * T(n/b) + f(n)` (`n >= d`)


* **Case 1 (Leaves dominate)** — `f(n) = O(n^(log_b(a) - eps))` -> `T(n) = Theta(n^(log_b(a)))` (e.g., `4T(n/2) + n` -> `O(n^2)`; heap build `2T(n/2) + log n` -> `O(n)`)


* **Case 2 (Balanced)** — `f(n) = Theta(n^(log_b(a)) * log^k(n))` -> `T(n) = Theta(n^(log_b(a)) * log^(k+1)(n))` (e.g., binary search `T(n/2) + 1` -> `O(log n)`)


* **Case 3 (Root dominates)** — `f(n) = Omega(n^(log_b(a) + eps))` and `a * f(n/b) <= delta * f(n)` (`delta < 1`) -> `T(n) = Theta(f(n))`






* **Classic Applications**
* **Fast Integer Multiplication (Karatsuba)** — split `n`-bit integers into high/low halves; algebraically reduce 4 multiplications to 3 (`T(n) = 3T(n/2) + n` -> `O(n^(log_2 3)) ~ O(n^1.585)`)
* **Maxima Set Problem (2D Multicriteria Optimization)** — `T(n) = 2T(n/2) + bn` -> `O(n log n)`


* **Syllabus Scope** — entire Chapter 11 included




* **Ch. 12: Dynamic Programming [Final Only]**


* **Core Principles** — Optimal Substructure, Overlapping Subproblems, Bottom-Up Tabulation (avoids exponential recursion)


* **Matrix Chain Multiplication**


* **Problem** — parenthesize `A_0 * A_1 * ... * A_(n-1)` (`A_i` is `d_i x d_(i+1)`) to minimize scalar ops


* **Failed Approaches** — brute-force enumeration is Catalan `~4^n`; greedy max/min ops both have counterexamples
* **Recurrence** — `N[i, j] = min_{i <= k < j} { N[i, k] + N[k+1, j] + d_i * d_(k+1) * d_(j+1) }`, base `N[i, i] = 0`


* **Complexity** — diagonal bottom-up table fill in `O(n^3)` time, `O(n^2)` space




* **Telescope Scheduling (Weighted Interval Scheduling)**
* **Input** — requests `i` with `(s_i, f_i, b_i)` sorted by finish time `f_i`
* **Predecessor Computation** — `P[i] = pred(i)` via binary search on finish times (`O(n log n)`)
* **DP Choice** — `B[i]` either includes observation `i` (`b_i + B[P[i]]`) or excludes it (`B[i - 1]`)
* **Complexity** — `O(n)` DP fill once sorted and `P` computed (`O(n log n)` overall)


* **Longest Common Subsequence (LCS)**


* **Application** — bioinformatics DNA sequence alignment over `{A, C, G, T}`


* **Brute Force Pitfall** — `2^n` subsequences (exponential)


* **Recurrence** — if `x_i == y_j`: `L[i, j] = L[i-1, j-1] + 1`; else `L[i, j] = max(L[i-1, j], L[i, j-1])`


* **Complexity** — `O(n * m)` time and space; reconstruct subsequence by backtracking table `L`




* **0-1 Knapsack Problem**


* **Constraint** — items indivisible (`x_i in {0, 1}`), maximize benefit `sum(b_i)` subject to `sum(w_i) <= W`


* **Complexity Note** — pseudo-polynomial `O(n * W)` (polynomial in numeric value `W`, exponential in bit-length of `W`)




* **Syllabus Exclusion** — Section `12.4` excluded




* **Ch. 13: Graph Terminology & Traversals [Final Only]**


* **Graph Fundamentals**


* **Definition** — `G = (V, E)` with `n = |V|` vertices and `m = |E|` edges


* **Edge & Graph Types** — directed `(u, v)` vs undirected `{u, v}`, parallel edges, self-loops


* **Terminology** — endpoints, incident edges, adjacent vertices, vertex degree (`sum(deg(v)) = 2m`)


* **Subgraphs** — subgraph `S` (`V_S <= V_G`, `E_S <= E_G`); spanning subgraph (`V_S == V_G`)


* **Applications** — electronic circuits, road/flight networks, computer networks, DB ER models




* **Depth-First Search (DFS)**


* Explores deepest unvisited neighbors recursively; classifies non-tree edges as **back edges** (`(v, w)` where `w` is ancestor of `v`)


* Complexity — `O(n + m)` with adjacency list


* **Breadth-First Search (BFS)**


* Level-by-level exploration (`L_0, L_1, L_2, ...`) in `O(n + m)` time


* Classifies non-tree edges as **cross edges** (`(v, w)` on same or adjacent level)


* **Capabilities** — visits all vertices/edges, tests connectivity, finds connected components, computes spanning forest, finds shortest unweighted path (fewest edges), detects cycles




* **Syllabus Exclusions** — Sections `13.4.3`, `13.5` excluded




* **Ch. 14: Shortest Paths [Final Only]**


* **Weighted Graphs** — edges carry numeric weights (distances, costs)


* **Edge Relaxation** — for edge `e = (u, z)`, update `D[z] = min(D[z], D[u] + weight(e))`
* **Dijkstra's Algorithm (Single-Source, Non-Negative Weights)**
* **Strategy** — greedy cloud expansion; extract min-distance vertex `u` from priority queue, relax outgoing edges
* **Complexity** — `O((n + m) log n)` with adjacency list + binary heap (`O(m log n)` if connected)
* **Pitfall** — fails on negative-weight edges (vertex finalized in cloud can later have shorter path)


* **Bellman-Ford Algorithm (Single-Source, Negative Weights Allowed)**
* **Strategy** — requires directed edges; iteration `i` finds all shortest paths using at most `i` edges
* **Complexity** — `O(n * m)`
* **Negative Cycle Detection** — extra `n`-th relaxation pass detects negative-weight cycles if any `D[z]` decreases


* **DAG Shortest Paths**
* **Strategy** — process vertices in topological order; works with negative weights, no complex data structures
* **Complexity** — `O(n + m)` (faster than Dijkstra)


* **All-Pairs Shortest Paths (Floyd-Warshall DP)**
* **Recurrence** — `D^k[i, j] = min(D^(k-1)[i, j], D^(k-1)[i, k] + D^(k-1)[k, j])` using intermediate vertices `1..k`
* **Complexity** — `O(n^3)` (vs `O(n * m log n)` for `n` Dijkstra calls or `O(n^2 * m)` for `n` Bellman-Ford calls)


* **Syllabus Exclusion** — Section `14.5.2` excluded




* **Ch. 15: Minimum Spanning Trees (MST) [Final Only]**


* **Fundamental MST Properties**
* **Cycle Property** — heaviest edge on any cycle `C` cannot belong to an MST (proof by contradiction)
* **Partition (Cut) Property** — minimum-weight edge `e` crossing any vertex partition `(U, V)` belongs to some MST


* **Prim-Jarnik Algorithm**
* **Strategy** — grow single cloud from arbitrary start vertex `s`; `d(v)` tracks min edge weight to cloud
* **Complexity** — `O((n + m) log n)` with binary heap + adjacency list (`O(m log n)` if connected)


* **Kruskal's Algorithm**


* **Strategy** — maintain forest of clusters; priority queue extracts edges in ascending weight; accept edge if endpoints in different clusters


* **Data Structures** — min-heap PQ (`O(m log n)`) + Union-Find partition (`makeSet`, `find`, `union` in `O(n log n)`)


* **Complexity** — `O((n + m) log n)` (faster if edges pre-sorted -> `O(1)` `removeMin`)


* **Boruvka's Algorithm**
* **Strategy** — grow multiple clusters in parallel; each phase picks min outgoing edge per component, halving component count
* **Complexity** — `O(m log n)` (`O(log n)` phases)


* **Syllabus Scope** — entire Chapter 15 included




* **Ch. 16: Maximum Flow [Final Only]**


* **Ford-Fulkerson Algorithm**


* **Initialization** — `f(e) = 0` for all edges `e`
* **Iterative Augmentation** — find augmenting path `pi` from `s` to `t` via DFS/BFS where residual capacity `Delta_f(u, v) > 0`; augment flow by `Delta_f(pi)`
* **Max-Flow Min-Cut Theorem** — terminates when no augmenting path exists; max flow value equals min cut capacity
* **Complexity & Pitfall** — `O(|f*| * (n + m))` worst-case (`O(n + m)` per augmentation, up to `|f*|` augmentations; alternating paths can cause `|f*|` steps)




* **Applications (Reductions to Max-Flow)**


* **Maximum Bipartite Matching** — bipartite graph `(X, Y)` reduced to unit-capacity flow network `H`; edge `e` in matching `M` iff `f(e) = 1`; runs in `O(n * m)`


* **Baseball Elimination** — determine if team `i` (with `w_i` wins, `g_i` games left) can finish first given remaining league schedule




* **Syllabus Exclusions** — Sections `16.2.2`, `16.3`, `16.4`, `16.5` excluded




* **Ch. 17: NP-Completeness [Final Only]**


* **Formal Framework**


* **Input Size `n**` — binary encoding bit-length (distinguishes true polynomial from pseudo-polynomial like 0-1 Knapsack)
* **Decision Problems & Languages** — binary output (`yes`/`no`); language `L` is set of strings accepted by algorithm `A`


* **Complexity Classes**


* **`P`** — languages decided by deterministic polynomial-time algorithms (`p(n)`)
* **`NP` (Two Equivalent Definitions)**


* Languages accepted by non-deterministic polynomial-time algorithms (`choose(b)`)
* Languages verified in polynomial time by deterministic verifier `B(x, y)` given certificate `y`




* **Open Question** — `P <= NP`; `P == NP?` remains open (conjectured `P != NP`)


* **Reductions & NP-Completeness**


* **Polynomial-Time Reduction** — transform input `x` of `M` into `x'` of `L` in poly-time such that `x in M` iff `x' in L`


* **`NP-hard`** — every problem in `NP` reduces to `L` in polynomial time


* **`NP-complete`** — `L in NP` AND `L` is `NP-hard` (hardest problems in `NP`; poly-time solution for one implies `P = NP`)




* **Cook-Levin Theorem**


* **`CIRCUIT-SAT` is `NP-complete**` — deciding if a Boolean circuit (`AND`, `OR`, `NOT` gates) has an input assignment outputting `1`


* **Proof Sketch** — `CIRCUIT-SAT in NP` (guess inputs + gate outputs, verify gates); `NP-hard` by simulating `p(n)` steps of any `NP` verifier `D` with workspace `W` as a polynomial-sized circuit `O(p(n)^3)`




* **Syllabus Exclusions** — Sections `17.3`, `17.4`, `17.5` excluded







---

*Notes*

* **Midterm vs. Final Strategy:** The Midterm (`Ch. 1, 5, 6, 7, 8, 10, 11`) focuses on asymptotic/amortized analysis, core data structures (heaps, hash tables, union-find), sorting, greedy proofs, and divide-and-conquer recurrences (`Master Theorem`). The Final is cumulative and adds Dynamic Programming (`Ch. 12`), Graph Algorithms (`Ch. 13–16`), and Complexity Theory (`Ch. 17`).


* **High-Yield Exam Exclusions:** Do not spend study time on Chernoff-bound Linear Probing proofs (pp. 202–203), Cuckoo Hashing analysis (pp. 208–211), Huffman formal proof (pp. 294–297), or NP-completeness reductions beyond Cook-Levin (`17.3–17.5`).


* **Algorithmic Paradigm Selection:** Use **Greedy** when a local choice is provably safe via exchange argument (`Fractional Knapsack`, `Dijkstra`, `MST`); use **Dynamic Programming** when greedy fails and subproblems overlap (`0-1 Knapsack`, `Matrix Chain`, `LCS`, `Telescope Scheduling`, `Floyd-Warshall`).