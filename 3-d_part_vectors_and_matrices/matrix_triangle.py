import numpy as np
import matplotlib as mt

points_count = 3 #int(input())
point_1 = np.array([-7, -8]) #np.array(input().split(), dtype=float)
point_2 = np.array([-11, 4]) #np.array(input().split(), dtype=float)
point_3 = np.array([-9, 5]) #np.array(input().split(), dtype=float)
angle = 5 #int(input())
angle = np.radians(angle)

massive = np.array([point_1, point_2, point_3])

rotate = np.array([[np.cos(angle), np.sin(angle)], [np.sin(angle)*-1, np.cos(angle)]])

multiply = np.dot(massive, rotate)

average_1 = np.average(multiply[:, 0])
average_2 = np.average(multiply[:, 1])

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
