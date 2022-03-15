print('This program will transcribe an inputted DNA molecule into its RNA counterpart.')
userIn = input('Please enter the DNA molecule of your choice: ')

if userIn.upper() == 'A':
    print('U')
elif userIn.upper() == 'C':
    print('G')
elif userIn.upper() == 'G':
    print('C')
elif userIn.upper() == 'T':
    print('A')
else:
    print('That is not a valid DNA molecule.')
