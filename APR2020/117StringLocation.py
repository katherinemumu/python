'''
katherinemumu
Apr 24 2020
This program will show that two strings with the same value will point to the same address
'''

a = 'hi'
b = 'hi'

print(id(a))
print(id(b))

print("\nMemory location of a =", hex(id(a)))
print("Memory location of b =", hex(id(b)))

print("THEYRE THE SAME YO")