#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <list>
#include <algorithm>
#include <climits>
#include <memory>

/**
 * @brief GRAPHS - Data Structure Implementation in C++
 * 
 * A graph is a non-linear data structure consisting of vertices (nodes) and edges connecting them.
 * Graphs can represent networks, relationships, paths, and many real-world structures.
 * 
 * Key Characteristics:
 * - Vertices/Nodes: The entities in the graph
 * - Edges: Connections between vertices
 * - Directed vs Undirected: Edges have direction or not
 * - Weighted vs Unweighted: Edges have weights/costs or not
 * - Cyclic vs Acyclic: Contains cycles or not
 * - Connected vs Disconnected: All vertices reachable or not
 * 
 * Graph Representations:
 * 1. Adjacency Matrix: 2D array where matrix[i][j] = weight/1 if edge exists
 *    - Space: O(V²)
 *    - Check edge: O(1)
 *    - Find neighbors: O(V)
 * 
 * 2. Adjacency List: Dictionary/array of lists storing neighbors
 *    - Space: O(V + E)
 *    - Check edge: O(degree of vertex)
 *    - Find neighbors: O(degree of vertex)
 * 
 * Visual Example (Undirected Graph):
 *     A --- B
 *     |     |
 *     C --- D
 * 
 * Adjacency List:
 * A: [B, C]
 * B: [A, D]
 * C: [A, D]
 * D: [B, C]
 * 
 * Graph Traversals:
 * 1. BFS (Breadth-First Search): Level by level using queue
 * 2. DFS (Depth-First Search): Explore as far as possible using stack/recursion
 * 
 * Common Use Cases:
 * - Social networks (friends, followers)
 * - Maps and navigation (roads, routes)
 * - Computer networks (routers, connections)
 * - Web page ranking (PageRank)
 * - Dependency resolution
 * - Recommendation systems
 */

struct Edge {
    int vertex;
    int weight;
    
    Edge(int v, int w) : vertex(v), weight(w) {}
};

class GraphAdjacencyList {
private:
    std::unordered_map<int, std::vector<Edge>> graph;
    bool directed;

public:
    /**
     * @brief Graph implementation using adjacency list (dictionary of lists).
     * Efficient for sparse graphs.
     */
    explicit GraphAdjacencyList(bool directed = false) : directed(directed) {}

    /**
     * @brief Add a vertex to the graph - O(1)
     */
    void addVertex(int vertex) {
        if (graph.find(vertex) == graph.end()) {
            graph[vertex] = std::vector<Edge>();
        }
    }

    /**
     * @brief Add an edge between vertices u and v - O(1)
     */
    void addEdge(int u, int v, int weight = 1) {
        graph[u].emplace_back(v, weight);
        if (!directed) {
            graph[v].emplace_back(u, weight);
        }
    }

    /**
     * @brief Remove edge between u and v - O(degree)
     */
    void removeEdge(int u, int v) {
        graph[u].erase(
            std::remove_if(graph[u].begin(), graph[u].end(),
                [v](const Edge& edge) { return edge.vertex == v; }),
            graph[u].end());
        
        if (!directed) {
            graph[v].erase(
                std::remove_if(graph[v].begin(), graph[v].end(),
                    [u](const Edge& edge) { return edge.vertex == u; }),
                graph[v].end());
        }
    }

    /**
     * @brief Get neighbors of a vertex - O(1)
     */
    const std::vector<Edge>& getNeighbors(int vertex) const {
        return graph.at(vertex);
    }

    /**
     * @brief Check if edge exists - O(degree of u)
     */
    bool hasEdge(int u, int v) const {
        const auto& neighbors = graph.at(u);
        return std::any_of(neighbors.begin(), neighbors.end(),
            [v](const Edge& edge) { return edge.vertex == v; });
    }

    /**
     * @brief Get all vertices - O(1)
     */
    std::vector<int> getVertices() const {
        std::vector<int> vertices;
        for (const auto& pair : graph) {
            vertices.push_back(pair.first);
        }
        return vertices;
    }

