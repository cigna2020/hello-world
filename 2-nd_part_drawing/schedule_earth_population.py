import math, matplotlib.pyplot as plt

def compute_population(t):
   arcctan = math.pi/2-(math.atan((2000-t)/45))
   n = (172/45) * arcctan
   return n

a = 2300
b = 2400

h = range(a, b, 1)

years_str_list = list(h)
years_list = list(int(x) for x in years_str_list)

for z in years_list:
    print(("%5d - %6.3f миллиард(ов)" % (z, compute_population(z))))

plt.xlabel('год')
plt.ylabel('численность населения')


plt.gca().spines["left"].set_position('center')
plt.gca().spines["bottom"].set_position('center')
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.plot(years_str_list, years_list)



plt.show()