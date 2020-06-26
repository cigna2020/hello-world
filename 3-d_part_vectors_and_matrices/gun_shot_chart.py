import matplotlib.pyplot as plt


x_trend = [i for i in range(0,1500,10)] # список со значениями координат по оси OX
y_trend = [get_trend(x, a) for x in x_trend] #список координат по оси OY, значения которого посчитаны с помощью функции тренда

plt.plot(x_array, h_array, 'go', label = "положение снаряда") #Сформируем линию для отображения точных координат положений снаряда
