def compute_payment(t, s, n, k):
    p = s/n + (s - (t - 1) * (s / n)) * (k / (12 * 100))
    return p

def comput_ann(s, n, k):
    ka = k/(12*100)
    pa = ((ka * ((1 + ka) ** n)) / (((1 + ka) ** n) - 1)) * s
    return pa


s, n, k = int(input()), int(input()), int(input())

t = 0
z = -1
t_list = [i for i in range(1, n+1)]
payment_list = [compute_payment(t, s, n, k) for t in t_list]
payment_list_2 = (float(comput_ann(s, n, k)) * n) - s

if n <= 0:
    print("Неверные данные")
else:
    while z != n-1:
        z += 1
        print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (t_list[z], payment_list[z], comput_ann(s, n, k)))


doh = (sum(payment_list)) - s
print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (doh, payment_list_2))


# s, n, k = [int(input()) for _ in range(3)]
# db = 0
# for t in range(1, n+1):
#     p = s/n + (s - (t-1)*s/n)*k/1200
#     db += p
#     print("%2d месяц - %8.2f руб" % (t, p))
# print("Доход банка - %6.2f руб" % (db-s))