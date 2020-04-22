'''
katherinemumu
Apr 22 2020
This program will check if a number is positive, zero or negative
'''

def pnz (n):
    if (n == 0):
        print("zero")
    elif (n < 0):
        print("negative")
    else:
        print("positive")

pnz(6)
pnz(0)
pnz(-1)