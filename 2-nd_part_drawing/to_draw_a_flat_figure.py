from matplotlib.patches import Wedge, Arc
import matplotlib.pyplot as plt

x = 6
y = 5

plt.xlim(0, x)
plt.ylim(0, y)

ax = plt.gca()

figure_w = Wedge((3, 1), 2, 45, 135) # рисуем сектор (центр, радиус, углы)
ax.add_patch(figure_w)

figure_a = Arc((3, 1), 6, 6, 135, 270, lw=3)
ax.add_patch(figure_a)

plt.grid()
plt.show()