import numpy as np
import numpy.linalg as alg

a = np.array([[3, 4, -2],[-2, -1, 4],[1, 2, 1]])
print("A :\n", a)

b = np.array([[1, -3, -2, 1],[2, 4, -2, -1],[5, -2, 0, -2]])
print("B :\n", b)

c = np.dot(a, b) # Вычислить произведение (multiply)
print("A*B:\n", c)

det_a = alg.det(a)  # Вычислить определитель матрицы A
print("dеt(A): ", round(det_a, 1))

a_inv = alg.inv(a) # Вычислить обратную матрицу A-1
print("A^-1:\n", np.round(a_inv,1))

"""
Вычислить матричное выражение: det(A)\cdot A^{-1}\cdot B -10\cdot A^3 \cdot Bdet(A)*A^−1 * B−10⋅A^3 * B
"""
a_3 = np.dot(a, np.dot(a,a))
result = det_a * np.dot(a_inv, b) - 10 * np.dot(a_3, b)
print("Result:\n", result)