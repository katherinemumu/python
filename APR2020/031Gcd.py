'''
katherinemumu
Apr 14 2020
This program will calculate the gcd of 2 numbers
'''

def gcd(n1, n2):
    if n2 == 0:
        return n1
    r = n1 % n2
    return gcd(n2, r)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The gcd is", gcd(num1, num2))