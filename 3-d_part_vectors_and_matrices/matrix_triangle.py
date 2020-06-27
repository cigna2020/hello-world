import numpy as np
import matplotlib as mt

points_count = int(input())
points = []

for i in range(points_count):
    i = str(input())
    y = i.split()
    points.append(y)

angle = int(input())
angle = np.radians(angle)


massive = np.array(points, dtype=float)

rotate = np.array([[np.cos(angle), np.sin(angle)], [np.sin(angle)*-1, np.cos(angle)]])

multiply = np.dot(massive, rotate)

average_1 = np.mean(multiply[:, 0])
average_2 = np.mean(multiply[:, 1])

print("avg_x = %6.2f, avg_y=%6.2f" %(average_1, average_2))


# import numpy as np
#
#
# points_count = (input())
# point_1 = np.array(input().split(), dtype=float)
# point_2 = np.array(input().split(), dtype=float)
# point_3 = np.array(input().split(), dtype=float)
# angle = np.array(input().split(), dtype=int)
# angle = np.radians(angle[0])
#
# massive = np.array([point_1, point_2, point_3])
#
# rotate = np.array([[np.cos(angle), np.sin(angle)], [np.sin(angle)*-1, np.cos(angle)]])
#
# multiply = np.dot(massive, rotate)
#
# average_1 = np.average(multiply[:, 0])
# average_2 = np.average(multiply[:, 1])
#
# print("avg_x = %6.2f, avg_y=%6.2f" %(average_1, average_2))
