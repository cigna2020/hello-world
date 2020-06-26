import numpy as np


road_length = input().split()
road_speed = input().split()

road_length = np.array(road_length, dtype=int)
road_speed = np.array(road_speed, dtype=int)

total_length = np.sum(road_length)
total_time = np.sum(road_length / road_speed)
average_speed = total_length/total_time

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" %(total_length, total_time, average_speed))