    /**
     * @brief Breadth-First Search traversal - O(V + E)
     */
    std::vector<int> bfs(int start) const {
        std::unordered_set<int> visited;
        std::queue<int> q;
        std::vector<int> result;

        visited.insert(start);
        q.push(start);

        while (!q.empty()) {
            int vertex = q.front();
            q.pop();
            result.push_back(vertex);

            for (const Edge& edge : graph.at(vertex)) {
                int neighbor = edge.vertex;
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }

        return result;
    }

    /**
     * @brief Depth-First Search traversal - O(V + E)
     */
    std::vector<int> dfs(int start) const {
        std::unordered_set<int> visited;
        std::vector<int> result;

        dfsRecursive(start, visited, result);
        return result;
    }

private:
    void dfsRecursive(int vertex, std::unordered_set<int>& visited, std::vector<int>& result) const {
        visited.insert(vertex);
        result.push_back(vertex);

        for (const Edge& edge : graph.at(vertex)) {
            int neighbor = edge.vertex;
            if (visited.find(neighbor) == visited.end()) {
                dfsRecursive(neighbor, visited, result);
            }
        }
    }

public:
    /**
     * @brief Iterative DFS using stack - O(V + E)
     */
    std::vector<int> dfsIterative(int start) const {
        std::unordered_set<int> visited;
        std::stack<int> s;
        std::vector<int> result;

        s.push(start);

        while (!s.empty()) {
            int vertex = s.top();
            s.pop();

            if (visited.find(vertex) == visited.end()) {
                visited.insert(vertex);
                result.push_back(vertex);

                // Add neighbors to stack in reverse order to maintain left-to-right traversal
                for (auto it = graph.at(vertex).rbegin(); it != graph.at(vertex).rend(); ++it) {
                    if (visited.find(it->vertex) == visited.end()) {
                        s.push(it->vertex);
                    }
                }
            }
        }

        return result;
    }

    /**
     * @brief Detect cycle in graph - O(V + E)
     */
    bool hasCycle() const {
        std::unordered_set<int> visited;
        std::unordered_set<int> recStack;

        for (const auto& pair : graph) {
            int vertex = pair.first;
            if (visited.find(vertex) == visited.end()) {
                if (hasCycleUtil(vertex, visited, recStack)) {
                    return true;
                }
            }
        }

        return false;
    }

private:
    bool hasCycleUtil(int vertex, std::unordered_set<int>& visited, std::unordered_set<int>& recStack) const {
        visited.insert(vertex);
        recStack.insert(vertex);

        for (const Edge& edge : graph.at(vertex)) {
            int neighbor = edge.vertex;
            if (visited.find(neighbor) == visited.end()) {
                if (hasCycleUtil(neighbor, visited, recStack)) {
                    return true;
                }
            } else if (recStack.find(neighbor) != recStack.end()) {
                return true; // Back edge found, cycle exists
            }
        }

        recStack.erase(vertex);
        return false;
    }

public:
    void print() const {
        for (const auto& pair : graph) {
            std::cout << pair.first << ": ";
            for (size_t i = 0; i < pair.second.size(); ++i) {
                std::cout << pair.second[i].vertex << "(w:" << pair.second[i].weight << ")";
                if (i < pair.second.size() - 1) std::cout << ", ";
            }
            std::cout << std::endl;
        }
    }
};

class GraphAdjacencyMatrix {
private:
    std::vector<std::vector<int>> matrix;
    std::unordered_map<int, int> vertexToIndex;
    std::unordered_map<int, int> indexToVertex;
    size_t numVertices;
    bool directed;
    size_t nextIndex;

public:
    /**
     * @brief Graph implementation using adjacency matrix.
     * Efficient for dense graphs and fast edge lookup.
     */
    explicit GraphAdjacencyMatrix(size_t numVertices, bool directed = false) 
        : numVertices(numVertices), directed(directed), nextIndex(0) {
        matrix.resize(numVertices, std::vector<int>(numVertices, 0));
    }

    void addVertex(int vertex) {
        if (vertexToIndex.find(vertex) == vertexToIndex.end()) {
            if (nextIndex >= numVertices) {
                // Expand matrix if needed
                for (auto& row : matrix) {
                    row.push_back(0);
                }
                matrix.push_back(std::vector<int>(matrix[0].size() + 1, 0));
                ++numVertices;
            }
            vertexToIndex[vertex] = nextIndex;
            indexToVertex[nextIndex] = vertex;
            nextIndex++;
        }
    }

