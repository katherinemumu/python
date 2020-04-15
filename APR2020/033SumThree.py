'''
katherinemumu
Apr 15 2020
This program will add 3 integers together, but if two of them are the same, it will return 0
'''

def addThree(n1, n2, n3):
    if (n1 == n2 or n1 == n3 or n2 == n3):
        return 0
    else:
        return n1 + n2 + n3

nums = input("Enter a list of 3 numbers separated by spaces: ")
l = nums.split(" ")
print(addThree(int(l[0]), int(l[1]), int(l[2])))