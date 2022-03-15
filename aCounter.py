print("This program will return the amount of each DNA molecule in the provided text.")
userIn = input("Please enter a DNA string: ")

aCount = 0
cCount = 0
gCount = 0
tCount = 0
invalid = ''
for i in userIn:
    if i.upper() == 'A':
        aCount += 1
    elif i.upper() == 'C':
        cCount += 1
    elif i.upper() == 'G':
        gCount += 1
    elif i.upper() == 'T':
        tCount += 1
    else:
        invalid = ' Invalid characters were detected that have been ignored.'

print('There are ' + str(aCount) + " A's, " + str(cCount) + " C's, " + str(gCount) + " G's, and " + str(tCount) +
      " T's in your input." + invalid)
