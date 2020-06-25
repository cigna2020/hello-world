import numpy as np

def compute_population(t):
    c = 172
    t_1 = 2000
    tau = 45
    y = c / tau * (np.pi / 2 - np.arctan((t_1-t)/tau))
    return y

t = np.array([1000, 1500, 1800, 1850, 1900, 1950, 1990, 2019, 2030])

print("Годы : ", t)

print("Численность : ", np.round(compute_population(t), 3))

lst = zip(t, np.round(compute_population(t), 3))
print(list(lst))