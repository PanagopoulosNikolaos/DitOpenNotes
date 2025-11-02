"""
GRAPH ALGORITHMS - Implementation

Advanced graph algorithms for shortest paths, minimum spanning trees, and maximum flow.
These algorithms solve fundamental problems in network optimization and graph theory.

Algorithm Categories:
1. Shortest Path Algorithms:
   - Dijkstra's Algorithm: Single-source shortest path (non-negative weights)
   - Bellman-Ford Algorithm: Single-source shortest path (handles negative weights)
   
2. Minimum Spanning Tree (MST):
   - Prim's Algorithm: Grows MST from starting vertex
   - Kruskal's Algorithm: Sorts edges and adds them greedily
   
3. Maximum Flow:
   - Ford-Fulkerson Algorithm: Finds maximum flow in network
   - Edmonds-Karp Algorithm: BFS-based implementation of Ford-Fulkerson

Common Use Cases:
- Shortest Path: GPS navigation, network routing, game AI
- MST: Network design, clustering, circuit design
- Maximum Flow: Network capacity, bipartite matching, resource allocation
"""

import heapq
from collections import defaultdict, deque

class ShortestPathAlgorithms:
    """Shortest path algorithms for weighted graphs"""
    
    @staticmethod
    def dijkstra(graph, start):
        """
        DIJKSTRA'S ALGORITHM
        
        Finds shortest paths from start vertex to all other vertices.
        Uses greedy approach with priority queue. Works only with non-negative weights.
        
        How it works:
        - Initialize distances: start=0, others=infinity
        - Use min-heap priority queue
        - Extract vertex with minimum distance
        - Update distances to neighbors
        - Repeat until all vertices processed
        
        Time: O((V + E) log V) with binary heap
        Space: O(V)
        Limitation: Cannot handle negative weights
        """
        distances = {vertex: float('infinity') for vertex in graph}
        distances[start] = 0
        previous = {vertex: None for vertex in graph}
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current_vertex = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            for neighbor, weight in graph[current_vertex]:
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances, previous
    
    @staticmethod
    def bellman_ford(graph, start):
        """
        BELLMAN-FORD ALGORITHM
        
        Finds shortest paths from start vertex. Can handle negative weights
        and detects negative cycles.
        
        How it works:
        - Initialize distances: start=0, others=infinity
        - Relax all edges V-1 times
        - Check for negative cycles (one more relaxation)
        - If distance decreases, negative cycle exists
        
        Time: O(V * E)
        Space: O(V)
        Advantage: Handles negative weights, detects negative cycles
        """
        vertices = list(graph.keys())
        distances = {v: float('infinity') for v in vertices}
        distances[start] = 0
        previous = {v: None for v in vertices}
        
        for _ in range(len(vertices) - 1):
            for u in graph:
                for v, weight in graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        previous[v] = u
        
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    raise ValueError("Graph contains negative weight cycle")
        
        return distances, previous
    
    @staticmethod
    def reconstruct_path(previous, start, end):
        """Reconstruct shortest path from previous dictionary"""
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        
        if path[0] == start:
            return path
        return []

