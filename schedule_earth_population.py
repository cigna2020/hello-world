import math, matplotlib.pyplot as plt

def compute_population(t):
   arcctan = math.pi/2-(math.atan((2000-t)/45))
   n = (172/45) * arcctan
   return n

line = input()
years_str_list = line.split()
years_list = list(int(x) for x in years_str_list)

for z in years_list:
    print(("%5d - %6.3f миллиард(ов)" % (z, compute_population(z))))

plt.gca().spines['left'].set_position('zero')