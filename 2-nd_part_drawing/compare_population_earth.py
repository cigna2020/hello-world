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


index_min_error = error_list.index(min(error_list[a_range:b_range+1]))
index_max_error = error_list.index(max(error_list[a_range:b_range+1]))
min_year = years[index_min_error]
max_year = years[index_max_error]
evereg_error = sum(error_list[a_range:b_range+1])/len(error_list[a_range:b_range+1])*100

print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f" %(min_year, max_year, evereg_error))


