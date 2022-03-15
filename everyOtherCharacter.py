print('This program will take an inputted string and output every other letter.')
inputString = input('String to be mutilated: ')
outputString = ''
counter = 0

for i in inputString:
    if counter % 2 == 0:
        outputString = outputString + i
        counter += 1
    else:
        counter += 1

print(outputString)
