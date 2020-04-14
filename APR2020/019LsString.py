"""
katherinemumu
Apr 14 2020
This program will add Is to the front of a string unless it is already there
"""

def addls(something):
    if (something[0:2] == 'Is'):
        return something
    else:
        return "Is" + something

s = input("Enter a string:")
print("The new string is:", addls(s))
