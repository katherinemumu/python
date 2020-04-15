'''
katherinemumu
Apr 14 2020
This program will compute the area of a triangle
'''

def triangleArea(b, h):
    return b * h / 2

base = int(input("Enter a base: "))
height = int(input("Enter a height: "))

print("The area is", triangleArea(base, height))