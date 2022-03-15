from random import *

print('This program will mutate 10% of an inputted DNA string to a T.')
inputString = input('Please enter a DNA string to be mutated: ')
outputString = ''

for i in inputString:
    if random() < .1:
        outputString = outputString + "T"
    else:
        outputString = outputString + i.upper()

print('Mutated DNA string: ' + outputString)