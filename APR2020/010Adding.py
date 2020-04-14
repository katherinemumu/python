"""
katherinemumu
Apr 13 2020
This program reads an integer n and prints nnn + nn + n
"""

n = int(input("Enter an integer between 0 and 9 inclusive: "))
n1 = int("%i" %n)
n2 = int("%i%i" %(n, n))
n3 = int("%i%i%i" %(n, n, n))
ded = 3 * n + 2 * n * 10 + n * 100
print("The sum is %i" %(n1 + n2 + n3))