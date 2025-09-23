# input() and concatenation
name = input('what is your name? ')
fav_color = input('what is your favourite color? ')
print('Hi ' + name)
print(name + ' likes ' + fav_color)

# input() and typecasting
birth_year = input('what is your birth_year? ')
print('type of birth variable: ', type(birth_year))
age = 2025 - int(birth_year)
print('type of age variable: ', type(age))
print(age)

weight_ibs = input('what is your weight(in pounds)? ')
weight_kg = int(weight_ibs) * 0.4536
print(weight_kg)