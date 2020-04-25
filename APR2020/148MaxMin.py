'''
katherinemumu
Apr 25 2020
This program will output the max and min from a sequence of numbers
'''
data = [1, 2,4,56,67,123,71, -1]
a = data[0]
b = data[0]

for i in data:
    if i > a:
        a = i
    if i < b:
        b = i

print(a, b)