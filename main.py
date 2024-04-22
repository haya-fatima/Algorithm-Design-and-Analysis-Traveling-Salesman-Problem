import matplotlib.pyplot as plt
import time
from PIL import Image, ImageDraw
from dynamicTSP import *
from greedyTSP import *
from bruteTSP import *
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

# filename = r"datasets\s4.tsp"
# tsp_data = read_tsp_data(filename)

# optimal_tour, distance = greedy_tsp(tsp_data)
# print("Optimal Tour:", optimal_tour)
# print("Total Distance:", distance)

# plot_tour(optimal_tour, tsp_data)

# runtime_data = [[" ", "Dynamic Programming", "Greedy", "Brute Force"]]
runtime_data = []

def populate_string(time, dis):
    s = ""
    s += str(round(time,3))
    s += ":"
    s += str(round(dis,2))
    return s

for i in range(13, 15):
    filename = f"datasets/s{i}.tsp"
    tsp_data = read_tsp_data(filename)
    
    start_time_dp = time.time()
    optimal_tour_dp, distance_dp = dp_tsp(tsp_data)
    end_time_dp = time.time()
    elapsed_time_dp = end_time_dp - start_time_dp
    sd = populate_string(distance_dp, elapsed_time_dp)
    
    start_time_gr = time.time()
    optimal_tour_gr, distance_gr = greedy_tsp(tsp_data)
    end_time_gr = time.time()
    elapsed_time_gr = end_time_gr - start_time_gr
    sg = populate_string(distance_gr, elapsed_time_gr)
    
    start_time_bf = time.time()
    optimal_tour_bf, distance_bf = bf_tsp(tsp_data)
    end_time_bf = time.time()
    elapsed_time_bf = end_time_bf - start_time_bf
    sb = populate_string(distance_bf, elapsed_time_bf)
    
    runtime_data.append([f"s{i}", sd, sg, sb])

column_widths = [max(len(cell) for cell in column) for column in zip(*runtime_data)]

with open("runtimes.txt", "a+") as file:
    # Write the table to the file
    for row in runtime_data:
        file.write("|".join(cell.ljust(width) for cell, width in zip(row, column_widths)) + "\n")
