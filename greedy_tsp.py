import math
import matplotlib.pyplot as plt
import random
from PIL import Image, ImageDraw

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

def plot_tour(solution, tsp_data, image_size=(800, 600), line_color=(0, 0, 255), point_color=(255, 0, 0)):
    # Extract x and y coordinates from tsp_data
    x = [tsp_data[point][0] for point in solution]
    y = [tsp_data[point][1] for point in solution]

    # Scale coordinates to fit within image_size
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)
    scale_x = image_size[0] / (max_x - min_x)
    scale_y = image_size[1] / (max_y - min_y)
    x = [(val - min_x) * scale_x for val in x]
    y = [(val - min_y) * scale_y for val in y]

    # Create a blank image
    img = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(img)

    # Draw the tour as lines
    for i in range(len(x) - 1):
        draw.line((x[i], y[i], x[i + 1], y[i + 1]), fill=line_color)

    # Draw points
    for i in range(len(x)):
        draw.ellipse((x[i] - 3, y[i] - 3, x[i] + 3, y[i] + 3), fill=point_color)

    # Show plot
    img.show()
    
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
