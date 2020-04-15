'''
katherinemumu
Apr 15 2020
This program will return True if 2 numbers are equal, or if their sum or difference is equal to 5
'''

def whatIsIt(n1, n2):
    if (n1 == n2):
        return True
    sum = n1 + n2
    diff = abs(n1 - n2)
    if (sum == 5 or diff == 5):
        return True
    return False

print(whatIsIt(4, 4))
print(whatIsIt(11, 6))
print(whatIsIt(2, 3))
print(whatIsIt(5, 0))
print(whatIsIt(2,4))
