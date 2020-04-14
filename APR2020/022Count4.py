"""
katherinemumu
Apr 14 2020
This program will count the number of times 4 appears in a list
"""

def list_count_4(lst):
    count = 0
    for i in lst:
        if (i == 4):
            count += 1
    return count

print(list_count_4([1, 4, 5, 6, 4, 6, 4]))
print(list_count_4([4, 4, 4, 4, 4, 4, 4]))