import numpy as np


all_parts_road = np.array([16, 11, 10, 15, 6, 11, 14, 10, 6, 11, 16])#np.array(input().split(), dtype=int)
all_average_speed = np.array([56, 62, 36, 69, 41, 50, 63, 33, 30, 63, 49])#np.array(input().split(), dtype=int)
start = 2  #int(input())
finish = 7 #int(input())

traveling_length = np.sum(all_parts_road[start:finish+1])
traveling_time = np.sum(all_parts_road[start:finish+1] / all_average_speed[start:finish+1])
average_speed = traveling_length/traveling_time

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" %(traveling_length, traveling_time, average_speed))
