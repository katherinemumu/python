'''
katherinemumu
Apr 25 2020
This program will check if a variable is defined or not
'''

try:
    x = 1
except (NameError):
    print("Variable is not defined")
else:
    print("Variable is defined")

try:
    y
except(NameError):
    print("Variable not defined")
else:
    print("Variable is defined")