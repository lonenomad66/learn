#  Copyright (c) 24.11.2024, 07:16
#  Поликарпов О.Е.
#  learn
#  Практическое задание по курсу "Разработчик Python"
#
#

def print_params(a = 1, b = 'строка', c = True):
    print(f'{a}  {b}  {c} \n')

# варианты вызова функции с предопределенными параметрами
print('Вызываем без аргументов')
print_params()
print('Меняем первый аргумент')
print_params(2)
print('Меняем первый и второй аргументы')
print_params(3, 'Oleg')
print('Вызываем с тремя аргументами')
print_params(5, 'Denis', False)
print('Меняем только второй аргументы')
print_params(b=42)
print('Меняем только третий аргументы')
print_params(c = [1,2,3])

# распаковка параметров
print('Распаковка параметров из списка')
values_list = [25, 'My list', 25.93]
print_params(*values_list)

print('Распаковка параметров из словаря')
values_dict = {'a': 100, 'b': 'String', 'c': False}
print_params(**values_dict)

print('Распаковка + отдельные параметры')
values_list_2 = ['0000 0001', 'Byte']
print_params(*values_list_2, 42)