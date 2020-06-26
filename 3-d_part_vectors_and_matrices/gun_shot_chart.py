import matplotlib.pyplot as plt
import numpy as np


def get_trend(x, a):
    "функция для вычисления значений полинома второй степени в точке x"
    y = a[0] * x **2 + a[1]* x + a[2]
    return y

x_array = np.array([18.6, 99.9, 157.2, 219.9, 303.7, 399.6, 452.5, 528.4, 613.8, 669.7, 750.6, 816.2, 906.2])
h_array = np.array([85.7, 173.8, 196.7, 259.6, 332.5, 379.3, 414.2, 419.7, 461.3, 438.9,
 447.8, 434.1, 441.4])

a = np.polyfit(x_array, h_array, 2) # Построим траекторию движения снаряда

h_zero = get_trend(0, a)  # вычислим высоту, на которой находилась пушка
print("Высота, на которой стоит пушка: %6.2f м" % h_zero)

# Вычислим, на какой высоте будет находиться снаряд в точке по оси ОХ, где расположена мишень
x_target = 1450
h_target = get_trend(x_target, a)
print("Высота, в точке %4d м: %6.2f м" % (x_target, h_target))

delta_h = abs(51 - h_target) # Определим, попадет ли снаряд в мишень, расположена на высоте 51 метр
if delta_h <= 0.5:  # радиус мишени 50 см =0.5 м
    print("Снаряд попадет в мишень.")
else:
    print("Снаряд не попадет в мишень.")

x_trend = [i for i in range(0,1500,10)] # список со значениями координат по оси OX
y_trend = [get_trend(x, a) for x in x_trend] #список координат по оси OY, значения которого посчитаны с помощью функции тренда

plt.plot(x_array, h_array, 'go', label = "положение снаряда") #Сформируем линию для отображения точных координат положений снаряда

plt.plot(x_trend, y_trend, 'r-', label = "линия тренда") #Сформируем график линии тренда

# Отформатируем оси, выведем легенду и покажем область построения
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.legend(loc="lower center")


plt.plot([x_target], [h_target], 'b+', markersize = 12)


plt.show()