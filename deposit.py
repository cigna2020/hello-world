# deposit - сумма вклада, interest_rate -процентная ставка,
# amount_months - количество месяцев
def compute_income(deposit, interest_rate, amount_months):
    # deposit, interest_rate, amount_months = x, k, n
    s = deposit * ((1 + interest_rate / (12 * 100))**amount_months)
    profit = s - deposit
    print(int(profit))

x = float(input())
k = float(input())
n = int(input())

result = compute_income(x, k, n)
