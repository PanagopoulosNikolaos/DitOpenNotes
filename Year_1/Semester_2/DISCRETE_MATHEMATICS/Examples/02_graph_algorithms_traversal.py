"""Demonstrates graph data structures and traversal algorithms.

Implements adjacency list representations, Breadth-First Search (BFS),
Depth-First Search (DFS), and connected components detection.
"""

from collections import deque
from typing import Dict, List, Set


class Graph:
    """Represents an undirected graph using adjacency lists."""

    def __init__(self) -> None:
        """Initializes an empty graph."""
        self.adj_list: Dict[str, List[str]] = {}

    def add_edge(self, u: str, v: str) -> None:
        """Adds an undirected edge between vertices u and v.

        Args:
            u (str): First vertex identifier.
            v (str): Second vertex identifier.
        """
        self.adj_list.setdefault(u, []).append(v)
        self.adj_list.setdefault(v, []).append(u)

    def bfs(self, start_node: str) -> List[str]:
        """Performs Breadth-First Search from start_node.

        Args:
            start_node (str): Starting vertex identifier.

        Returns:
            List[str]: Order of vertices visited during BFS traversal.
        """
        if start_node not in self.adj_list:
            return []
        visited: Set[str] = {start_node}
        queue: deque = deque([start_node])
        order: List[str] = []

        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start_node: str) -> List[str]:
        """Performs Depth-First Search from start_node.

        Args:
            start_node (str): Starting vertex identifier.

        Returns:
            List[str]: Order of vertices visited during DFS traversal.
        """
        visited: Set[str] = set()
        order: List[str] = []

        def _dfs_helper(node: str) -> None:
            visited.add(node)
            order.append(node)
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    _dfs_helper(neighbor)

        if start_node in self.adj_list:
            _dfs_helper(start_node)

        return order

    def is_connected(self) -> bool:
        """Determines whether the graph is connected.

        Returns:
            bool: True if every vertex is reachable from any other vertex, False otherwise.
        """
        if not self.adj_list:
            return True
        start_node = next(iter(self.adj_list))
        visited = set(self.bfs(start_node))
        return len(visited) == len(self.adj_list)


def main() -> None:
    """Executes sample graph traversals and tests connectivity."""
    g = Graph()
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    for u, v in edges:
        g.add_edge(u, v)

    print("Graph Adjacency List:")
    for vertex, neighbors in sorted(g.adj_list.items()):
        print(f"  {vertex}: {', '.join(neighbors)}")

    print(f"\nBFS Traversal from 'A': {g.bfs('A')}")
    print(f"DFS Traversal from 'A': {g.dfs('A')}")
    print(f"Is graph connected? {g.is_connected()}")


if __name__ == "__main__":
    main()
