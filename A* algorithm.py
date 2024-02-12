# f(n) = g(n) + h(n)
# h(n) = heuristic function --> estimate cost of path from one node to another
# g(n) = cost of path from one node to another

# h(n) of S = 5
# h(n) of A = 3
# h(n) of B = 4
# h(n) of C = 2
# h(n) of D = 6
# h(n) of G = 0
    
# g(n) of S to A = 1
# g(n) of S to G = 10
# g(n) of A to B = 2
# g(n) of A to C = 1
# g(n) of B to D = 5
# g(n) of C to D = 3
# g(n) of C to G = 4
# g(n) of D to G = 2

def astar(graph, src, dest):
    open_set = [(0, src)]  # Tuple: (f(n), node)
    
    # Dictionary to store the cost to reach each node from the start node
    g_score = {node: float('inf') for node in graph}
    g_score[src] = 0
    
    # Heuristic function values for each node
    heuristic = {
        'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0
    }
    
    # Cost values for each edge
    cost = {
        ('S', 'A'): 1, ('S', 'G'): 10,
        ('A', 'B'): 2, ('A', 'C'): 1,
        ('B', 'D'): 5,
        ('C', 'D'): 3, ('C', 'G'): 4,
        ('D', 'G'): 2
    }
    
    while open_set:
        open_set.sort()  # Sort based on f(n)
        current_node = open_set.pop(0)[1]  # Get the node with the lowest f(n)
        
        if current_node == dest:
            return g_score[dest]  # Return the cost to reach the destination
        
        # Iterate through neighbors of the current node
        for neighbor in graph[current_node]:
            tentative_g_score = g_score[current_node] + cost.get((current_node, neighbor), float('inf'))
            
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_set.append((f_score, neighbor))  # Add neighbor to open set with updated f(n)
    
    return float('inf')  # If no path found, return infinity or handle as needed

# Example graph representation (adjust as per your graph structure)
graph = {
    'S': ['A', 'G'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'G'],
    'D': ['G'],
    'G': []
}

# Example usage
source_node = 'S'
goal_node = 'G'
result = astar(graph, source_node, goal_node)
print("Cost to reach destination:", result)

    
    
   
