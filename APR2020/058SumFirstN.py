'''
katherinemumu
Apr 15 2020
This program will sum the first n numbers
'''

def sumN(n):
    s = 0
    for i in range(n):
       s += i + 1
    return s

print(sumN(5)) 