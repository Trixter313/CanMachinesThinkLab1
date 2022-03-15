print("This program will take two DNA strings and return the one containing the most A's.")
dnaString1 = input('Enter DNA string one: ')
dnaString2 = input('Enter DNA string two: ')

string1A = 0
string2A = 0
for i in dnaString1:
    if i.upper() == 'A':
        string1A += 1

for i in dnaString2:
    if i.upper() == 'A':
        string2A += 1

if string1A > string2A:
    print("The first string contained more A's, with a total of " + str(string1A) + ".")
elif string2A > string1A:
    print("The second string contained more A's, with a total of " + str(string2A) + ".")
elif string1A == string2A:
    print("The strings contained the same amount of A's, with each having a total of " + str(string1A) + ".")
else:
    print('Something went wrong.')
