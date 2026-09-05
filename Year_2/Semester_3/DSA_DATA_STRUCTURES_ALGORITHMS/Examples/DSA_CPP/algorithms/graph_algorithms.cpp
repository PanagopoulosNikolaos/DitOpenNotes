#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <climits>
#include <functional>
#include <algorithm>

/**
 * @brief Graph algorithms for shortest paths, minimum spanning trees, and maximum flow.
 * 
 * Advanced graph algorithms for shortest paths, minimum spanning trees, and maximum flow.
 * These algorithms solve fundamental problems in network optimization and graph theory.
 * 
 * Algorithm Categories:
 * 1. Shortest Path Algorithms:
 *    - Dijkstra's Algorithm: Single-source shortest path (non-negative weights)
 *    - Bellman-Ford Algorithm: Single-source shortest path (handles negative weights)
 *    
 * 2. Minimum Spanning Tree (MST):
 *    - Prim's Algorithm: Grows MST from starting vertex
 *    - Kruskal's Algorithm: Sorts edges and adds them greedily
 *    
 * 3. Maximum Flow:
 *    - Ford-Fulkerson Algorithm: Finds maximum flow in network
 *    - Edmonds-Karp Algorithm: BFS-based implementation of Ford-Fulkerson
 * 
 * Common Use Cases:
 * - Shortest Path: GPS navigation, network routing, game AI
 * - MST: Network design, clustering, circuit design
 * - Maximum Flow: Network capacity, bipartite matching, resource allocation
 */

struct GraphAlgoEdge {
    int to;
    int weight;
    
    GraphAlgoEdge(int t, int w) : to(t), weight(w) {}
};

using Graph = std::unordered_map<int, std::vector<GraphAlgoEdge>>;

class ShortestPathAlgorithms {
public:
    /**
     * @brief DIJKSTRA'S ALGORITHM
     * 
     * Finds shortest paths from start vertex to all other vertices.
     * Uses greedy approach with priority queue. Works only with non-negative weights.
     * 
     * How it works:
     * - Initialize distances: start=0, others=infinity
     * - Use min-heap priority queue
     * - Extract vertex with minimum distance
     * - Update distances to neighbors
     * - Repeat until all vertices processed
     * 
     * Time: O((V + E) log V) with binary heap
     * Space: O(V)
     * Limitation: Cannot handle negative weights
     */
    static std::pair<std::unordered_map<int, int>, std::unordered_map<int, int>> 
    dijkstra(const Graph& graph, int start) {
        std::unordered_map<int, int> distances;
        std::unordered_map<int, int> previous;
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
        std::unordered_set<int> visited;

        // Initialize distances
        for (const auto& node : graph) {
            distances[node.first] = INT_MAX;
            previous[node.first] = -1;
        }
        distances[start] = 0;
        pq.push({0, start});

        while (!pq.empty()) {
            int currentDist = pq.top().first;
            int currentVertex = pq.top().second;
            pq.pop();

            if (visited.count(currentVertex)) {
                continue;
            }

            visited.insert(currentVertex);

            for (const GraphAlgoEdge& edge : graph.at(currentVertex)) {
                int neighbor = edge.to;
                int weight = edge.weight;
                int distance = currentDist + weight;

                if (distance < distances[neighbor]) {
                    distances[neighbor] = distance;
                    previous[neighbor] = currentVertex;
                    pq.push({distance, neighbor});
                }
            }
        }

        return {distances, previous};
    }

    /**
     * @brief BELLMAN-FORD ALGORITHM
     * 
     * Finds shortest paths from start vertex. Can handle negative weights
     * and detects negative cycles.
     * 
     * How it works:
     * - Initialize distances: start=0, others=infinity
     * - Relax all edges V-1 times
     * - Check for negative cycles (one more relaxation)
     * - If distance decreases, negative cycle exists
     * 
     * Time: O(V * E)
     * Space: O(V)
     * Advantage: Handles negative weights, detects negative cycles
     */
    static std::pair<std::unordered_map<int, int>, std::unordered_map<int, int>> 
    bellmanFord(const Graph& graph, int start) {
        std::vector<int> vertices;
        for (const auto& node : graph) {
            vertices.push_back(node.first);
        }

        std::unordered_map<int, int> distances;
        std::unordered_map<int, int> previous;

        for (int vertex : vertices) {
            distances[vertex] = INT_MAX;
            previous[vertex] = -1;
        }
        distances[start] = 0;

        // Relax edges V-1 times
        for (size_t i = 0; i < vertices.size() - 1; ++i) {
            for (const auto& node : graph) {
                int u = node.first;
                for (const GraphAlgoEdge& edge : node.second) {
                    int v = edge.to;
                    int weight = edge.weight;
                    
                    if (distances[u] != INT_MAX && distances[u] + weight < distances[v]) {
                        distances[v] = distances[u] + weight;
                        previous[v] = u;
                    }
                }
            }
        }

        // Check for negative cycles
        for (const auto& node : graph) {
            int u = node.first;
            for (const GraphAlgoEdge& edge : node.second) {
                int v = edge.to;
                int weight = edge.weight;
                
                if (distances[u] != INT_MAX && distances[u] + weight < distances[v]) {
                    throw std::runtime_error("Graph contains negative weight cycle");
                }
            }
        }

        return {distances, previous};
    }

