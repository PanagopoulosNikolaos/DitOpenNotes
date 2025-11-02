"""
GRAPHS - Data Structure Implementation

A graph is a non-linear data structure consisting of vertices (nodes) and edges connecting them.
Graphs can represent networks, relationships, paths, and many real-world structures.

Key Characteristics:
- Vertices/Nodes: The entities in the graph
- Edges: Connections between vertices
- Directed vs Undirected: Edges have direction or not
- Weighted vs Unweighted: Edges have weights/costs or not
- Cyclic vs Acyclic: Contains cycles or not
- Connected vs Disconnected: All vertices reachable or not

Graph Representations:
1. Adjacency Matrix: 2D array where matrix[i][j] = weight/1 if edge exists
   - Space: O(V²)
   - Check edge: O(1)
   - Find neighbors: O(V)

2. Adjacency List: Dictionary/array of lists storing neighbors
   - Space: O(V + E)
   - Check edge: O(degree of vertex)
   - Find neighbors: O(degree of vertex)

Visual Example (Undirected Graph):
    A --- B
    |     |
    C --- D

Adjacency List:
A: [B, C]
B: [A, D]
C: [A, D]
D: [B, C]

Graph Traversals:
1. BFS (Breadth-First Search): Level by level using queue
2. DFS (Depth-First Search): Explore as far as possible using stack/recursion

Common Use Cases:
- Social networks (friends, followers)
- Maps and navigation (roads, routes)
- Computer networks (routers, connections)
- Web page ranking (PageRank)
- Dependency resolution
- Recommendation systems
"""

from collections import deque, defaultdict

class GraphAdjacencyList:
    """
    Graph implementation using adjacency list (dictionary of lists).
    Efficient for sparse graphs.
    """
    
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph - O(1)"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v, weight=1):
        """Add an edge between vertices u and v - O(1)"""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def remove_edge(self, u, v):
        """Remove edge between u and v - O(degree)"""
        self.graph[u] = [(vertex, weight) for vertex, weight in self.graph[u] if vertex != v]
        if not self.directed:
            self.graph[v] = [(vertex, weight) for vertex, weight in self.graph[v] if vertex != u]
    
    def get_neighbors(self, vertex):
        """Get neighbors of a vertex - O(1)"""
        return self.graph[vertex]
    
    def has_edge(self, u, v):
        """Check if edge exists - O(degree of u)"""
        for vertex, _ in self.graph[u]:
            if vertex == v:
                return True
        return False
    
    def get_vertices(self):
        """Get all vertices - O(1)"""
        return list(self.graph.keys())
    
    def bfs(self, start):
        """Breadth-First Search traversal - O(V + E)"""
        visited = set()
        queue = deque([start])
        result = []
        
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Depth-First Search traversal - O(V + E)"""
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def dfs_iterative(self, start):
        """Iterative DFS using stack - O(V + E)"""
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                for neighbor, _ in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def has_cycle(self):
        """Detect cycle in graph - O(V + E)"""
        visited = set()
        rec_stack = set()
        
        def has_cycle_util(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if has_cycle_util(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if has_cycle_util(vertex):
                    return True
        
        return False
    
    def __str__(self):
        result = []
        for vertex in self.graph:
            neighbors = [f"{v}(w:{w})" for v, w in self.graph[vertex]]
            result.append(f"{vertex}: {', '.join(neighbors)}")
        return "\n".join(result)

class GraphAdjacencyMatrix:
    """
    Graph implementation using adjacency matrix.
    Efficient for dense graphs and fast edge lookup.
    """
    
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertex_map = {}
        self.reverse_map = {}
        self.next_index = 0
    
    def add_vertex(self, vertex):
        """Add a vertex - O(1)"""
        if vertex not in self.vertex_map:
            self.vertex_map[vertex] = self.next_index
            self.reverse_map[self.next_index] = vertex
            self.next_index += 1
    
    def add_edge(self, u, v, weight=1):
        """Add an edge - O(1)"""
        if u not in self.vertex_map:
            self.add_vertex(u)
        if v not in self.vertex_map:
            self.add_vertex(v)
        
        u_idx = self.vertex_map[u]
        v_idx = self.vertex_map[v]
        
        self.matrix[u_idx][v_idx] = weight
        if not self.directed:
            self.matrix[v_idx][u_idx] = weight
    
    def has_edge(self, u, v):
        """Check if edge exists - O(1)"""
        if u not in self.vertex_map or v not in self.vertex_map:
            return False
        u_idx = self.vertex_map[u]
        v_idx = self.vertex_map[v]
        return self.matrix[u_idx][v_idx] != 0
    
    def get_neighbors(self, vertex):
        """Get neighbors of vertex - O(V)"""
        if vertex not in self.vertex_map:
            return []
        
        idx = self.vertex_map[vertex]
        neighbors = []
        
        for i in range(self.num_vertices):
            if self.matrix[idx][i] != 0:
                neighbors.append((self.reverse_map[i], self.matrix[idx][i]))
        
        return neighbors
    
    def __str__(self):
        result = ["   " + " ".join(f"{self.reverse_map.get(i, ' '):3}" for i in range(self.next_index))]
        for i in range(self.next_index):
            row = f"{self.reverse_map[i]:3}" + " ".join(f"{self.matrix[i][j]:3}" for j in range(self.next_index))
            result.append(row)
        return "\n".join(result)

class WeightedGraph(GraphAdjacencyList):
    """
    Weighted graph with additional algorithms for shortest paths.
    """
    
    def dijkstra(self, start):
        """Dijkstra's shortest path algorithm - O((V + E) log V)"""
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        visited = set()
        
        import heapq
        pq = [(0, start)]
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances
    
    def bellman_ford(self, start):
        """Bellman-Ford shortest path (handles negative weights) - O(V * E)"""
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        
        # Relax edges V-1 times
        for _ in range(len(self.graph) - 1):
            for u in self.graph:
                for v, weight in self.graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
        
        # Check for negative cycles
        for u in self.graph:
            for v, weight in self.graph[u]:
                if distances[u] + weight < distances[v]:
                    raise ValueError("Graph contains negative weight cycle")
        
        return distances

