'''
katherinemumu
Apr 24 2020
This program will filter a list for the positive numbers
'''

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l = list(filter(lambda x: x % 2 == 0, l))

print(l)