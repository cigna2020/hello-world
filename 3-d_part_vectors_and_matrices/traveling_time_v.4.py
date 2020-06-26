import numpy as np


all_parts_road = np.array(input().split(), dtype=int)
all_average_speed = np.array(input().split(), dtype=int)
start = int(input())
finish = int(input())

traveling_length = np.sum(all_parts_road[start:finish+1])
traveling_time = np.sum(all_parts_road[start:finish+1] / all_average_speed[start:finish+1])
average_speed = traveling_length/traveling_time

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" %(traveling_length, traveling_time, average_speed))
