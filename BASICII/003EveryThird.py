'''
katherinemumu
Apr 28 2020
This program will remove and print out every third character until the list is empty
'''

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_l = []
idx = 0

while(True):
    if len(l) == 0:
        break
    idx = (idx + 2) % len(l)
    new_l.append(l[idx])
    del l[idx]

print(new_l)
    

