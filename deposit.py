# deposit - сумма вклада, interest_rate -процентная ставка,
# amount_months - количество месяцев
def compute_income(deposit, interest_rate, amount_months):
    s = deposit * ((1 + interest_rate / (12 * 100))**amount_months)
    profit = s - deposit
    print("%2.0f" % profit)

x = float(input())
k = float(input())
n = int(input())

result = compute_income(x, k, n)
