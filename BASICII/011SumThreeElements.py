'''
katherinemumu
May 25 2020
This program will print out all the possible things for a sum of three numbers
'''

import itertools
from functools import partial

X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

def check_sum_array(N, *nums):
  if sum(x for x in nums) == N:
    return (True, nums)
  else:
      return (False, nums)

pro = itertools.product(X,Y,Z)
func = partial(check_sum_array, T)
sums = list(itertools.starmap(func, pro))

result = set()

for i in sums:
    if i[0]:
        result.add(i[1])
print(result)