# Example usage
if __name__ == "__main__":
    print("=== Graph Adjacency List Demo ===")
    g = GraphAdjacencyList(directed=False)
    
    # Add edges (automatically adds vertices)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')
    
    print("Graph structure:")
    print(g)
    
    print(f"\nNeighbors of A: {g.get_neighbors('A')}")
    print(f"Edge A-B exists: {g.has_edge('A', 'B')}")
    print(f"Edge A-E exists: {g.has_edge('A', 'E')}")
    
    print(f"\nBFS from A: {g.bfs('A')}")
    print(f"DFS from A: {g.dfs('A')}")
    print(f"DFS iterative from A: {g.dfs_iterative('A')}")
    
    print("\n=== Directed Graph Cycle Detection ===")
    dg = GraphAdjacencyList(directed=True)
    dg.add_edge('A', 'B')
    dg.add_edge('B', 'C')
    dg.add_edge('C', 'A')  # Creates cycle
    print(f"Has cycle: {dg.has_cycle()}")
    
    print("\n=== Graph Adjacency Matrix Demo ===")
    gm = GraphAdjacencyMatrix(5, directed=False)
    gm.add_edge('A', 'B', 1)
    gm.add_edge('A', 'C', 1)
    gm.add_edge('B', 'D', 1)
    gm.add_edge('C', 'D', 1)
    
    print("Adjacency Matrix:")
    print(gm)
    
    print("\n=== Weighted Graph & Shortest Path Demo ===")
    wg = WeightedGraph(directed=False)
    wg.add_edge('A', 'B', 4)
    wg.add_edge('A', 'C', 2)
    wg.add_edge('B', 'C', 1)
    wg.add_edge('B', 'D', 5)
    wg.add_edge('C', 'D', 8)
    wg.add_edge('C', 'E', 10)
    wg.add_edge('D', 'E', 2)
    
    print("Weighted graph:")
    print(wg)
    
    print("\nDijkstra's shortest paths from A:")
    distances = wg.dijkstra('A')
    for vertex, distance in sorted(distances.items()):
        print(f"  {vertex}: {distance}")
    
    print("\nBellman-Ford shortest paths from A:")
    distances = wg.bellman_ford('A')
    for vertex, distance in sorted(distances.items()):
        print(f"  {vertex}: {distance}")