    /**
     * @brief Reconstruct shortest path from previous dictionary
     */
    static std::vector<int> reconstructPath(const std::unordered_map<int, int>& previous, int start, int end) {
        std::vector<int> path;
        int current = end;

        while (current != -1) {
            path.push_back(current);
            current = previous.at(current);
        }

        std::reverse(path.begin(), path.end());

        if (path[0] == start) {
            return path;
        }
        return {};
    }
};

class MinimumSpanningTree {
private:
    // Union-Find (Disjoint Set) data structure
    struct UnionFind {
        std::unordered_map<int, int> parent;
        std::unordered_map<int, int> rank;

        UnionFind(const std::vector<int>& vertices) {
            for (int v : vertices) {
                parent[v] = v;
                rank[v] = 0;
            }
        }

        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);  // Path compression
            }
            return parent[x];
        }

        bool unite(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);

            if (rootX == rootY) {
                return false;  // Would create a cycle
            }

            // Union by rank
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }

            return true;
        }
    };

public:
    /**
     * @brief PRIM'S ALGORITHM
     * 
     * Finds minimum spanning tree by growing tree from starting vertex.
     * Greedily adds minimum weight edge connecting tree to non-tree vertex.
     * 
     * How it works:
     * - Start with arbitrary vertex
     * - Maintain set of vertices in MST
     * - Use priority queue for edges
     * - Add minimum weight edge connecting MST to new vertex
     * - Repeat until all vertices included
     * 
     * Time: O(E log V) with binary heap
     * Space: O(V)
     * Result: Set of edges forming MST
     */
    static std::pair<std::vector<std::tuple<int, int, int>>, int> 
    primsAlgorithm(const Graph& graph, int start) {
        std::vector<std::tuple<int, int, int>> mstEdges;
        std::unordered_set<int> visited;
        std::priority_queue<std::tuple<int, int, int>, std::vector<std::tuple<int, int, int>>, 
                          std::greater<std::tuple<int, int, int>>> edges;
        int totalWeight = 0;

        visited.insert(start);

        // Add all edges from start vertex to priority queue
        for (const GraphAlgoEdge& edge : graph.at(start)) {
            edges.push(std::make_tuple(edge.weight, start, edge.to));
        }

        while (!edges.empty() && visited.size() < graph.size()) {
            int weight, u, v;
            std::tie(weight, u, v) = edges.top();
            edges.pop();

            if (visited.count(v)) {
                continue;
            }

            visited.insert(v);
            mstEdges.push_back(std::make_tuple(u, v, weight));
            totalWeight += weight;

            // Add edges from newly added vertex to unvisited vertices
            for (const GraphAlgoEdge& edge : graph.at(v)) {
                if (!visited.count(edge.to)) {
                    edges.push(std::make_tuple(edge.weight, v, edge.to));
                }
            }
        }

        return {mstEdges, totalWeight};
    }

    /**
     * @brief KRUSKAL'S ALGORITHM
     * 
     * Finds MST by sorting all edges and adding them if they don't create cycle.
     * Uses Union-Find (Disjoint Set) data structure for cycle detection.
     * 
     * How it works:
     * - Sort all edges by weight
     * - Initialize each vertex as separate set
     * - For each edge in sorted order:
     *   - If endpoints in different sets, add edge to MST
     *   - Union the sets
     * - Repeat until V-1 edges added
     * 
     * Time: O(E log E) or O(E log V)
     * Space: O(V)
     * Result: Set of edges forming MST
     */
    static std::pair<std::vector<std::tuple<int, int, int>>, int> 
    kruskalsAlgorithm(const std::vector<int>& vertices, std::vector<std::tuple<int, int, int>>& edges) {
        // Sort edges by weight
        std::sort(edges.begin(), edges.end(), [](const std::tuple<int, int, int>& a, const std::tuple<int, int, int>& b) {
            return std::get<2>(a) < std::get<2>(b);
        });

        UnionFind uf(vertices);
        std::vector<std::tuple<int, int, int>> mstEdges;
        int totalWeight = 0;

        for (const auto& edge : edges) {
            int u, v, weight;
            std::tie(u, v, weight) = edge;

            if (uf.unite(u, v)) {
                mstEdges.push_back(edge);
                totalWeight += weight;

                if (mstEdges.size() == vertices.size() - 1) {
                    break;
                }
            }
        }

        return {mstEdges, totalWeight};
    }
};

