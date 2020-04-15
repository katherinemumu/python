'''
katherinemumu
Apr 14 2020
This program will concatenate the contents of a list
'''

def concat(lst):
    s = ""
    for i in lst:
        s = s + str(i)
    return s

print(concat([1,2,3,4]))