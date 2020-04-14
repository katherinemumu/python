"""
katherinemumu
Apr 13 2020
This program reads in a string of numbers, and prints them as a list and a tuple
"""

stuff = input("Enter your string of numbers, separated by commas pls: ")
lst = stuff.split(",")
tup = tuple(lst)

print(lst)
print(tup)
