ruble = int(input())

if ruble > 99 or ruble <= 0:
    print('ошибка')
elif str(ruble)[-1] == '1' and ruble != 11:
    print(ruble, 'рубль')
elif str(ruble)[-1] == '2' and ruble != '12':
    print(ruble, 'рубля')
elif str(ruble)[-1] == '3' and ruble != '13':
    print(ruble, 'рубля')
elif str(ruble)[-1] == '4' and ruble != '14':
    print(ruble, 'рубля')
else:
    print(ruble, 'рублей')