'''
katherinemumu
Apr 15 2020
This program will calculate the lcm of 2 numbers
'''

def gcd(n1, n2):
    if n2 == 0:
        return n1
    r = n1 % n2
    return gcd(n2, r)

def lcm(n1, n2):
    g = gcd(n1, n2)
    return g * n1 / g * n2 / g

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The gcd is", lcm(num1, num2))