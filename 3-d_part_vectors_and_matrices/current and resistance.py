import numpy as np

resist = np.array(input().split(), dtype=float)
current = np.array(input().split(), dtype=float)

i = np.sum(current)
r = 0
for _ in resist:
    y = 1/_
    r += y

u = i * (1/r)

print("R = %6.3f Ом, I = %6.3f А, U = %6.3f В" %(1/r, i, u))