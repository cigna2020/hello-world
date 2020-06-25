temperature_0 = input()
temperature_12 = input()
average_temperature = float(input())

list_temp_0 = temperature_0.split()
list_temp_12 = temperature_12.split()
list_average = [(float(list_temp_0[i]) + float(list_temp_12[i])) / 2 for i in range(len(list_temp_0))]

for i in range(len(list_average)):
    if float(list_average[i]) > average_temperature:
        print(i)


