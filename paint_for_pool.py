a = float(input()) # сторона басейна, м.
b = float(input()) # расход краски, мл.
v = float(input()) # обьем банки, л.

if a < 0 or b < 0 or v < 0:
    print('error')
# if type(int(a)) != int or type(int(a)) != float:
#     print('error')
# if type(int(b)) != int or type(int(b)) != float:
#     print('error')
# if type(v) != int or type(v) != float:
#     print('error')
else:
    area = a**2 * 5
    consumption = round(((area*b)/1000), 0)
    result = consumption/v
    print(int(result))

