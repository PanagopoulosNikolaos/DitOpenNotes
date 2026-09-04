"""Computes shortest paths in weighted undirected graphs using Dijkstra's algorithm."""

import heapq
from typing import Dict, List, Tuple


class WeightedGraph:
    """Represents a weighted undirected graph with shortest-path solving capability."""

    def __init__(self) -> None:
        """Initializes empty adjacency list dictionary."""
        self.adj_list: Dict[str, List[Tuple[str, float]]] = {}

    def addEdge(self, u: str, v: str, weight: float) -> None:
        """Inserts an undirected weighted edge into the graph.

        Args:
            u (str): First endpoint vertex.
            v (str): Second endpoint vertex.
            weight (float): Positive edge weight.
        """
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight)) # Enforces symmetric edge for undirected topology

    def findShortestPaths(self, source_vertex: str) -> Dict[str, float]:
        """Calculates single-source shortest path distances using Dijkstra's algorithm.

        Args:
            source_vertex (str): Origin vertex label.

        Returns:
            Dict[str, float]: Mapping from each vertex to minimum path cost from source.
        """
        distances: Dict[str, float] = {node: float("inf") for node in self.adj_list}
        distances[source_vertex] = 0.0

        priority_queue: List[Tuple[float, str]] = [(0.0, source_vertex)]

        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)

            if current_dist > distances[current_node]:
                continue # Skips stale queue entries

            for neighbor_node, edge_weight in self.adj_list[current_node]:
                tentative_dist = current_dist + edge_weight
                if tentative_dist < distances[neighbor_node]:
                    distances[neighbor_node] = tentative_dist
                    heapq.heappush(priority_queue, (tentative_dist, neighbor_node)) # Updates shortest boundary

        return distances


def main() -> None:
    """Executes demonstration of Dijkstra shortest path calculation on a sample graph."""
    graph = WeightedGraph()
    graph.addEdge("A", "B", 4.0)
    graph.addEdge("A", "C", 2.0)
    graph.addEdge("B", "C", 1.0)
    graph.addEdge("B", "D", 5.0)
    graph.addEdge("C", "D", 8.0)
    graph.addEdge("C", "E", 10.0)
    graph.addEdge("D", "E", 2.0)

    shortest = graph.findShortestPaths("A")
    print("=== Dijkstra Shortest Paths from Source 'A' ===")
    for node, cost in sorted(shortest.items()):
        print(f"Distance to {node}: {cost:.1f}")


if __name__ == "__main__":
    main()

