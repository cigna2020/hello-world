import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


points_number = int(input())
point = []



for i in range(points_number):
    i = input().split()
    point.append(i)



# for i in range(len(points)):
#     points_2.append(points[y])
#     y += 1


print(point)
print(points_2)


# r = np.sqrt((x - a) ** 2 + (y - b) ** 2)
# O_x = np.mean(points[:, 0])
# O_y = np.mean(points[:, 1])
# O_xy = np.mean(points,0)
#
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