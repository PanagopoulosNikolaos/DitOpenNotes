# Lecture 04: Graph Representations, Traversals, and Classical Algorithms

This lecture covers graph theory data structures, standard representations (adjacency matrices vs. adjacency lists), traversal strategies (BFS, DFS), topological sorting on Directed Acyclic Graphs (DAGs), shortest path algorithms (Dijkstra), and Minimum Spanning Trees (Prim, Kruskal).

---

## 1. Graph Definitions and Representations

A graph $G = (V, E)$ consists of a set of vertices $V$ and a set of edges $E \subseteq V \times V$.
Let $|V| = n$ and $|E| = m$.

### 1.1 Adjacency Matrix vs. Adjacency List

| Feature | Adjacency Matrix | Adjacency List |
|---|---|---|
| Memory Space | $\Theta(V^2)$ | $\Theta(V + E)$ |
| Edge Existence Check $(u, v)$ | $O(1)$ | $O(\deg(u))$ |
| Iterate Outgoing Edges of $u$ | $\Theta(V)$ | $\Theta(\deg(u))$ |
| Best Application | Dense graphs ($E \approx V^2$) | Sparse graphs ($E \ll V^2$) |

```cpp
// Adjacency List representation using standard C++ collections
using Graph = std::vector<std::vector<std::pair<int, int>>>; // u -> [(v, weight), ...]
```

---

## 2. Graph Traversals

### 2.1 Breadth-First Search (BFS)
Explores vertices in increasing order of distance from the source using a FIFO queue.
- Computes shortest paths in unweighted graphs.
- Time Complexity: $\Theta(V + E)$.
- Space Complexity: $\Theta(V)$ (for `visited` array and queue).

### 2.2 Depth-First Search (DFS)
Explores deeply along each branch before backtracking, implemented via recursion or an explicit LIFO stack.
- Classifies edges into Tree, Back, Forward, and Cross edges.
- Detects cycles: In a directed graph, a cycle exists if and only if DFS encounters a **Back Edge** to an active ancestor.
- Time Complexity: $\Theta(V + E)$.

---

## 3. Topological Sorting

A linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge $(u, v)$, vertex $u$ appears before vertex $v$.

### 3.1 Kahn's Algorithm (In-Degree Elimination)
1. Compute in-degree $\text{in}[u]$ for all $u \in V$.
2. Enqueue all vertices with $\text{in}[u] = 0$.
3. While queue is not empty:
   - Dequeue $u$, append to topological order.
   - For each neighbor $v$ of $u$: decrement $\text{in}[v]$. If $\text{in}[v] == 0$, enqueue $v$.
4. If processed vertex count $< |V|$, the graph contains a cycle.
- Time Complexity: $O(V + E)$.

---

## 4. Single-Source Shortest Paths: Dijkstra's Algorithm

Finds minimum edge-weight path from source $s$ to all other vertices in graphs with non-negative edge weights ($w(e) \ge 0$).

```cpp
std::vector<int> dijkstra(int src, int n, const Graph& adj) {
    std::vector<int> dist(n, std::numeric_limits<int>::max());
    // Min-priority queue storing pairs: (distance, vertex)
    std::priority_queue<std::pair<int, int>, 
                        std::vector<std::pair<int, int>>, 
                        std::greater<>> pq;

    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue; // Stale queue entry

        for (const auto& [v, weight] : adj[u]) {
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
```

- **Time Complexity:** $O((V + E) \log V)$ using a binary min-heap.

---

## 5. Minimum Spanning Trees (MST)

For a connected, undirected, weighted graph, an MST connects all $|V|$ vertices with $|V| - 1$ edges minimizing the total edge weight sum.

### 5.1 Kruskal's Algorithm
- Sort all edges in non-decreasing order of weight ($O(E \log E)$).
- Iterate through sorted edges, adding edge $(u, v)$ to MST if $u$ and $v$ belong to disjoint components.
- Uses **Disjoint Set Union (DSU)** with union-by-rank and path compression ($O(\alpha(V))$ per operation).
- Total Time: $O(E \log E) = O(E \log V)$.

### 5.2 Prim's Algorithm
- Grows a single tree starting from an arbitrary root vertex.
- Always selects the minimum-weight edge connecting the tree to a non-tree vertex using a min-heap.
- Total Time: $O((V + E) \log V)$.

---

## 6. Summary

- Adjacency lists minimize memory overhead for sparse graphs.
- BFS and DFS provide foundational $O(V + E)$ graph traversals for reachability, cycle detection, and topological ordering.
- Dijkstra solves non-negative shortest path problems greedily with a priority queue.
- MSTs minimize interconnection costs via greedy edge selection (Kruskal and Prim).

