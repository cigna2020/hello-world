x = input() #координаты населенных пунктов по оси OX
y = input() # координаты населенных пунктов по оси OY
numb = int(input()) # номер населенного пункта k
radius = int(input())

x, y = x.split(), y.split()
distances = [((int(x[numb]) - int(x[i])) ** 2 + (int(y[numb]) - int(y[i])) ** 2) ** 0.5 for i in range(len(x))]

count = 0

for i in distances:
    if i <= radius:
        count += 1
print(count)
