consumed = input().split()
norm = int(input())
cost_norm = float(input())
cost_over = float(input())

total_consumed = sum(int(consumed[i]) for i in range(len(consumed)))
total_cost = 0


for i in consumed:
    if int(i) > norm:
        total_cost += ((int(i) - norm) * cost_over) + (norm * cost_norm)
    else:
        total_cost += int(i)*cost_norm

print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (total_consumed, total_cost))

"""
short variant:
m = list(map(int, input().split()))
n, a, b = int(input()), float(input()), float(input())

print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (sum(m), sum(k*a if k <= n else n*a + (k-n)*b for k in m)))
"""