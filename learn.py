def has_digit(name):
    return all(char.isdigit() for char in name)

name = '12345'
print(has_digit(name))
name = '123m5'
print(has_digit(name))
name = 'ma3ma'
print(has_digit(name))
