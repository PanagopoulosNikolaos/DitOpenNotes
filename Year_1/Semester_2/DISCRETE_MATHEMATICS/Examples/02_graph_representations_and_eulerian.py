"""Demonstrates graph representation, connectivity verification, and Eulerian circuit detection."""

from typing import Dict, List, Set, Tuple


class UndirectedGraph:
    """Represents an undirected finite graph using an adjacency list model."""

    def __init__(self) -> None:
        """Initializes an empty undirected graph."""
        self.adj_list: Dict[str, Set[str]] = {}

    def addVertex(self, vertex: str) -> None:
        """Adds an isolated vertex to the graph if absent.
        
        Args:
            vertex (str): The node identifier.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()

    def addEdge(self, u: str, v: str) -> None:
        """Inserts an undirected edge between two vertices.
        
        Args:
            u (str): First endpoint.
            v (str): Second endpoint.
        """
        self.addVertex(u)
        self.addVertex(v)
        self.adj_list[u].add(v)
        self.adj_list[v].add(u) # Inserts symmetric link for undirected connectivity

    def getDegree(self, vertex: str) -> int:
        """Computes the vertex degree.
        
        Args:
            vertex (str): Node to inspect.
            
        Returns:
            int: Number of incident edges.
        """
        return len(self.adj_list.get(vertex, set()))

    def isConnected(self) -> bool:
        """Determines if all non-isolated vertices belong to a single component.
        
        Returns:
            bool: True if graph is connected over all active vertices.
        """
        active_nodes = [v for v in self.adj_list if len(self.adj_list[v]) > 0]
        if not active_nodes:
            return True

        visited: Set[str] = set()
        stack: List[str] = [active_nodes[0]]
        visited.add(active_nodes[0])

        while stack:
            curr = stack.pop()
            for neighbor in self.adj_list[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return len(visited) == len(active_nodes)

    def checkEulerian(self) -> str:
        """Determines Eulerian properties using Euler's theorem on vertex degrees.
        
        Returns:
            str: 'Eulerian Circuit', 'Eulerian Path', or 'Non-Eulerian'.
        """
        if not self.isConnected():
            return "Non-Eulerian (Disconnected)"

        odd_degrees = sum(1 for v in self.adj_list if self.getDegree(v) % 2 != 0)

        if odd_degrees == 0:
            return "Eulerian Circuit"
        if odd_degrees == 2:
            return "Eulerian Path"
        return "Non-Eulerian"


def main() -> None:
    """Executes graph construction and Euler classification demonstrations."""
    graph = UndirectedGraph()

    # Construct K4 complete graph (4 vertices, all degrees = 3, odd)
    k4_edges: List[Tuple[str, str]] = [
        ("A", "B"), ("A", "C"), ("A", "D"),
        ("B", "C"), ("B", "D"), ("C", "D")
    ]
    for u, v in k4_edges:
        graph.addEdge(u, v)

    print("K4 Graph Analysis:")
    for v in sorted(graph.adj_list.keys()):
        print(f"Vertex {v}: Degree {graph.getDegree(v)}")
    print(f"Eulerian Status: {graph.checkEulerian()}\n")

    # Construct Cycle C4 with diagonals removed (all degrees = 2, even)
    cycle = UndirectedGraph()
    for u, v in [("1", "2"), ("2", "3"), ("3", "4"), ("4", "1")]:
        cycle.addEdge(u, v)

    print("Cycle C4 Graph Analysis:")
    for v in sorted(cycle.adj_list.keys()):
        print(f"Vertex {v}: Degree {cycle.getDegree(v)}")
    print(f"Eulerian Status: {cycle.checkEulerian()}")


if __name__ == "__main__":
    main()

