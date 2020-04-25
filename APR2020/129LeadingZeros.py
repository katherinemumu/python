'''
katherinemumu
Apr 25 2020
This program will add leading zeros in a string
'''

str1='122.22'
print("Original String: ",str1)
str1 = str1.ljust(18, '0')
print(str1)
str1 = str1.ljust(100, '0')
print(str1)

str1 = str1.rjust(140, 'n')
print(str1)