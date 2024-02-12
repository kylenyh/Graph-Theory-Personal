
# distance of each node excluding source vertex, is originally at 0
# weight between nodes have already a set value from the start (+/-)
# let u = start vertex, v = end vertex 
# u --> v = directed edge from vertex u to v
# w(u,v) = weight of edge from u to v
# d(u,v) = distance from u to v
# d(u,v) = w(u,v) + d(u,v-1)
# d(u,v) = w(u,v) + min(d(u,v-1), d(u,v-2), d(u,v-3),...)

# originally (distance)
# dist_A = 0
# dist_B = 'inf'
# dist_C = 'inf'
# dist_D = 'inf'
# dist_E = 'inf'
# dist_F = 'inf'

# originally (weight)
# dist_AB = 5
# dist_BC = 1
# dist_BD = 2
# dist_DF = 2
# dist_FE = -3
# dist_DE = -1
# dist_CE = 1

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

def bellman_ford(graph, start):
    # Initialize distances
    distances = {vertex: float('inf') for vertex in graph.vertices}
    distances[start] = 0

    # Relax edges repeatedly
    for i in range(len(graph.vertices) - 1):
        for u, v, weight in graph.graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative cycles
    for u, v, weight in graph.graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Graph contains negative cycle. Cannot calculate shortest distances.")
            return None

    return distances

# Create a graph
vertices = {'A', 'B', 'C', 'D', 'E', 'F'}
graph = Graph(vertices)
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 1)
graph.add_edge('B', 'D', 2)
graph.add_edge('D', 'F', 2)
graph.add_edge('F', 'E', -3)
graph.add_edge('D', 'E', -1)
graph.add_edge('C', 'E', 1)

# Run Bellman-Ford algorithm
start_vertex = 'A'
result = bellman_ford(graph, start_vertex)

# Print the result
if result:
    for vertex, distance in result.items():
        print(f"Distance from {start_vertex} to {vertex}: {distance}")
