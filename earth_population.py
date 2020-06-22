import math

def compute_population(t):
   #вычислить численность населения для года t по формуле
   arcctan = math.pi/2-(math.atan((2000-t)/45))
   n = (172/45) * arcctan
   return n


line = input() #ввести строку с перечисленными через пробел годами

years_str_list = line.split() # преобразовать строку в список из строковых значений годов

# сформировать список years_list на основе years_str_list,
#преобразовав строковые значения в целые
years_list = list(int(x) for x in years_str_list)

for z in years_list:
    print(("%5d - %6.3f миллиард(ов)" % (z, compute_population(z))))
