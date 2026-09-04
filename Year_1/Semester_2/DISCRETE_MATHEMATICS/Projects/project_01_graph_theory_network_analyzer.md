# Project 01: Discrete Graph Theory and Network Connectivity Analyzer

## Project Overview
Design and implement a standalone graph analysis and topological evaluation engine in Python or C. The system models complex networks (e.g., social networks, computer network topologies, road systems), analyzes fundamental discrete graph properties (degrees, connectedness, Eulerian circuits, bipartite verification), tests planarity heuristics, and generates minimum spanning trees.

---

## 1. Functional Specifications

### 1.1 Input Representation
The engine must parse network topologies from adjacency lists and edge-list files:
```text
# node1 node2 weight
RouterA RouterB 4
RouterA RouterC 2
RouterB RouterD 5
RouterC RouterD 1
```

### 1.2 Core Analytical Modules
1. **Degree Analysis & Handshaking Verification**:
   * Computes degree sequences, identifies regular graphs, and formally verifies $\sum \deg(v) = 2|E|$.
2. **Connectivity & Component Decomposition**:
   * Uses BFS/DFS to find all connected components, bridges (cut-edges), and articulation points (cut-vertices).
3. **Eulerian and Hamiltonian Path Evaluator**:
   * Evaluates vertex degree parity to classify graphs as Eulerian Circuit, Eulerian Path, or Non-Eulerian.
   * If Eulerian, reconstructs the exact traversal circuit using Fleury's Algorithm or Hierholzer's Algorithm in $O(|E|)$ time.
4. **Bipartite Verification & 2-Coloring**:
   * Tests if the graph is 2-colorable (bipartite) via BFS odd-cycle detection.
5. **Minimum Spanning Tree (MST)**:
   * Implements Kruskal's algorithm using a Disjoint-Set Union (DSU / Union-Find) data structure with path compression.
6. **Planarity Bounds Checker**:
   * Checks planarity conditions ($E \le 3V - 6$ and $E \le 2V - 4$ for triangle-free graphs).

---

## 2. Architecture and Code Organization
* `network_analyzer/`
  * `graph.py` / `graph.c`: Adjacency representation and graph construction.
  * `algorithms.py` / `algorithms.c`: BFS, DFS, Hierholzer's, Kruskal's DSU algorithms.
  * `properties.py` / `properties.c`: Invariant checking, degree distribution, Handshaking verification.
  * `cli.py` / `main.c`: Command-line driver accepting input files and execution parameters.
  * `tests/`: Automated unit tests verifying synthetic graphs (complete graphs $K_n$, bipartite $K_{m,n}$, trees, cycles).

---

## 3. Deliverables and Evaluation
| Deliverable | Criteria | Points |
|---|---|---|
| Adjacency Model & I/O | Robust parser and flexible graph representation | 20 |
| Traversal & Connectivity | Accurate component detection, bridges, and cycle identification | 25 |
| Eulerian Reconstruction | Correct implementation of Hierholzer's circuit algorithm | 20 |
| MST via Union-Find | Optimal Kruskal's algorithm with path compression | 20 |
| Testing & Code Quality | Comprehensive test suite, zero memory/type errors, Google-style docstrings | 15 |
| **Total** | | **100** |

