temperature_0 = input()
temperature_12 = input()
average_temperature = float(input())

list_temp_0 = temperature_0.split()
list_temp_12 = temperature_12.split()
list_average = [(float(list_temp_0[i]) + float(list_temp_12[i])) / 2 for i in range(len(list_temp_0))]

for i in range(len(list_average)):
    if float(list_average[i]) > average_temperature:
        print(i)


"""
Вариант №1
n, d, m = [float(n) for n in input().split()], [float(d) for d in input().split()], float(input())
[print(i) for i in range(len(n)) if (n[i] + d[i])/2 > m]

Вариант №2
a, b, x = input().split(), input().split(), float(input())
[print(i) for i in range(len(a)) if (float(a[i])+float(b[i]))/2 > x]

№3
f = [float(x) for x in input().split()]
t = [float(x) for x in input().split()]
av = float(input())

for i in range(len(f)):
    avd = (f[i] + t[i]) / 2
    if avd > av:
        print(i)
"""
