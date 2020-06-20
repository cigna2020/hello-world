a = float(input()) # сторона басейна, м.
b = float(input()) # расход краски, мл.
v = int(input()) # обьем банки, л.

area = a**2 * 5
consumption = (area*b)/1000
result = consumption/v
print(int(result))