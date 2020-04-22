'''
katherinemumu
Apr 22 2020
This program will get numbers divisible by 15 using anonymous function ;oo
'''

l = [15, 23, 150, 30, 45, 123, 1234, 67]

newl = list(filter(lambda x: x % 15 == 0, l))

print(newl)