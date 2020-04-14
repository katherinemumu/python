'''
will return the list of elements that appear in both lists
'''

import random

a = random.sample(range(10),random.randint(1,10))
b = random.sample(range(10),random.randint(1,10))

print(a, "\n", b)
a = [1,1,2]
b = [1,2,4]
c = [x for x in set(a) if x in b]
print(c)

'''
difference between sets and lists is that the same element cannot
appear in the set
'''
