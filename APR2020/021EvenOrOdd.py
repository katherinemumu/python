"""
katherinemumu
Apr 14 2020
This program will determine whether an integer is even or odd
"""

def evenOdd(n):
    if (n % 2 == 0):
        return "Even"
    else:
        return "Odd"

a = int(input("Enter an integer:"))
print(evenOdd(a))