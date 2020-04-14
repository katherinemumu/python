"""
katherinemumu
Apr 14 2020
This program will find the difference between a number and 17, and if the number is bigger than 17,
then it will return double the absolute difference
"""

def difference(n):
    if (num <= 17):
        print("The answer is", 17 - num)
    else:
        print("The answer is", (num - 17) * 2)

num = int(input("Enter a number: "))

difference(num)