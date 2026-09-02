# Εργαστηριακός Οδηγός 2: Διάσχιση Γράφων και Αλγόριθμος Dijkstra σε Python

## 1. Σκοπός Εργαστηρίου
Σκοπός είναι η υλοποίηση γράφων με λίστες γειτνίασης (adjacency lists), η εκτέλεση διασχίσεων BFS και DFS, και η εφαρμογή του αλγορίθμου Dijkstra με χρήση της βιβλιοθήκης `heapq` (Min-Priority Queue).

---

## 2. Πλήρης Υλοποίηση σε Python

```python
import heapq
from collections import deque
from typing import Dict, List, Tuple

class Graph:
    def __init__(self):
        self.adj_list: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, u: str, v: str, weight: int = 1, directed: bool = False):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        self.adj_list[u].append((v, weight))
        if not directed:
            self.adj_list[v].append((u, weight))

    def bfs(self, start_node: str) -> List[str]:
        visited = set([start_node])
        queue = deque([start_node])
        traversal_order = []

        while queue:
            node = queue.popleft()
            traversal_order.append(node)

            for neighbor, _ in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    def dijkstra(self, source: str) -> Tuple[Dict[str, float], Dict[str, str]]:
        distances: Dict[str, float] = {node: float('inf') for node in self.adj_list}
        previous: Dict[str, str] = {node: None for node in self.adj_list}
        distances[source] = 0.0

        min_heap: List[Tuple[float, str]] = [(0.0, source)]

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            if current_dist > distances[u]:
                continue

            for v, weight in self.adj_list[u]:
                distance_via_u = current_dist + weight
                if distance_via_u < distances[v]:
                    distances[v] = distance_via_u
                    previous[v] = u
                    heapq.heappush(min_heap, (distance_via_u, v))

        return distances, previous

    def reconstruct_path(self, previous: Dict[str, str], target: str) -> List[str]:
        path = []
        curr = target
        while curr is not None:
            path.append(curr)
            curr = previous[curr]
        path.reverse()
        return path

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)

    print("BFS Diasxisi apo ton A:", g.bfs('A'))
    
    distances, previous = g.dijkstra('A')
    print("\nElaxistes Apostaseis apo ton A:")
    for node, dist in distances.items():
        path = g.reconstruct_path(previous, node)
        print(f"  Pros {node}: Kostos = {dist}, Monopati = {' -> '.join(path)}")
```

---

## 3. Εκτέλεση και Ανάλυση
Εκτελέστε το script:
```bash
python3 graph_algorithms.py
```
Ο αλγόριθμος Dijkstra επιτυγχάνει χρονική πολυπλοκότητα $O((V + E) \log V)$ χάρη στην ενσωματωμένη Min-Heap της Python.

