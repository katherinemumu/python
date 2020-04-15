'''
katherinemumu
Apr 15 2020
This program will add two objects if they are both of type int
'''

def add(n1, n2):
    if (isinstance(n1, int) and isinstance(n2, int)):
        return n1 + n2
    else:
        raise TypeError("Inputs must be integers.")

print(add(1, 2))
# print(add('1', 2))
print(add(2, True))
print(add(4, '5'))