class MaximumFlow {
private:
    // Helper function for BFS in Edmonds-Karp
    static bool bfs(const std::unordered_map<int, std::unordered_map<int, int>>& residualGraph,
                   int source, int sink, std::unordered_map<int, int>& parent) {
        std::unordered_set<int> visited;
        std::queue<int> q;

        q.push(source);
        visited.insert(source);
        parent[source] = -1;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (const auto& edge : residualGraph.at(u)) {
                int v = edge.first;
                int capacity = edge.second;

                if (visited.count(v) == 0 && capacity > 0) {
                    q.push(v);
                    visited.insert(v);
                    parent[v] = u;

                    if (v == sink) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

public:
    /**
     * @brief FORD-FULKERSON ALGORITHM
     *
     * Finds maximum flow in a flow network. Augments flow along paths
     * from source to sink until no more augmenting paths exist.
     *
     * How it works:
     * - Initialize flow to 0
     * - While augmenting path exists (DFS/BFS):
     *   - Find path from source to sink
     *   - Find minimum capacity along path
     *   - Augment flow by this amount
     *   - Update residual capacities
     *
     * Time: O(E * max_flow) with DFS
     * Space: O(V²)
     * Result: Maximum flow value
     */
    static int fordFulkerson(const std::unordered_map<int, std::unordered_map<int, int>>& graph, int source, int sink) {
        // Create residual graph
        std::unordered_map<int, std::unordered_map<int, int>> residualGraph = graph;

        // Add reverse edges with 0 capacity
        for (const auto& node : graph) {
            for (const auto& edge : node.second) {
                if (residualGraph[edge.first][node.first] == 0) {
                    residualGraph[edge.first][node.first] = 0;
                }
            }
        }

        int maxFlow = 0;
        std::unordered_map<int, int> parent;

        // Continuously find augmenting paths using DFS in the residual graph
        while (dfs(residualGraph, source, sink, parent)) {
            int pathFlow = INT_MAX;
            int s = sink;

            while (s != source) {
                pathFlow = std::min(pathFlow, residualGraph[parent[s]][s]);
                s = parent[s];
            }

            maxFlow += pathFlow;
            int v = sink;

            while (v != source) {
                int u = parent[v];
                residualGraph[u][v] -= pathFlow;
                residualGraph[v][u] += pathFlow;
                v = parent[v];
            }

            // Clear parent for the next path search
            parent.clear();
        }

        return maxFlow;
    }

private:
    static bool dfs(const std::unordered_map<int, std::unordered_map<int, int>>& residualGraph,
                   int source, int sink, std::unordered_map<int, int>& parent) {
        if (source == sink) {
            return true;
        }

        for (const auto& edge : residualGraph.at(source)) {
            int v = edge.first;
            int capacity = edge.second;

            if (parent.count(v) == 0 && capacity > 0) {
                parent[v] = source;
                if (dfs(residualGraph, v, sink, parent)) {
                    return true;
                }
            }
        }

        return false;
    }

public:
    /**
     * @brief EDMONDS-KARP ALGORITHM
     *
     * BFS-based implementation of Ford-Fulkerson.
     * Uses BFS to find augmenting paths, guaranteeing polynomial time.
     *
     * How it works:
     * - Same as Ford-Fulkerson but uses BFS
     * - BFS ensures shortest augmenting path
     * - Guaranteed O(VE²) time complexity
     *
     * Time: O(V * E²)
     * Space: O(V²)
     * Result: Maximum flow value
     */
    static int edmondsKarp(const std::unordered_map<int, std::unordered_map<int, int>>& graph, int source, int sink) {
        // Create residual graph
        std::unordered_map<int, std::unordered_map<int, int>> residualGraph = graph;

        // Add reverse edges with 0 capacity
        for (const auto& node : graph) {
            for (const auto& edge : node.second) {
                if (residualGraph[edge.first][node.first] == 0) {
                    residualGraph[edge.first][node.first] = 0;
                }
            }
        }

        int maxFlow = 0;
        std::unordered_map<int, int> parent;

        while (bfs(residualGraph, source, sink, parent)) {
            int pathFlow = INT_MAX;
            int s = sink;

            while (s != source) {
                pathFlow = std::min(pathFlow, residualGraph[parent[s]][s]);
                s = parent[s];
            }

            maxFlow += pathFlow;
            int v = sink;

            while (v != source) {
                int u = parent[v];
                residualGraph[u][v] -= pathFlow;
                residualGraph[v][u] += pathFlow;
                v = parent[v];
            }

            parent.clear();
        }

        return maxFlow;
    }
};

// Example usage
#ifndef SKIP_STANDALONE_MAIN
int main() {
    std::cout << "=== Dijkstra's Algorithm Demo ===" << std::endl;
    Graph graphDijkstra;
    graphDijkstra[0] = {{1, 4}, {2, 2}};
    graphDijkstra[1] = {{0, 4}, {2, 1}, {3, 5}};
    graphDijkstra[2] = {{0, 2}, {1, 1}, {3, 8}, {4, 10}};
    graphDijkstra[3] = {{1, 5}, {2, 8}, {4, 2}};
    graphDijkstra[4] = {{2, 10}, {3, 2}};

    auto [distances, previous] = ShortestPathAlgorithms::dijkstra(graphDijkstra, 0);
    std::cout << "Shortest distances from 0: ";
    for (const auto& dist : distances) {
        std::cout << "[" << dist.first << ": " << dist.second << "] ";
    }
    std::cout << std::endl;
    
    std::vector<int> path = ShortestPathAlgorithms::reconstructPath(previous, 0, 4);
    std::cout << "Path from 0 to 4: ";
    for (size_t i = 0; i < path.size(); ++i) {
        std::cout << path[i];
        if (i < path.size() - 1) std::cout << " -> ";
    }
    std::cout << std::endl;

    std::cout << "\n=== Prim's Algorithm Demo ===" << std::endl;
    Graph graphPrim;
    graphPrim[0] = {{1, 2}, {2, 3}};
    graphPrim[1] = {{0, 2}, {2, 1}, {3, 1}, {4, 4}};
    graphPrim[2] = {{0, 3}, {1, 1}, {5, 5}};
    graphPrim[3] = {{1, 1}, {4, 1}};
    graphPrim[4] = {{1, 4}, {3, 1}, {5, 1}};
    graphPrim[5] = {{2, 5}, {4, 1}};

    auto [mstEdges, totalWeight] = MinimumSpanningTree::primsAlgorithm(graphPrim, 0);
    std::cout << "MST edges: ";
    for (const auto& edge : mstEdges) {
        int u, v, w;
        std::tie(u, v, w) = edge;
        std::cout << "(" << u << ", " << v << ", " << w << ") ";
    }
    std::cout << std::endl;
    std::cout << "Total weight: " << totalWeight << std::endl;

    std::cout << "\n=== Kruskal's Algorithm Demo ===" << std::endl;
    std::vector<int> vertices = {0, 1, 2, 3, 4, 5};
    std::vector<std::tuple<int, int, int>> edges = {
        {0, 1, 2}, {0, 2, 3}, {1, 2, 1},
        {1, 3, 1}, {1, 4, 4}, {2, 5, 5},
        {3, 4, 1}, {4, 5, 1}
    };

    auto [mstEdges2, totalWeight2] = MinimumSpanningTree::kruskalsAlgorithm(vertices, edges);
    std::cout << "MST edges: ";
    for (const auto& edge : mstEdges2) {
        int u, v, w;
        std::tie(u, v, w) = edge;
        std::cout << "(" << u << ", " << v << ", " << w << ") ";
    }
    std::cout << std::endl;
    std::cout << "Total weight: " << totalWeight2 << std::endl;

    std::cout << "\n=== Ford-Fulkerson & Edmonds-Karp Algorithm Demo ===" << std::endl;
    std::unordered_map<int, std::unordered_map<int, int>> graphFlow;
    graphFlow[0] = {{1, 10}, {2, 5}};   // S: 0
    graphFlow[1] = {{2, 15}, {3, 10}};  // A: 1
    graphFlow[2] = {{4, 10}};           // B: 2
    graphFlow[3] = {{4, 10}, {5, 10}}; // C: 3
    graphFlow[4] = {{5, 10}};           // D: 4
    graphFlow[5] = {};                  // T: 5

    try {
        int maxFlowFF = MaximumFlow::fordFulkerson(graphFlow, 0, 5);
        std::cout << "Maximum flow (Ford-Fulkerson) from S(0) to T(5): " << maxFlowFF << std::endl;

        int maxFlowEK = MaximumFlow::edmondsKarp(graphFlow, 0, 5);
        std::cout << "Maximum flow (Edmonds-Karp) from S(0) to T(5): " << maxFlowEK << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    return 0;
}
#endif // SKIP_STANDALONE_MAIN
