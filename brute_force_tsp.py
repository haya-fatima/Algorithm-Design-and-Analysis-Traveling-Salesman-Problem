import math
import itertools
import matplotlib.pyplot as plt
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
    return tsp_data

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

def brute_force(tsp_data):
    cities = list(tsp_data.keys())
    min_distance = float('inf')
    min_path = None

    # Generate all permutations of cities
    for perm in itertools.permutations(cities):
        perm_with_start = perm + (perm[0],)  # Append the starting node to the end of the permutation
        d = total_distance(perm_with_start, tsp_data)
        print(d, perm_with_start)
        if d < min_distance:
            min_distance = d
            min_path = perm_with_start

    return min_path, min_distance

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

if __name__ == "__main__":
    filename = "datasets/s10.tsp"
    tsp_data = read_tsp_data(filename)

    optimal_tour, distance = brute_force(tsp_data)
    print("Optimal Tour:", optimal_tour)
    print("Total Distance:", distance)

    plot_tour(optimal_tour, tsp_data)
