year = int(input())

print('error' if year < 1582 else 366 if year % 100 and year % 4 ==0 or year % 400 == 0 else 365)
