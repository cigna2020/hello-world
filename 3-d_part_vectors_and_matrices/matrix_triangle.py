import numpy as np

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


"""
import numpy as np

a, q = np.array([input().split() for i in range(int(input()))], dtype=float), np.radians(float(input()))
print("avg_x = %6.2f, avg_y=%6.2f"% 
      tuple(np.dot(a,np.array([[np.cos(q),np.sin(q)],[-np.sin(q),np.cos(q)]])).mean(0))
"""


