# vertice of A from start = inf
# vertice of B from start = inf
# vertica of C from start = inf
# vertcie of D from start = inf
# vertice of E from start = inf
    
# start node = A
# end node = E

# distance of start vertex/start node = 0

def dijkstra(graph, src, dest):
    open_set = [(0, src)]
    
    unvis_nodes = ['A', 'B', 'C', 'D', 'E']
    vis_nodes = []
    
    dist = {}  # Dictionary to store distances between nodes
    
    # Initialize distances with infinity for all nodes
    for node in unvis_nodes:
        dist[(src, node)] = float('inf')
    
    # Define the actual distances between connected nodes
    actual_dist = {
        ('A', 'D'): 1, ('A', 'B'): 6,
        ('B', 'E'): 2, ('B', 'C'): 5,
        ('D', 'B'): 2, ('D', 'E'): 1,
        ('E', 'C'): 5
    }
    
    while open_set:
        open_set.sort()  # Sort based on distance
        current_node = open_set.pop(0)[1]  # Get the node with the lowest distance
        
        if current_node == dest:
            return dist[(src, dest)]  # Return the shortest distance to the destination
        
        vis_nodes.append(current_node)
        unvis_nodes.remove(current_node)
        
        # Iterate through neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor in unvis_nodes:
                tentative_distance = actual_dist.get((current_node, neighbor), float('inf')) + dist[(src, current_node)]
                
                if tentative_distance < dist[(src, neighbor)]:
                    dist[(src, neighbor)] = tentative_distance
                    open_set.append((tentative_distance, neighbor))  # Add neighbor to open set with updated distance
    
    return float('inf')  # If no path found, return infinity or handle as needed

# Example graph representation (adjust as per your graph structure)
graph = {
    'A': ['D', 'B'],
    'B': ['E', 'C'],
    'C': [],
    'D': ['B', 'E'],
    'E': ['C']
}

# Example usage
source_node = 'A'
goal_node = 'C'
result = dijkstra(graph, source_node, goal_node)
print("Shortest distance to reach destination:", result)
