print('This program will take two inputted numbers and output them in order of least to greatest.')
number1 = input('Number 1: ')
number2 = input('Number 2: ')

if number1 < number2:
    print(number1 + ', ' + number2)
elif number2 < number1:
    print(number2 + ', ' + number1)
elif number1 == number2:
    print('The numbers ' + number1 + ' and ' + number2 + ' are equal.')
else:
    print('Something went wrong.')
