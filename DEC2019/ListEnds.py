'''
this program will take a list of numbrs and make a new list of the first
and last elements of the list
'''

import random

a = random.sample(range(10),random.randint(1,10))
print(a)

b = [a[0], a[-1]]
print(b)
