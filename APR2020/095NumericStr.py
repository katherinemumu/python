'''
katherinemumu
Apr 21 2020
This program will check if a string is numeric
'''

#str = 'a123'
str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()