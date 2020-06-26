import numpy as np

def get_trend1(x, a1):
    y =  a1[0] * x + a1[1]
    return y

def get_trend2(x, a2):
    y = a2[0] * x**2 + a2[1] * x + a2[2]
    return y

def otn_pogr(y, yr):
    p = abs((yr - y) / y) * 100
    return p

x_array, y_array = np.array([input().split()], dtype = float), np.array([input().split()], dtype = float)
x = x_array[0, :]
y = y_array[0, :]
path_1 = np.polyfit(x, y, 1)
path_2 = np.polyfit(x, y, 2)
# path_3 = otn_pogr(y_array, y)


print("%5.3f %5.3f" % (path_1[0], path_1[1]))
print("%5.3f %5.3f %5.3f" % (path_2[0], path_2[1], path_2[2]))
# print(path_3)