# -*- coding: utf-8 -*-
print("Ваше имя?")

name = input()

print("Привет, ", name, "!")

age = int(input("Сколько Вам полных лет? "))

height = float(input("Ваш рост? "))

weight = float(input("Ваш вес? "))

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:

    print("Ошибочные входные данные")

else:
    bmi = weight / height ** 2

    bmi = round(bmi, 2)

    print("Ваш индекс массы тела: ", str(bmi))

    if bmi < 18.5:

        description = "недостаточной массой тела."

    elif bmi < 25:

        description = "нормальной массой тела."

    elif bmi < 30:

        description = "избыточной массой тела."

    else:

        description = "ожирением."

    print("Вы относитесь к группе людей с", description)