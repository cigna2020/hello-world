import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


points_number = 4 #int(input())

point = [[10.1, 14.0], [5.1, 8.5], [13.3, -3.9], [-15.8, 12.9]]
# point = []
#
# for i in range(points_number):
#     i = str(input())
#     y = i.split()
#     point.append(y)

points = np.array(point, dtype=float)

O_x = np.mean(points[:, 0])
O_y = np.mean(points[:, 1])
O_xy = np.mean(points, 0)


distance = [((float(O_xy[0]) - float(points[i, 0])) ** 2 + (float(O_xy[1]) - float(points[i, 1])) ** 2) ** 0.5 for i in range(0, points_number)]

r = distance[3]
# print(distance)
# print(points)
# # print("О(%6.3f, %6.3f)" %(O_x, O_y))

# r = np.sqrt((x - a) ** 2 + (y - b) ** 2)
#
print("О(%6.3f, %6.3f), r = %6.3f" %(O_x, O_y, r))

# plt.xlim(-30, 30)
# plt.ylim(-30, 30)
# ax = plt.gca()
# circle = Circle((O_x, O_y), np.max(rasst), fc="white", ec="red", lw = 2)
# ax.add_patch(circle)
#
# plt.gca().spines["left"].set_position("zero")
# plt.gca().spines["bottom"].set_position("zero")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)
#
#
# plt.plot(points[:,0], points[:,1], 'go')
# plt.show()


