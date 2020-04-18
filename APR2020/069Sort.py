'''
katherinemumu
Apr 18 2020
This program will sort 3 numbers without using loops or conditionals
'''

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

a = max(x, y, z)
b = min(x, y, z)
c = x + y + z - a - b

print(b, c, a)