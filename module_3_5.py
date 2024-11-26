#  Copyright (c) 24.11.2024, 13:24
#  Поликарпов О.Е.
#  learn
#  Практическое задание по курсу "Разработчик Python"
#
#

def get_multiplied_digits(number):
    str_number = str(number)


    if len(str_number) > 1:
        first = int(str_number[0])

        if first != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:

            return get_multiplied_digits(int(str_number[1:]))
    else:
        if int(str_number) != 0:        # если последняя цифра будет 0,  то обнулиться весь результат
            return int(str_number)
        else:
            return 1                    # поэтому поменяем на единицу, умножение на которую не меняет результат

result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(402030)
print(result)