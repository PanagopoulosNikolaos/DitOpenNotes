# Lecture 03: Graph Theory, Trees, and Network Connectivity

## Context and Grounding
This lecture note introduces graph definitions, traversability criteria (Eulerian and Hamiltonian paths), planar graphs, and tree structures. It directly grounds `Resources/Notes/7_Graph Theory & Trees.md` and `Lectures/6 Graph Theory.pdf`.

---

## 1. Graph Fundamentals

A graph $G = (V, E)$ consists of a non-empty set of vertices $V$ and a set of edges $E \subseteq V \times V$.

### 1.1 Degrees and the Handshaking Lemma
For an undirected graph, the degree $\deg(v)$ of vertex $v$ is the number of edges incident to it (self-loops count twice).

$$\sum_{v \in V} \deg(v) = 2|E|$$

**Corollary**: An undirected graph has an even number of vertices of odd degree.

### 1.2 Special Graph Classes
* **Complete Graph ($K_n$)**: Simple graph with an edge between every pair of distinct vertices ($|E| = \binom{n}{2} = \frac{n(n-1)}{2}$).
* **Bipartite Graph ($K_{m,n}$)**: Vertex set partitioned into $V_1, V_2$ such that all edges connect $V_1$ to $V_2$. (A graph is bipartite iff it contains no odd-length cycles).

---

## 2. Paths, Circuits, and Traversals

### 2.1 Eulerian Paths and Circuits
* **Euler Path**: Visits every **edge** in $G$ exactly once.
* **Euler Circuit**: Euler path that starts and terminates at the same vertex.
* **Euler's Theorem**:
  * A connected multigraph has an Euler circuit iff **every vertex has an even degree**.
  * A connected multigraph has an Euler path iff **exactly zero or two vertices have an odd degree**.

### 2.2 Hamiltonian Cycles
* **Hamiltonian Cycle**: A closed loop that visits every **vertex** in $G$ exactly once (except starting/ending vertex).
* Determining Hamiltonian cycles is NP-complete.
* **Dirac's Theorem**: If $G$ is a simple graph with $n \ge 3$ vertices and $\deg(v) \ge n/2$ for all $v \in V$, then $G$ contains a Hamiltonian cycle.

---

## 3. Trees and Spanning Trees

A **tree** is a connected undirected graph with no simple circuits.

### 3.1 Fundamental Tree Equivalences
For a graph $T = (V, E)$ with $|V| = n$, the following are equivalent:
1. $T$ is a tree.
2. $T$ contains no cycles and $|E| = n - 1$.
3. $T$ is connected and $|E| = n - 1$.
4. Between any two vertices in $T$, there exists a unique simple path.

### 3.2 Spanning Trees
A spanning tree of a connected graph $G$ is a subgraph that is a tree and includes every vertex of $G$.
* Found via Breadth-First Search (BFS) or Depth-First Search (DFS).
* Minimum Spanning Trees (MST) on weighted graphs are computed via Kruskal's or Prim's algorithms in $O(|E| \log |V|)$ time.

---

## 4. Planar Graphs and Euler's Formula

A graph is **planar** if it can be drawn in the Euclidean plane such that no two edges cross.

### 4.1 Euler's Polyhedral Formula
For any connected planar graph with $V$ vertices, $E$ edges, and $R$ regions (faces):
$$V - E + R = 2$$

### 4.2 Planarity Bounds and Kuratowski's Theorem
* For a simple connected planar graph with $V \ge 3$:
  $$E \le 3V - 6$$
* If the graph contains no triangles (cycles of length 3):
  $$E \le 2V - 4$$
* **Kuratowski's Theorem**: A graph is planar if and only if it does not contain a subgraph homeomorphic to (or contractible to) $K_5$ or $K_{3,3}$.

