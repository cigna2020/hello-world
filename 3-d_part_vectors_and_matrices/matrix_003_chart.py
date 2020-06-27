import numpy as np
import matplotlib.pyplot as plt

#задаем координаты точек
points = np.array([[1,3],[3,-2], [2,3],[-3,4],[-2,-1]])

# вычисляем координаты средней точки
mean_point = np.mean(points, 0)
print("Средняя точка: ",np.round(mean_point, 2))

# выводим точки на график
plt.plot(points[:,0], points[:,1],"bo")
plt.plot(mean_point[0], mean_point[1],"ro")

# устанавливаем оси
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.show()