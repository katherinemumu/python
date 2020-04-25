'''
katherinemumu
Apr 25 2020
This program will split a variable length string into variables
'''

l = ['a', 'b', 'c']

l = l + [None] * 3

x, y, z = l[0:3]

print(x, y, z)