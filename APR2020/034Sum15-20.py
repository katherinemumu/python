'''
katherinemumu
Apr 15 2020
This program will add 2 integers, and if the sum is in between 15 and 20, it will return 20
'''

def add(n1, n2):
    sum = n1 + n2
    if (15 <= sum <= 20):
        return 20
    else:
        return sum

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

print(add(num1, num2))