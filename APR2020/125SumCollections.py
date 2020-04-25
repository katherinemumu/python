'''
katherinemumu
Apr 25 2020
This program will sum of all counts in a collection
'''

import collections

num = [1,2,3,4,5,6,1,1,5,6]

print(sum(collections.Counter(num).values()))