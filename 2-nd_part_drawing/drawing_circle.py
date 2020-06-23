import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch
from matplotlib.patches import  Circle
import matplotlib.pyplot as plt

plt.xlim(0, 13)
plt.ylim(0, 13)

ax = plt.gca()
circle = Circle((6, 7),5)
ax.add_patch(circle)

plt.show()

