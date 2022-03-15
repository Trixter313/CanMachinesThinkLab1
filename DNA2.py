print('This program will transcribe an inputted DNA string into its RNA counterpart.')
userIn = input('Please enter the DNA string of your choice: ')

output = ''
invalid = ''

for i in userIn:
    if i.upper() == 'A':
        output = output + 'U'
    elif i.upper() == 'C':
        output = output + 'G'
    elif i.upper() == 'G':
        output = output + 'C'
    elif i.upper() == 'T':
        output = output + 'A'
    else:
        output = output + 'X'
        invalid = '. One or more invalid characters were detected. They have been replaced with an X.'

print('RNA string: ' + output + invalid)
