import numpy as np


all_parts_road = np.array([16, 11, 10, 15, 6, 11, 14, 10, 6, 11, 16])#np.array(input().split(), dtype=int)
all_average_speed = np.array([56, 62, 36, 69, 41, 50, 63, 33, 30, 63, 49])#np.array(input().split(), dtype=int)
start = 2  #int(input())
finish = 7 #int(input())

traveling_length = np.sum(all_parts_road[start:finish+1])

print(traveling_length)