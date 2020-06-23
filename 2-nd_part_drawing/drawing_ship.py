from matplotlib.patches import Path, PathPatch
import matplotlib.pyplot as plt

n = # размер области

m  = # размер области

plt.xlim(0, n)

plt.ylim(0,m)

ax = plt.gca()

# создать массив точек
vertices = [(1, 3), (7, 2), (6, 1), (3, 1), (1, 3), (4, 2.5), (4,6), (7, 3), (4,2.5)]

#создать список кодов для последовательности рисования:
codes = #список


#создать объект pyth
path = Path(vertices, codes)

#создать фигуру
path_patch = PathPatch(path, lw = 3)

# Добавить созданную фигуру в область ax:
#оператор 1

plt.show()