import numpy as np


def get_trend(x, a):
    "функция для вычисления значений полинома второй степени в точке x"
    y = a[0] * x **2 + a[1]* x + a[2]
    return y

x_array = np.array(input().split(), dtype=float)
y_array = np.array(input().split(), dtype=float)
x_target = float(input())
y_target = float(input())

a = np.polyfit(x_array, y_array, 2) # Построим траекторию движения снаряда

h_zero = get_trend(0, a)  # вычислим высоту, на которой находилась пушка

# Вычислим, на какой высоте будет находиться снаряд в точке по оси ОХ, где расположена мишень
h_target = get_trend(x_target, a)

delta_h = abs(h_target - y_target) # Определим, попадет ли снаряд в мишень, расположена на высоте 51 метр

if delta_h <= 0.5:  # радиус мишени 50 см =0.5 м
    print("h0 = %6.2f, %2s" % (h_zero, 'да'))
else:
    print("h0 = %6.2f, %2s" % (h_zero, 'нет'))