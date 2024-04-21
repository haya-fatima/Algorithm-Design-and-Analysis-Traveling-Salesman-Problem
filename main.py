import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from dynamicTSP import *
from greedyTSP import *
from readData import *

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
    img = Image.new("RGB", (image_size[0]+30,image_size[1]+30), "white")
    draw = ImageDraw.Draw(img)

    # Draw the tour as lines
    for i in range(len(x) - 1):
        draw.line((x[i], y[i], x[i + 1], y[i + 1]), fill=line_color)

    # Draw points
    for i in range(len(x)):
        draw.ellipse((x[i] - 3, y[i] - 3, x[i] + 3, y[i] + 3), fill=point_color)
        draw.text((x[i] + 5, y[i] + 5), str(solution[i]), fill=(0, 0, 0))

    # Show plot
    img.show()

filename = r"datasets\s4.tsp"
tsp_data = read_tsp_data(filename)

optimal_tour, distance = greedy_tsp(tsp_data)
print("Optimal Tour:", optimal_tour)
print("Total Distance:", distance)

plot_tour(optimal_tour, tsp_data)