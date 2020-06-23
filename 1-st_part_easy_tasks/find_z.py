from math import sqrt, pi, asin, cos

x = float(input())
y = float(input())

a = (x + (sqrt(3)/2)*pi)
b = sqrt((2-(cos(y)**2)))
z = ((asin(cos(a))) + (1.2*b))/(x**2 + y**2 + 1)

print(round(z, 5))