    void addEdge(int u, int v, int weight = 1) {
        if (vertexToIndex.find(u) == vertexToIndex.end()) {
            addVertex(u);
        }
        if (vertexToIndex.find(v) == vertexToIndex.end()) {
            addVertex(v);
        }

        int uIdx = vertexToIndex[u];
        int vIdx = vertexToIndex[v];

        matrix[uIdx][vIdx] = weight;
        if (!directed) {
            matrix[vIdx][uIdx] = weight;
        }
    }

    bool hasEdge(int u, int v) const {
        if (vertexToIndex.find(u) == vertexToIndex.end() || vertexToIndex.find(v) == vertexToIndex.end()) {
            return false;
        }
        int uIdx = vertexToIndex.at(u);
        int vIdx = vertexToIndex.at(v);
        return matrix[uIdx][vIdx] != 0;
    }

    std::vector<Edge> getNeighbors(int vertex) const {
        if (vertexToIndex.find(vertex) == vertexToIndex.end()) {
            return {};
        }

        int idx = vertexToIndex.at(vertex);
        std::vector<Edge> neighbors;
        
        for (size_t i = 0; i < nextIndex; ++i) {
            if (matrix[idx][i] != 0) {
                int neighborVertex = indexToVertex.at(i);
                neighbors.emplace_back(neighborVertex, matrix[idx][i]);
            }
        }

        return neighbors;
    }

