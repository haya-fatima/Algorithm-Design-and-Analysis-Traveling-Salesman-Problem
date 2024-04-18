import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def dp_tsp(tsp_data):
    num_nodes = len(tsp_data)
    
    # Initialize memoization table
    memo = {}
    
    # Function to compute the shortest tour recursively
    def tsp_helper(curr_node, visited):
        if (curr_node, visited) in memo:
            return memo[(curr_node, visited)]
        
        # Base case: If all nodes have been visited, return the distance to the start node
        if visited == (1 << num_nodes) - 1:
            return euclidean_distance(tsp_data[curr_node], tsp_data[1]), [1]
        
        min_distance = float('inf')
        optimal_tour = None
        for next_node in range(2, num_nodes + 1):
            if (visited >> (next_node - 1)) & 1 == 0:  # Check if next_node is not visited
                distance_to_next = euclidean_distance(tsp_data[curr_node], tsp_data[next_node])
                new_visited = visited | (1 << (next_node - 1))
                distance, tour = tsp_helper(next_node, new_visited)
                
                if distance + distance_to_next < min_distance:
                    min_distance = distance + distance_to_next
                    optimal_tour = [next_node] + tour
        
        memo[(curr_node, visited)] = min_distance, optimal_tour
        return min_distance, optimal_tour
    # Start the recursion from the first node
    distance, tour = tsp_helper(1, 1)
    
    # Add the start node to the tour and return
    optimal_tour = [1] + tour
    return optimal_tour, distance