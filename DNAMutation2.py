from random import *

print('This program will mutate 10% of an inputted DNA string to a random DNA molecule.')
inputString = input('Please enter a DNA string to be mutated: ')
outputString = ''
errorString = ''

for i in inputString:
    if random() < .1:
        letterPicker = random()
        if letterPicker <= .25:
            outputString = outputString + 'A'
        elif .25 < letterPicker <= .5:
            outputString = outputString + 'C'
        elif .5 < letterPicker <= .75:
            outputString = outputString + 'G'
        elif .75 < letterPicker <= 1:
            outputString = outputString + 'T'
        else:
            errorString = 'Something went wrong.'
    else:
        outputString = outputString + i.upper()

print('Mutated DNA string: ' + outputString + '. ' + errorString)
