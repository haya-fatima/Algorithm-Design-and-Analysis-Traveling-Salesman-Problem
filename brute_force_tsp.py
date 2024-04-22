import math
import itertools

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def total_distance(tour, tsp_data):
    """
    Calculate the total distance of a tour.
    """
    dist = 0
    for i in range(len(tour) - 1):
        dist += euclidean_distance(tsp_data[tour[i]], tsp_data[tour[i+1]])
    dist += euclidean_distance(tsp_data[tour[-1]], tsp_data[tour[0]])  # Complete the tour
    return dist

def bf_tsp(tsp_data):
    cities = list(tsp_data.keys())
    min_distance = float('inf')
    min_path = None

    # Generate all permutations of cities
    for perm in itertools.permutations(cities):
        perm_with_start = perm + (perm[0],)  # Append the starting node to the end of the permutation
        d = total_distance(perm_with_start, tsp_data)
        if d < min_distance:
            min_distance = d
            min_path = perm_with_start

    return min_path, min_distance
