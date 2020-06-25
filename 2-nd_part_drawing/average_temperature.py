temperature_0 = ('3.4 0.7 2.0 0.4 2.5 2.6 1.7 0.2 4.0 2.5') #input('0 = ')
temperature_12 = ('6.4 8.3 6.8 6.7 7.4 6.4 8.9 4.7 5.3 7.6') #input('12 = ')
average_temperature = 4.5 #float(input('average = '))

list_temp_0 = temperature_0.split()
list_temp_12 = temperature_12.split()
list_average = [((float(list_temp_0[i]) + float(list_temp_12[i])) / 2 for i in range(len(list_temp_0)))]


# for i in range(len(list_average)):
#     if float(list_average[i] > average_temperature:
#         print(i)


# print('temp_0 = ', temperature_0, 'temp_12 = ', temperature_12, 'average_tmp = ', average_temperature)