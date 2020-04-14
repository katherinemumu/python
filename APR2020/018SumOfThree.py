"""
katherinemumu
Apr 14 2020
This program will calculate the sum of 3 numbers, and if they are the same,
the it will return 3 times that value
"""

def threesum(n1, n2, n3):
    if (n1 == n2 == n3):
        return (n1 + n2 + n3) * 3
    else:
        return n1 + n2 + n3

a1 = int(input("Enter the first number: "))
a2 = int(input("Enter the second number: "))
a3 = int(input("Enter the third number: "))

print("The answer is", threesum(a1, a2, a3))