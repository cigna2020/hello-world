import math

x = float(input())
y = float(input())

a = (x + (math.sqrt(3)/2)*math.pi)
b = math.sqrt((2-(math.cos(y)**2)))

z = ((math.asin(math.cos(a))) + (1.2*b))/(x**2 + y**2 + 1)
print(round(z, 5))