'''
katherinemumu
Apr 28 2020
This program will print out a random combination of the vowels a, e, i, o, u
'''

import random

c = ['a', 'e', 'i', 'o', 'u']

random.shuffle(c)

print(''.join(c))