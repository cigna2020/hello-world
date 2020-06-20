year = int(input())

if len(str(year)) < 4 or year <= 1582:
    print('error')
elif year % 4 == 0 and str(year)[-2:] != '00':
    print('366')
elif year % 4 == 0 and str(year)[-2:] == '00' and year % 100 == 0 and year % 400 == 0:
    print('366')
else:
    print('365')