class MinimumSpanningTree:
    """Minimum Spanning Tree algorithms"""
    
    @staticmethod
    def prims_algorithm(graph, start):
        """
        PRIM'S ALGORITHM
        
        Finds minimum spanning tree by growing tree from starting vertex.
        Greedily adds minimum weight edge connecting tree to non-tree vertex.
        
        How it works:
        - Start with arbitrary vertex
        - Maintain set of vertices in MST
        - Use priority queue for edges
        - Add minimum weight edge connecting MST to new vertex
        - Repeat until all vertices included
        
        Time: O(E log V) with binary heap
        Space: O(V)
        Result: Set of edges forming MST
        """
        mst_edges = []
        visited = {start}
        edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
        heapq.heapify(edges)
        total_weight = 0
        
        while edges:
            weight, u, v = heapq.heappop(edges)
            
            if v in visited:
                continue
            
            visited.add(v)
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            for neighbor, edge_weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_weight, v, neighbor))
        
        return mst_edges, total_weight
    
    @staticmethod
    def kruskals_algorithm(vertices, edges):
        """
        KRUSKAL'S ALGORITHM
        
        Finds MST by sorting all edges and adding them if they don't create cycle.
        Uses Union-Find (Disjoint Set) data structure for cycle detection.
        
        How it works:
        - Sort all edges by weight
        - Initialize each vertex as separate set
        - For each edge in sorted order:
          - If endpoints in different sets, add edge to MST
          - Union the sets
        - Repeat until V-1 edges added
        
        Time: O(E log E) or O(E log V)
        Space: O(V)
        Result: Set of edges forming MST
        """
        class UnionFind:
            def __init__(self, vertices):
                self.parent = {v: v for v in vertices}
                self.rank = {v: 0 for v in vertices}
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                
                if root_x == root_y:
                    return False
                
                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                elif self.rank[root_x] > self.rank[root_y]:
                    self.parent[root_y] = root_x
                else:
                    self.parent[root_y] = root_x
                    self.rank[root_x] += 1
                
                return True
        
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(vertices)
        mst_edges = []
        total_weight = 0
        
        for u, v, weight in edges:
            if uf.union(u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight
                
                if len(mst_edges) == len(vertices) - 1:
                    break
        
        return mst_edges, total_weight

class MaximumFlow:
    """Maximum flow algorithms for network flow problems"""
    
    @staticmethod
    def ford_fulkerson(graph, source, sink):
        """
        FORD-FULKERSON ALGORITHM
        
        Finds maximum flow in a flow network. Augments flow along paths
        from source to sink until no more augmenting paths exist.
        
        How it works:
        - Initialize flow to 0
        - While augmenting path exists (DFS/BFS):
          - Find path from source to sink
          - Find minimum capacity along path
          - Augment flow by this amount
          - Update residual capacities
        
        Time: O(E * max_flow) with DFS
        Space: O(V²)
        Result: Maximum flow value
        """
        residual_graph = defaultdict(lambda: defaultdict(int))
        for u in graph:
            for v, capacity in graph[u].items():
                residual_graph[u][v] = capacity
        
        def dfs(u, sink, parent, visited):
            visited.add(u)
            if u == sink:
                return True
            
            # Search for a path in the residual graph
            for v, capacity in list(residual_graph[u].items()):
                if v not in visited and capacity > 0:
                    parent[v] = u
                    if dfs(v, sink, parent, visited):
                        return True
            return False

        parent = {}
        max_flow = 0
        
        # Continuously find augmenting paths using DFS in the residual graph
        while dfs(source, sink, parent, set()):
            path_flow = float('infinity')
            s = sink
            
            while s != source:
                path_flow = min(path_flow, residual_graph[parent[s]][s])
                s = parent[s]
            
            max_flow += path_flow
            v = sink
            
            while v != source:
                u = parent[v]
                residual_graph[u][v] -= path_flow
                residual_graph[v][u] += path_flow
                v = parent[v]
            
            # Reset parent for the next path search
            parent = {}
        
        return max_flow
    
    @staticmethod
    def edmonds_karp(graph, source, sink):
        """
        EDMONDS-KARP ALGORITHM
        
        BFS-based implementation of Ford-Fulkerson.
        Uses BFS to find augmenting paths, guaranteeing polynomial time.
        
        How it works:
        - Same as Ford-Fulkerson but uses BFS
        - BFS ensures shortest augmenting path
        - Guaranteed O(VE²) time complexity
        
        Time: O(V * E²)
        Space: O(V²)
        Result: Maximum flow value
        """
        residual_graph = defaultdict(lambda: defaultdict(int))
        for u in graph:
            for v, capacity in graph[u].items():
                residual_graph[u][v] = capacity

        def bfs(s, t, parent):
            visited = {s}
            queue = deque([s])
            parent[s] = -1
            
            while queue:
                u = queue.popleft()
                
                # Search for a path in the residual graph
                for v, capacity in residual_graph[u].items():
                    if v not in visited and capacity > 0:
                        queue.append(v)
                        visited.add(v)
                        parent[v] = u
                        if v == t:
                            return True
            return False
        
        parent = {}
        max_flow = 0
        
        # Continuously find augmenting paths using BFS in the residual graph
        while bfs(source, sink, parent):
            path_flow = float('infinity')
            s = sink
            
            while s != source:
                path_flow = min(path_flow, residual_graph[parent[s]][s])
                s = parent[s]
            
            max_flow += path_flow
            v = sink
            
            while v != source:
                u = parent[v]
                residual_graph[u][v] -= path_flow
                residual_graph[v][u] += path_flow
                v = parent[v]
        
        return max_flow

# Example usage
if __name__ == "__main__":
    print("=== Dijkstra's Algorithm Demo ===")
    graph_dijkstra = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    distances, previous = ShortestPathAlgorithms.dijkstra(graph_dijkstra, 'A')
    print(f"Shortest distances from A: {distances}")
    path = ShortestPathAlgorithms.reconstruct_path(previous, 'A', 'E')
    print(f"Path from A to E: {' -> '.join(path)}")
    
    print("\n=== Prim's Algorithm Demo ===")
    graph_prim = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 1), ('E', 4)],
        'C': [('A', 3), ('B', 1), ('F', 5)],
        'D': [('B', 1), ('E', 1)],
        'E': [('B', 4), ('D', 1), ('F', 1)],
        'F': [('C', 5), ('E', 1)]
    }
    
    mst_edges, total_weight = MinimumSpanningTree.prims_algorithm(graph_prim, 'A')
    print(f"MST edges: {mst_edges}")
    print(f"Total weight: {total_weight}")
    
    print("\n=== Kruskal's Algorithm Demo ===")
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [
        ('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1),
        ('B', 'D', 1), ('B', 'E', 4), ('C', 'F', 5),
        ('D', 'E', 1), ('E', 'F', 1)
    ]
    
    mst_edges, total_weight = MinimumSpanningTree.kruskals_algorithm(vertices, edges)
    print(f"MST edges: {mst_edges}")
    print(f"Total weight: {total_weight}")
    
    print("\n=== Ford-Fulkerson & Edmonds-Karp Algorithm Demo ===")
    graph_flow = {
        'S': {'A': 10, 'B': 5},
        'A': {'B': 15, 'C': 10},
        'B': {'D': 10},
        'C': {'D': 10, 'T': 10},
        'D': {'T': 10},
        'T': {}
    }
    
    max_flow_ff = MaximumFlow.ford_fulkerson(graph_flow, 'S', 'T')
    print(f"Maximum flow (Ford-Fulkerson) from S to T: {max_flow_ff}")
    
    max_flow_ek = MaximumFlow.edmonds_karp(graph_flow, 'S', 'T')
    print(f"Maximum flow (Edmonds-Karp) from S to T: {max_flow_ek}")