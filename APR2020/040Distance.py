'''
katherinemumu
Apr 15 2020
This program will compute the distance between 2 points
'''
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(distance(4, 0, 6, 6))

