x = input()
y = input()
numb = int(input())
radius = int(input())

x, y = x.split(), y.split()
distances = [((int(x[numb]) - int(x[i])) ** 2 + (int(y[numb]) - int(y[i])) ** 2) * 0.5 for i in range(len(x))]

count = 0

for i in distances:
    if i <= radius:
        count += 1
print(count)


# print(int(a[7]))
#
# d = [int(a[i]) for i in range(len(a))]
# g = [((int(a[7]) - int(a[7]))**2 + (int(b[7]) - int(b[7])**2))*0.5]
# print(c)
# print(d)
# print(g)

# print((20 - 20)**2 + )
