import math

def compute_population(t):
   arcctan = math.pi/2-(math.atan((2000-t)/45))
   n = (172/45) * arcctan
   return n


years = [1000, 1750, 1800, 1850, 1900, 1950, 1955, 1960, 1965,
         1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010,
         2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

populalion = [0.400,0.791,1.000,1.262,1.650,2.519,
             2.756,3.021,3.335,3.692,4.068,4.435,4.831,
             5.264,5.674,6.071,6.344,6.933, 7.015,7.100,
             7.162,7.271,7.358,7.444,7.530,7.669,7.763]

a_range = int(input('a = '))
b_range = int(input('b = '))

populalion_theory = [compute_population(t) for t in years]

error_list = [abs((populalion[i] - populalion_theory[i]) / populalion[i])
for i in range(len(years))]



print('min = ', min(error_list)*100, 'max = ', max(error_list), 'mean = ', (sum(error_list)/len(error_list))*100)


"Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f"


print("-" * 40)

print("|%7s | %7s | %7s |%8s |" % ("1","2","exp(t)", "error"))

print( "-" * 40)

for i in range(len(years)):
    print("| %7.3f | %7.3f | %7.0f |%7.3f%% |"
          % (populalion[i], populalion_theory[i], years[i], error_list[i] * 100))

print("-" * 40)

# for z in years:
#     print(("%5d - %6.3f миллиард(ов)" % (z, compute_population(z))))
