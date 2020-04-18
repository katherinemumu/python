'''
katherinemumu
Apr 18 2020
This program will calculate the hypotneuse of a right angled triangle
'''

import math

def hyp(a, b):
    return math.sqrt(a**2 + b**2)

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

print(hyp(n1, n2))