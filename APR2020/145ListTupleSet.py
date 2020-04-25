'''
katherinemumu
Apr 25 2020
This program will check whether smth is a tuple, list, or set
'''

x = [1, 2, 3]

if (type(x) is list):
    print("list")
elif (type(x) is tuple):
    print("tuple")
elif (type(x) is set):
    print("set")
else:
    print("none")
    