import math

a = float(input()) # сторона басейна, м.
b = float(input()) # расход краски, мл.
v = float(input()) # обьем банки, л.

if a <= 0 or b <= 0 or v <= 0:
    print('error')
else:
    area = a**2 * 5
    consumption = (area*b)/1000
    result = math.ceil(consumption/v)
    print(result)


