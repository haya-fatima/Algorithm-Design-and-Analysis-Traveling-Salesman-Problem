import random
import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def greedy_tsp(tsp_data):
    # Start from the first point
    current_point = random.choice(list(tsp_data.keys()))
    tour = [current_point]
    remaining_points = set(tsp_data.keys())
    remaining_points.remove(current_point)
    total_distance = 0

    while remaining_points:
        nearest_point = min(remaining_points, key=lambda x: euclidean_distance(tsp_data[current_point], tsp_data[x]))
        total_distance += euclidean_distance(tsp_data[current_point], tsp_data[nearest_point])
        tour.append(nearest_point)
        remaining_points.remove(nearest_point)
        current_point = nearest_point

    # Return to the starting point to complete the tour
    total_distance += euclidean_distance(tsp_data[tour[-1]], tsp_data[tour[0]])
    tour.append(tour[0])

    return tour, total_distance