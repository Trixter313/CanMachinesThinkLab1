print('This program will take a string and output the last n amount of letters, in reverse.')
inputString = input('String to be cut: ')
n = int(input('Amount of letters to be printed: '))
counter = 0
outputString = ''

for i in inputString:
    if counter >= len(inputString) - n:
        outputString = i + outputString
        counter += 1
    else:
        counter += 1

print(outputString)
