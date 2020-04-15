'''
katherinemumu
Apr 14 2020
This program will print out a set of items that are in set1 but not in set2
'''

def sets(s1, s2):
    s = set()
    for i in s1:
        if i not in s2:
            s.add(i)
    return s

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(sets(color_list_1, color_list_2))