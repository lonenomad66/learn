#  Copyright (c) 15.11.2024, 17:50
#  Поликарпов О.Е.
#  learn
#  Практическое задание по курсу "Разработчик Python"
#
#

def calls_count():
    global calls
    calls += 1

def string_info(str_):
    calls_count()
    return (len(str_), str_.upper(), str_.lower())

def is_contains(string, list_to_search):
    calls_count()
    flag = False
    for each in list_to_search:
        if each.lower() == string.lower(): flag = True
    return flag

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
