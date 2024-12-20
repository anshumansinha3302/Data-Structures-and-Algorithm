#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Function to implement Dijkstra's algorithm
void dijkstra(int source, const vector<vector<pair<int, int>>>& graph, vector<int>& distances) {
    // Priority queue to store (distance, vertex) pairs
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    // Initialize distances from source to all vertices as infinite
    distances[source] = 0;
    pq.push({0, source}); // Push the source vertex with distance 0

    while (!pq.empty()) {
        int currentDistance = pq.top().first;
        int currentVertex = pq.top().second;
        pq.pop();

        // If the distance is greater than the recorded distance, skip
        if (currentDistance > distances[currentVertex]) {
            continue;
        }

        // Explore neighbors
        for (const auto& neighbor : graph[currentVertex]) {
            int neighborVertex = neighbor.first;
            int edgeWeight = neighbor.second;

            // Relaxation step
            if (distances[currentVertex] + edgeWeight < distances[neighborVertex]) {
                distances[neighborVertex] = distances[currentVertex] + edgeWeight;
                pq.push({distances[neighborVertex], neighborVertex});
            }
        }
    }
}

int main() {
    int vertices, edges;
    cout << "Enter number of vertices and edges: ";
    cin >> vertices >> edges;

    // Create a graph represented as an adjacency list
    vector<vector<pair<int, int>>> graph(vertices);

    cout << "Enter edges (u v w) where u and v are vertices and w is the weight:\n";
    for (int i = 0; i < edges; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].emplace_back(v, w);
        graph[v].emplace_back(u, w); // For undirected graph
    }

    int source;
    cout << "Enter the source vertex: ";
    cin >> source;

    // Vector to store distances from the source
    vector<int> distances(vertices, INT_MAX);

    // Run Dijkstra's algorithm
    dijkstra(source, graph, distances);

    // Output the distances
    cout << "Shortest distances from source vertex " << source << ":\n";
    for (int i = 0; i < vertices; ++i) {
        if (distances[i] == INT_MAX) {
            cout << "Vertex " << i << ": INF\n";
        } else {
            cout << "Vertex " << i << ": " << distances[i] << "\n";
        }
    }

    return 0;
}
