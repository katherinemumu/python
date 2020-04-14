"""
katherinemumu
Apr 14 2020
This program will print the first 2 characters of a string n times
"""

def multiple(s, n):
    print(s * n)

a = input("Enter the string: ")
b = int(input("Enter the number of times you want to repeat it: "))

multiple(a[0:2], b)