consumed = '150 132 110 186 103 229 179 224 230 113 224 202'.split()
norm = 148
cost_norm = 3.67
cost_over = 4.83

total_consumed = sum(int(consumed[i]) for i in range(len(consumed)))

print(total_consumed)
