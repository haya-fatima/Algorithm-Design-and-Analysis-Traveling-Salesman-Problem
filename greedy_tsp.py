import math
import matplotlib.pyplot as plt
import random

def read_tsp_data(filename):
    tsp_data = {}
    with open(filename, 'r') as file:
        lines = file.readlines()

        # Find the index where NODE_COORD_SECTION starts
        coord_section_index = lines.index('NODE_COORD_SECTION\n')

        # Iterate over lines after NODE_COORD_SECTION and extract coordinates
        for line in lines[coord_section_index + 1:]:
            if line.strip() == 'EOF':
                break
            node, x, y = line.strip().split(' ')
            tsp_data[int(node)] = (float(x), float(y))
    # print(tsp_data)
    return tsp_data

def plot_tour(solution, tsp_data):
    # Extract x and y coordinates from tsp_data
    x = [tsp_data[point][0] for point in solution]
    y = [tsp_data[point][1] for point in solution]

    # Connect the points in the order specified by the solution
    x.append(x[0])  # Closing the loop
    y.append(y[0])  # Closing the loop

    # Plot the tour
    plt.plot(x, y, marker='o')

    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Optimal Tour')

    # Show plot
    plt.show()
    
def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def greedy_tsp(tsp_data):
    """
    Greedy algorithm for the Traveling Salesman Problem.
    """
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

filename = "qa194.tsp"
tsp_data = read_tsp_data(filename)

optimal_tour, distance = greedy_tsp(tsp_data)
print("Optimal Tour:", optimal_tour)
print("Total Distance:", distance)

plot_tour(optimal_tour, tsp_data)
