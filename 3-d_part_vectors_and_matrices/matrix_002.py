import numpy as np
import numpy.linalg as alg


a = np.array([[-2, -8.5, -3.4, 3.5], [0, 2.4, 0, 8.2], [2.5, 1.6, 2.1, 3], [0.3, -0.4, -4.8, 4.6]])

b = np.array([-1.88, -3.28, -0.5, -2.83])

a_inv = alg.inv(a)

x = np.dot(a_inv, b)


print("[ %1.1f %1.1f  %1.1f %1.1f]" %(x[0], x[1], x[2], x[3]))