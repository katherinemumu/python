"""
katherinemumu
Apr 13 2020
This program prints out the area of a circle given input
"""

import math

print("Enter a radius or smth: ")
r = float(input())

area = r**2 * math.pi

print("r = " + str(r))
print("area = " + str(area))