# Tutorial 02: Graph Isomorphism, Invariants, and Graph Traversals

## Context and Grounding
This tutorial provides practical analytical tools to prove or disprove graph isomorphism using graph invariants, and details the step-by-step execution of Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms. It directly grounds `Lectures/6 Graph Theory.pdf` and `Resources/Notes/7_Graph Theory & Trees.md`.

---

## 1. Graph Isomorphism and Invariants

### 1.1 Formal Definition
Two simple graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are **isomorphic** ($G_1 \cong G_2$) if there exists a bijection $f: V_1 \to V_2$ such that:
$$\forall u, v \in V_1, \quad \{u, v\} \in E_1 \iff \{f(u), f(v)\} \in E_2$$

### 1.2 Preservation of Graph Invariants
If $G_1 \cong G_2$, both graphs MUST share identical graph invariants:
1. Number of vertices: $|V_1| = |V_2|$.
2. Number of edges: $|E_1| = |E_2|$.
3. Degree sequence (sorted list of vertex degrees).
4. Subgraph structures (number of triangles $C_3$, squares $C_4$).
5. Connectedness and number of connected components.
6. Chromatic number $\chi(G)$ and planarity.

*Disproof Strategy:* If two graphs differ in any invariant, they are not isomorphic.
*Proof Strategy:* If all invariants match, construct an explicit bijection table $f(v)$ and verify adjacency preservation across the entire adjacency matrix.

---

## 2. Graph Traversal Algorithms

### 2.1 Breadth-First Search (BFS)
Traverses a graph level-by-level using a FIFO queue.
* Time Complexity: $O(|V| + |E|)$.
* Applications: Shortest path in unweighted graphs, bipartite graph verification.

```python
from collections import deque

def bfs(graph, start_vertex):
    visited = set([start_vertex])
    queue = deque([start_vertex])
    traversal_order = []

    while queue:
        vertex = queue.popleft()
        traversal_order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order
```

### 2.2 Depth-First Search (DFS)
Explores along each branch as deep as possible before backtracking using a LIFO stack or recursion.
* Time Complexity: $O(|V| + |E|)$.
* Applications: Topological sorting, cycle detection, connected components, finding bridges/articulation points.

```python
def dfs(graph, start_vertex, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(start_vertex)
    traversal_order.append(start_vertex)

    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal_order)

    return traversal_order
```

