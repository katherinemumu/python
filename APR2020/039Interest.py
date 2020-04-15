'''
katherinemumu
Apr 15 2020
This program will calculate interest
'''

def interest(amt, int, years):
    return amt * (1+int/100) ** years

print(round(interest(10000, 3.5, 7), 2))