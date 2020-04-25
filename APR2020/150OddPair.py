'''
katherinemumu
Apr 25 2020
This program will find a pair of integers whos product is odd
'''

def yeah(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                p = i * j
                if (p % 2 == 1):
                    return True
    return False

l = [2, 5, 6]

print(yeah(l))