    void print() const {
        std::cout << "   ";
        for (size_t i = 0; i < nextIndex; ++i) {
            std::cout << indexToVertex.at(i) << " ";
        }
        std::cout << std::endl;
        
        for (size_t i = 0; i < nextIndex; ++i) {
            std::cout << indexToVertex.at(i) << ": ";
            for (size_t j = 0; j < nextIndex; ++j) {
                std::cout << matrix[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }
};

class WeightedGraph : public GraphAdjacencyList {
public:
    /**
     * @brief Weighted graph with additional algorithms for shortest paths.
     */
    explicit WeightedGraph(bool directed = false) : GraphAdjacencyList(directed) {}

    /**
     * @brief Dijkstra's shortest path algorithm - O((V + E) log V)
     */
    std::unordered_map<int, int> dijkstra(int start) const {
        std::unordered_map<int, int> distances;
        std::unordered_set<int> visited;
        
        // Initialize distances
        auto vertices = getVertices();
        for (int vertex : vertices) {
            distances[vertex] = INT_MAX;
        }
        distances[start] = 0;

        // Priority queue simulation with a vector (for simplicity)
        // In practice, a proper priority queue would be more efficient
        for (size_t i = 0; i < vertices.size(); ++i) {
            // Find vertex with minimum distance that hasn't been visited
            int minDist = INT_MAX;
            int currentVertex = -1;
            
            for (int vertex : vertices) {
                if (visited.find(vertex) == visited.end() && distances[vertex] < minDist) {
                    minDist = distances[vertex];
                    currentVertex = vertex;
                }
            }
            
            if (currentVertex == -1) break; // No more reachable vertices
            
            visited.insert(currentVertex);
            
            // Update distances to neighbors
            for (const Edge& edge : getNeighbors(currentVertex)) {
                int neighbor = edge.vertex;
                int weight = edge.weight;
                int distance = distances[currentVertex] + weight;
                
                if (distance < distances[neighbor]) {
                    distances[neighbor] = distance;
                }
            }
        }

        return distances;
    }

    /**
     * @brief Bellman-Ford shortest path (handles negative weights) - O(V * E)
     */
    std::unordered_map<int, int> bellmanFord(int start) const {
        std::unordered_map<int, int> distances;
        auto vertices = getVertices();
        
        // Initialize distances
        for (int vertex : vertices) {
            distances[vertex] = INT_MAX;
        }
        distances[start] = 0;

        // Relax edges V-1 times
        for (size_t i = 0; i < vertices.size() - 1; ++i) {
            for (int u : vertices) {
                for (const Edge& edge : getNeighbors(u)) {
                    int v = edge.vertex;
                    int weight = edge.weight;
                    if (distances[u] != INT_MAX && distances[u] + weight < distances[v]) {
                        distances[v] = distances[u] + weight;
                    }
                }
            }
        }

        // Check for negative cycles
        for (int u : vertices) {
            for (const Edge& edge : getNeighbors(u)) {
                int v = edge.vertex;
                int weight = edge.weight;
                if (distances[u] != INT_MAX && distances[u] + weight < distances[v]) {
                    throw std::runtime_error("Graph contains negative weight cycle");
                }
            }
        }

        return distances;
    }
};

// Example usage
int main() {
    std::cout << "=== Graph Adjacency List Demo ===" << std::endl;
    GraphAdjacencyList g(false); // undirected graph

    // Add edges (automatically adds vertices)
    g.addEdge(0, 1); // A, B represented as 0, 1
    g.addEdge(0, 2); // A, C represented as 0, 2
    g.addEdge(1, 3); // B, D represented as 1, 3
    g.addEdge(2, 3); // C, D represented as 2, 3
    g.addEdge(3, 4); // D, E represented as 3, 4

    std::cout << "Graph structure:" << std::endl;
    g.print();

    std::cout << "\nNeighbors of 0: ";
    auto neighbors = g.getNeighbors(0);
    for (size_t i = 0; i < neighbors.size(); ++i) {
        std::cout << neighbors[i].vertex;
        if (i < neighbors.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "Edge 0-1 exists: " << (g.hasEdge(0, 1) ? "true" : "false") << std::endl;
    std::cout << "Edge 0-4 exists: " << (g.hasEdge(0, 4) ? "true" : "false") << std::endl;

    std::cout << "\nBFS from 0: ";
    auto bfsResult = g.bfs(0);
    for (size_t i = 0; i < bfsResult.size(); ++i) {
        std::cout << bfsResult[i];
        if (i < bfsResult.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "DFS from 0: ";
    auto dfsResult = g.dfs(0);
    for (size_t i = 0; i < dfsResult.size(); ++i) {
        std::cout << dfsResult[i];
        if (i < dfsResult.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "DFS iterative from 0: ";
    auto dfsIterResult = g.dfsIterative(0);
    for (size_t i = 0; i < dfsIterResult.size(); ++i) {
        std::cout << dfsIterResult[i];
        if (i < dfsIterResult.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    std::cout << "\n=== Directed Graph Cycle Detection ===" << std::endl;
    GraphAdjacencyList dg(true); // directed graph
    dg.addEdge(0, 1); // A -> B
    dg.addEdge(1, 2); // B -> C
    dg.addEdge(2, 0); // C -> A (creates cycle)
    std::cout << "Has cycle: " << (dg.hasCycle() ? "true" : "false") << std::endl;

    std::cout << "\n=== Graph Adjacency Matrix Demo ===" << std::endl;
    GraphAdjacencyMatrix gm(5, false); // undirected graph with 5 initial vertices
    gm.addEdge(0, 1, 1); // A, B
    gm.addEdge(0, 2, 1); // A, C
    gm.addEdge(1, 3, 1); // B, D
    gm.addEdge(2, 3, 1); // C, D

    std::cout << "Adjacency Matrix:" << std::endl;
    gm.print();

    std::cout << "\n=== Weighted Graph & Shortest Path Demo ===" << std::endl;
    WeightedGraph wg(false); // undirected weighted graph
    wg.addEdge(0, 1, 4); // A, B
    wg.addEdge(0, 2, 2); // A, C
    wg.addEdge(1, 2, 1); // B, C
    wg.addEdge(1, 3, 5); // B, D
    wg.addEdge(2, 3, 8); // C, D
    wg.addEdge(2, 4, 10); // C, E
    wg.addEdge(3, 4, 2); // D, E

    std::cout << "Weighted graph:" << std::endl;
    wg.print();

    std::cout << "\nDijkstra's shortest paths from 0:" << std::endl;
    auto distances = wg.dijkstra(0);
    for (const auto& pair : distances) {
        std::cout << "  " << pair.first << ": " << pair.second << std::endl;
    }

    std::cout << "\nBellman-Ford shortest paths from 0:" << std::endl;
    try {
        auto bfDistances = wg.bellmanFord(0);
        for (const auto& pair : bfDistances) {
            std::cout << "  " << pair.first << ": " << pair.second << std::endl;
        }
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    return 0;
}