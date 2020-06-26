import numpy as np


path = np.array([15, 5, 12, 2, 21, 17, 21, 3, 10, 5])
speed = np.array([60, 30, 60,45, 50, 60, 50, 40, 60, 40])

len_path = path.sum() #Вычислим длину пути, можно й так: len_path = np.sum(path)
print("Расстояние между пунктами А и В :", len_path)

time = path / speed # Вычислим время прохождения автомобилем каждого участка
print("Время на каждом участке :", np.round(time, 2))

sum_time = time.sum() #  Вычислим общее время в пути
print("Общее время в пути : ", round(sum_time, 2))

avg_speed = len_path / sum_time  # Посчитаем среднюю скорость
print("Средняя скорость : ", round(avg_speed, 2))