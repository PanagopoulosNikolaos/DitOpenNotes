# Assignment 01: Multi-Paradigm Problem Solving in Haskell, Prolog, and Python

This coursework assignment evaluates paradigm comprehension by implementing an algorithmic problem across three contrasting programming paradigms: Pure Functional (Haskell), Declarative Logic (Prolog), and Multi-Paradigm Scripting (Python).

---

## 1. Problem Specification: Route Planning in a Weighted Directed Graph

Consider a directed graph representing a network of interconnected servers with communication latencies (in milliseconds):

```text
Nodes: s1, s2, s3, s4, s5
Edges:
  s1 -> s2 (10 ms)
  s1 -> s3 (25 ms)
  s2 -> s3 (8 ms)
  s2 -> s4 (15 ms)
  s3 -> s4 (12 ms)
  s3 -> s5 (30 ms)
  s4 -> s5 (10 ms)
```

---

## 2. Deliverables across Paradigms

### Part 1: Haskell Functional Implementation (35 Points)
Implement a module `GraphPath.hs`:
1. Define custom data types for `Node` and `Graph`.
2. Implement a pure function `findValidPaths :: Graph -> Node -> Node -> [[Node]]` that returns all acyclic paths between source and destination using recursion and list comprehensions.
3. Implement `shortestPath :: Graph -> Node -> Node -> ([Node], Int)` using higher-order combinators (`foldr` / `minimumBy`) to select the path minimizing total latency.

### Part 2: Prolog Declarative Implementation (35 Points)
Implement a knowledge base `graph_path.pl`:
1. Represent edges as facts: `edge(s1, s2, 10).`
2. Define a recursive predicate `path(Start, End, VisitedNodes, Path, TotalCost)` that unifies with all valid acyclic routes and their costs.
3. Use the built-in predicate `setof/3` or `findall/3` to gather all paths and determine the minimum-cost route.
4. Demonstrate how the Cut operator (`!`) can be applied to stop searching once the first valid route is found.

### Part 3: Python Multi-Paradigm Comparison (20 Points)
Implement `graph_path.py`:
1. Implement a generator function `findAllPaths(graph, start, end, visited=None)` yielding paths on-demand using `yield`.
2. Compute the optimal path using a clean functional expression combining `min()` and a `key` lambda.

### Part 4: Comparative Paradigm Analysis Report (10 Points)
Submit a concise analysis (1–2 pages) comparing:
- State management and mutability across the three implementations.
- Ease of expressing backtracking and search algorithms.
- Type safety and debugging feedback.

---

## 3. Evaluation Rubric

| Criteria | Points |
|---|---|
| Idiomatic Haskell solution (pure recursion, type safety, zero side-effects) | 35 |
| Idiomatic Prolog solution (declarative predicates, backtracking, cycle prevention) | 35 |
| Clean Python solution utilizing generators and functional idioms | 20 |
| Rigorous comparative technical report | 10 |

