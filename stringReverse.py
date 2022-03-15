print('This program will reverse an inputted string.')
inputString = input('String to be reversed: ')
outputString = ''

for i in inputString:
    outputString = i + outputString

print(outputString)
