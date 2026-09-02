# Εργαστηριακός Οδηγός 2: Αναπαράσταση Γράφων και Αλγόριθμοι Διάσχισης (BFS, DFS) σε Python

## 1. Σκοπός Εργαστηρίου
Υλοποίηση θεμελιωδών δομών αναπαράστασης γράφων (Πίνακας Γειτνίασης, Λίστα Γειτνίασης) και εκτέλεση αλγορίθμων διάσχισης κατά πλάτος (BFS) και κατά βάθος (DFS).

---

## 2. Αναπαράσταση Γράφου με Λίστα Γειτνίασης

```python
from collections import deque
from typing import Dict, List, Set

class Graph:
    """Represents an undirected graph using an adjacency list."""

    def __init__(self) -> None:
        """Initializes an empty graph."""
        self.adj_list: Dict[int, List[int]] = {}

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected edge between vertices u and v.
        Args:
            u (int): First vertex.
            v (int): Second vertex.
        """
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start_node: int) -> List[int]:
        """Performs Breadth-First Search starting from start_node.
        Args:
            start_node (int): The source vertex.
        Returns:
            List[int]: Traversal order.
        """
        visited: Set[int] = {start_node}
        queue: deque[int] = deque([start_node])
        traversal_order: List[int] = []

        while queue:
            node = queue.popleft()
            traversal_order.append(node)

            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    def dfs(self, start_node: int) -> List[int]:
        """Performs Depth-First Search starting from start_node.
        Args:
            start_node (int): The source vertex.
        Returns:
            List[int]: Traversal order.
        """
        visited: Set[int] = set()
        traversal_order: List[int] = []

        def _dfs_util(vertex: int) -> None:
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    _dfs_util(neighbor)

        _dfs_util(start_node)
        return traversal_order
```

---

## 3. Εφαρμογές
- Εύρεση συνεκτικών συνιστωσών (Connected Components).
- Έλεγχος διμερούς γράφου (Bipartite Graph Testing) με χρωματισμό 2 χρωμάτων κατά το BFS.
- Ανίχνευση κύκλων σε κατευθυνόμενους και μη κατευθυνόμενους γράφους.

