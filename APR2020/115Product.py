'''
katherinemumu
Apr 24 2020
This program will compute the product of the numbers in a list without for loop
'''

from functools import reduce

l = [2, 2, 3]

n = reduce(lambda x,y: x * y, l)

print(n)